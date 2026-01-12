FROM golang:1.24-alpine

RUN apk add --no-cache git curl unzip python3 py3-pip

RUN git clone https://github.com/v2fly/geoip.git /geoip

RUN curl -L -o /geoip/refilterbeta.txt https://raw.githubusercontent.com/1andrevich/Re-filter-lists/refs/heads/beta/ipsum.lst

RUN curl -L -o /geoip/antifilterdownloadcommunity.txt https://community.antifilter.download/list/community.lst

RUN curl -L -o /geoip/refilter.txt https://raw.githubusercontent.com/1andrevich/Re-filter-lists/refs/heads/main/ipsum.lst

RUN curl -L -o /geoip/refiltercommunity.txt https://raw.githubusercontent.com/1andrevich/Re-filter-lists/refs/heads/main/community_ips.lst

RUN curl -L -o /geoip/antifilternetworksum.txt https://antifilter.network/download/ipsum.lst

RUN curl -L -o /geoip/antifilternetworksubnet.txt https://antifilter.network/download/subnet.lst

RUN curl -L -o /geoip/antifilternetworkcommunity.txt https://antifilter.network/downloads/custom.lst

RUN curl -L -o /geoip/cdn.lst https://raw.githubusercontent.com/mansourjabin/cdn-ip-database/refs/heads/main/data/cdn.lst

RUN curl -L -o /geoip/merged.sum https://raw.githubusercontent.com/PentiumB/CDN-RuleSet/refs/heads/main/release/merged.sum

COPY . /geoip/

RUN mkdir -p /geoip/geolite2

COPY GeoLite2-Country-CSV.zip /geoip/geolite2/

RUN unzip -o /geoip/geolite2/GeoLite2-Country-CSV.zip -d /geoip/geolite2 && \
    mv /geoip/geolite2/GeoLite2-Country-CSV_*/* /geoip/geolite2/ && \
    rmdir /geoip/geolite2/GeoLite2-Country-CSV_*

WORKDIR /geoip

RUN go mod tidy
RUN go mod download

RUN go build -o geoip

CMD ["sh","-c","./geoip -c config-1-init.json && ./geoip -c config-2-sum.json && python3 ipset_ops.py --mode diff --A ./output/text/prepare.txt --B ./refilterbeta.txt,./refilter.txt,./antifilternetworksum.txt,./antifilternetworksubnet.txt,./antifilterdownloadcommunity.txt,./refiltercommunity.txt,./antifilternetworkcommunity.txt,./cdn.lst,./merged.sum,./CUSTOM-LIST-DEL.txt --out ./output/text/final.txt && ./geoip -c config-3-cut.json"]
