#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import ipaddress
import os
from ipaddress import collapse_addresses, summarize_address_range


def read_nets(p: str):
    if not os.path.exists(p):
        return []
    out = []
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        for t in f:
            t = t.strip()
            if not t or t.startswith("#"):
                continue
            try:
                out.append(ipaddress.ip_network(t, strict=False))
            except Exception:
                pass
    return out


def read_any(base: str):
    if os.path.exists(base + ".list"):
        nets = read_nets(base + ".list")
        if nets:
            return nets
    return read_nets(base)


def read_group(arg: str):
    nets = []
    for part in [s.strip() for s in arg.split(",") if s.strip()]:
        nets.extend(read_any(part))
    return nets


def normalize(nets):
    v4 = [n for n in nets if n.version == 4]
    v6 = [n for n in nets if n.version == 6]
    return list(collapse_addresses(v4)) + list(collapse_addresses(v6))


def split_sorted_by_family(nets):
    A4 = sorted(
        [n for n in nets if n.version == 4], key=lambda n: int(n.network_address)
    )
    A6 = sorted(
        [n for n in nets if n.version == 6], key=lambda n: int(n.network_address)
    )
    return A4, A6


def inter_linear(A, B):
    out = []
    i = j = 0
    while i < len(A) and j < len(B):
        a, b = A[i], B[j]
        if int(a.broadcast_address) < int(b.network_address):
            i += 1
            continue
        if int(b.broadcast_address) < int(a.network_address):
            j += 1
            continue
        lo = max(int(a.network_address), int(b.network_address))
        hi = min(int(a.broadcast_address), int(b.broadcast_address))
        lo_addr = type(a.network_address)(lo)
        hi_addr = type(a.network_address)(hi)
        out.extend(summarize_address_range(lo_addr, hi_addr))
        if int(a.broadcast_address) < int(b.broadcast_address):
            i += 1
        else:
            j += 1
    return out


def diff_linear(A, B):
    out = []
    i = j = 0
    while i < len(A):
        a = A[i]
        a_lo = int(a.network_address)
        a_hi = int(a.broadcast_address)
        cur = a_lo
        while j < len(B) and int(B[j].broadcast_address) < cur:
            j += 1
        k = j
        while k < len(B) and int(B[k].network_address) <= a_hi:
            b = B[k]
            b_lo = int(b.network_address)
            b_hi = int(b.broadcast_address)
            if b_lo > cur:
                lo_addr = type(a.network_address)(cur)
                hi_addr = type(a.network_address)(min(a_hi, b_lo - 1))
                out.extend(summarize_address_range(lo_addr, hi_addr))
            if b_hi + 1 > a_hi:
                cur = a_hi + 1
                break
            else:
                cur = b_hi + 1
            k += 1
        if cur <= a_hi:
            lo_addr = type(a.network_address)(cur)
            hi_addr = type(a.network_address)(a_hi)
            out.extend(summarize_address_range(lo_addr, hi_addr))
        if k > j:
            j = k
        i += 1
    return out


def op_intersection(A, B):
    A4, A6 = split_sorted_by_family(normalize(A))
    B4, B6 = split_sorted_by_family(normalize(B))
    return normalize(inter_linear(A4, B4) + inter_linear(A6, B6))


def op_difference(A, B):
    A4, A6 = split_sorted_by_family(normalize(A))
    B4, B6 = split_sorted_by_family(normalize(B))
    return normalize(diff_linear(A4, B4) + diff_linear(A6, B6))


def write_list(path, nets):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)

    nets_sorted = sorted(
        nets, key=lambda n: (n.version, n.prefixlen, int(n.network_address))
    )
    with open(path, "w", encoding="utf-8") as f:
        for n in nets_sorted:
            f.write(f"{n.network_address}/{n.prefixlen}\n")


def write_fingerprint(script_path: str, out_path: str):
    if not out_path:
        return
    with open(script_path, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    d = os.path.dirname(out_path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(h + "\n")


def main():
    ap = argparse.ArgumentParser(description="Generic IP set operations")
    ap.add_argument("--mode", choices=["intersect", "diff"], required=True)
    ap.add_argument(
        "--set",
        action="append",
        default=[],
        help="group for intersection; comma-separated files per group",
    )
    ap.add_argument(
        "--A", default="", help="minuend group for diff; comma-separated files"
    )
    ap.add_argument(
        "--B", default="", help="subtrahend group for diff; comma-separated files"
    )
    ap.add_argument("--out", required=True, help="output .list")
    ap.add_argument("--fingerprint-out", default="")
    args = ap.parse_args()

    if args.mode == "intersect":
        if len(args.set) < 2:
            raise SystemExit("intersect requires at least two --set groups")
        groups = [read_group(s) for s in args.set]
        res = normalize(groups[0])
        for g in groups[1:]:
            res = op_intersection(res, g)
        write_list(args.out, res)
    else:
        if not args.A or not args.B:
            raise SystemExit("diff requires --A and --B groups")
        A = read_group(args.A)
        B = read_group(args.B)
        res = op_difference(A, B)
        write_list(args.out, res)

    write_fingerprint(os.path.abspath(__file__), args.fingerprint_out)


if __name__ == "__main__":
    main()
