FROM golang:1.24-alpine

RUN apk add --no-cache git curl unzip python3

RUN git clone https://github.com/v2fly/geoip.git /geoip

RUN curl -o /geoip/ipsum.lst https://github.com/1andrevich/Re-filter-lists/blob/main/ipsum.lst

RUN curl -o /geoip/merged.sum https://github.com/PentiumB/CDN-RuleSet/blob/main/source/merged.sum

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

CMD ["sh","-c","./geoip -c config-1-init.json && ./geoip -c config-2-sum.json && python ipset_ops.py --mode diff --A /output/text/prepare.txt --B ipsum.lst,merged.sum --out /output/text/final.txt && ./geoip -c config-3-cut.json"]
