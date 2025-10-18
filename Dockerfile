FROM golang:1.24-alpine

RUN apk add --no-cache git curl unzip

RUN git clone https://github.com/v2fly/geoip.git /geoip

COPY config-preparing.json /geoip/config-preparing.json

COPY config-finalise.json /geoip/config-finalise.json

RUN mkdir -p /geoip/changes

COPY changes/ /geoip/changes/

RUN mkdir -p /geoip/geolite2

COPY GeoLite2-Country-CSV.zip /geoip/geolite2/

RUN unzip -o /geoip/geolite2/GeoLite2-Country-CSV.zip -d /geoip/geolite2 && \
    mv /geoip/geolite2/GeoLite2-Country-CSV_*/* /geoip/geolite2/ && \
    rmdir /geoip/geolite2/GeoLite2-Country-CSV_*

WORKDIR /geoip

RUN go mod tidy
RUN go mod download

RUN go build -o geoip

CMD ["sh","-c","./geoip -c config-preparing.json && ./geoip -c config-finalise.json"]
