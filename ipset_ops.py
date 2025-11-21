#!/usr/bin/env python3
from __future__ import annotations
import argparse, os, ipaddress, hashlib
from typing import List
from ipaddress import collapse_addresses, summarize_address_range

def read_nets(p: str):
    if not os.path.exists(p): 
        print(f"  Файл {p} не существует, пропускаем")
        return []
    out=[]
    with open(p,'r',encoding='utf-8',errors='ignore') as f:
        for t in f:
            t=t.strip()
            if not t or t.startswith('#'): continue
            try: out.append(ipaddress.ip_network(t, strict=False))
            except: pass
    print(f"  Файл {p}: прочитано {len(out)} сетей")
    return out

def read_any(base: str):
    if os.path.exists(base + ".list"): 
        print(f"  Пробуем прочитать {base}.list")
        nets = read_nets(base + ".list")
        if nets: return nets
    return read_nets(base)

def read_group(arg: str):
    print(f"Обработка группы: {arg}")
    nets=[]
    parts = [s.strip() for s in arg.split(",") if s.strip()]
    print(f"  Файлы в группе: {len(parts)}")
    for i, part in enumerate(parts, 1):
        print(f"  [{i}/{len(parts)}] Обработка: {part}")
        nets += read_any(part)
    print(f"  Группа завершена: всего {len(nets)} сетей из {len(parts)} файлов")
    return nets

def normalize(nets):
    print(f"Нормализация {len(nets)} сетей...")
    v4=[n for n in nets if n.version==4]
    v6=[n for n in nets if n.version==6]
    result = list(collapse_addresses(v4)) + list(collapse_addresses(v6))
    print(f"  После нормализации: {len(result)} сетей (IPv4: {len(v4)} → {len([n for n in result if n.version==4])}, IPv6: {len(v6)} → {len([n for n in result if n.version==6])})")
    return result

def split_sorted_by_family(nets):
    A4 = sorted([n for n in nets if n.version==4], key=lambda n:int(n.network_address))
    A6 = sorted([n for n in nets if n.version==6], key=lambda n:int(n.network_address))
    print(f"  Сортировка: IPv4: {len(A4)}, IPv6: {len(A6)}")
    return A4, A6

def inter_linear(A, B):
    print(f"  Вычисление пересечения: {len(A)} vs {len(B)} сетей")
    out=[]; i=j=0
    while i<len(A) and j<len(B):
        a,b=A[i],B[j]
        if int(a.broadcast_address)<int(b.network_address): i+=1; continue
        if int(b.broadcast_address)<int(a.network_address): j+=1; continue
        lo=max(int(a.network_address),int(b.network_address))
        hi=min(int(a.broadcast_address),int(b.broadcast_address))
        lo_addr = type(a.network_address)(lo)
        hi_addr = type(a.network_address)(hi)
        out.extend(summarize_address_range(lo_addr, hi_addr))
        if int(a.broadcast_address)<int(b.broadcast_address): i+=1
        else: j+=1
    print(f"  Результат пересечения: {len(out)} сетей")
    return out

def diff_linear(A, B):
    print(f"  Вычисление разности: {len(A)} vs {len(B)} сетей")
    out=[]; i=j=0
    while i < len(A):
        a=A[i]
        a_lo=int(a.network_address); a_hi=int(a.broadcast_address)
        cur=a_lo
        while j < len(B) and int(B[j].broadcast_address) < cur:
            j+=1
        k=j
        while k < len(B) and int(B[k].network_address) <= a_hi:
            b=B[k]
            b_lo=int(b.network_address); b_hi=int(b.broadcast_address)
            if b_lo > cur:
                lo_addr = type(a.network_address)(cur)
                hi_addr = type(a.network_address)(min(a_hi, b_lo-1))
                out.extend(summarize_address_range(lo_addr, hi_addr))
            if b_hi + 1 > a_hi:
                cur=a_hi+1
                break
            else:
                cur=b_hi+1
            k+=1
        if cur <= a_hi:
            lo_addr = type(a.network_address)(cur)
            hi_addr = type(a.network_address)(a_hi)
            out.extend(summarize_address_range(lo_addr, hi_addr))
        if k>j: j=k
        i+=1
    print(f"  Результат разности: {len(out)} сетей")
    return out

def op_intersection(A, B):
    print(f"Операция пересечения между {len(A)} и {len(B)} сетями")
    A4,A6 = split_sorted_by_family(normalize(A))
    B4,B6 = split_sorted_by_family(normalize(B))
    return normalize(inter_linear(A4,B4) + inter_linear(A6,B6))

def op_difference(A, B):
    print(f"Операция разности между {len(A)} и {len(B)} сетями")
    A4,A6 = split_sorted_by_family(normalize(A))
    B4,B6 = split_sorted_by_family(normalize(B))
    return normalize(diff_linear(A4,B4) + diff_linear(A6,B6))

def write_list(path, nets):
    print(f"Запись результата в файл: {path}")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    nets_sorted = sorted(nets, key=lambda n:(n.version, n.prefixlen, int(n.network_address)))
    with open(path,"w",encoding="utf-8") as f:
        for n in nets_sorted:
            f.write(f"{n.network_address}/{n.prefixlen}\n")
    print(f"  Успешно записано {len(nets_sorted)} сетей")

def write_fingerprint(script_path: str, out_path: str):
    if not out_path: 
        print("Файл для отпечатка не указан, пропускаем")
        return
    print(f"Создание отпечатка скрипта: {out_path}")
    with open(script_path, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(h + "\n")
    print(f"  Отпечаток успешно создан: {h}")

def main():
    print("Запуск IP set operations...")
    ap = argparse.ArgumentParser(description="Generic IP set operations")
    ap.add_argument("--mode", choices=["intersect","diff"], required=True)
    ap.add_argument("--set", action="append", default=[], help="group for intersection; comma-separated files per group")
    ap.add_argument("--A", default="", help="minuend group for diff; comma-separated files")
    ap.add_argument("--B", default="", help="subtrahend group for diff; comma-separated files")
    ap.add_argument("--out", required=True, help="output .list")
    ap.add_argument("--fingerprint-out", default="")
    args = ap.parse_args()

    print(f"Режим работы: {args.mode}")
    print(f"Выходной файл: {args.out}")

    if args.mode == "intersect":
        if len(args.set) < 2:
            raise SystemExit("intersect requires at least two --set groups")
        print(f"Обработка {len(args.set)} групп для пересечения")
        groups = []
        for i, group_arg in enumerate(args.set, 1):
            print(f"\n=== Группа {i}/{len(args.set)} ===")
            groups.append(read_group(group_arg))
        
        print(f"\nНачинаем операцию пересечения...")
        res = normalize(groups[0])
        for i, g in enumerate(groups[1:], 1):
            print(f"\n--- Пересечение с группой {i+1} ---")
            res = op_intersection(res, g)
        print(f"\nФинальный результат пересечения: {len(res)} сетей")
        write_list(args.out, res)
    else:
        if not args.A or not args.B:
            raise SystemExit("diff requires --A and --B groups")
        print("Обработка групп для разности")
        
        print(f"\n=== Группа A (minuend) ===")
        A = read_group(args.A)
        print(f"\n=== Группа B (subtrahend) ===")
        B = read_group(args.B)
        
        print(f"\n--- Вычисление разности A - B ---")
        res = op_difference(A, B)
        print(f"\nФинальный результат разности: {len(res)} сетей")
        write_list(args.out, res)

    write_fingerprint(os.path.abspath(__file__), args.fingerprint_out)
    print("\n✅ Операция успешно завершена!")

if __name__ == "__main__":
    main()