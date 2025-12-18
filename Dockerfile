FROM golang:1.24-alpine

RUN apk add --no-cache git curl unzip python3 py3-pip

RUN git clone https://github.com/v2fly/geoip.git /geoip

RUN curl -L -o /geoip/antifilter.txt https://antifilter.download/list/allyouneed.lst

RUN curl -L -o /geoip/refilter.txt https://raw.githubusercontent.com/1andrevich/Re-filter-lists/refs/heads/main/ipsum.lst

RUN curl -L -o /geoip/refiltercommunity.txt https://raw.githubusercontent.com/1andrevich/Re-filter-lists/refs/heads/main/community_ips.lst

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

CMD ["sh","-c","./geoip -c config-1-init.json && ./geoip -c config-2-prepare.json && python3 ipset_ops.py --mode intersect --set ./output/text/directprepare.txt,./output/text/proxyprepare.txt --out ./output/text/proxyfinalise.txt && ./geoip -c config-3-finalise.json"]
