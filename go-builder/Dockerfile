FROM golang:alpine

RUN apk add --no-cache -U \
	build-base git make protobuf protobuf-dev && \
	go get -u github.com/golang/protobuf/protoc-gen-go

RUN mkdir /src

ONBUILD WORKDIR /src
ONBUILD COPY . .
ONBUILD RUN /bin/sh -c "[ -f Makefile ] && make || go build"
