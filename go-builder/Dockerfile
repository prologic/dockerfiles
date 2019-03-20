FROM golang:alpine

RUN apk --no-cache -U build-base git make protobuf protobuf-dev && \
	go get -u github.com/golang/protobuf/protoc-gen-go
