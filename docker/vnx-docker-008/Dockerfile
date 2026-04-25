# vnx-docker-008 eval target: package manager install without version pinning
FROM ubuntu:22.04

# TRIGGERS rule (no version pins on packages)
RUN apt-get update && apt-get install -y curl wget git

FROM alpine:3.19

# TRIGGERS rule (no version pins)
RUN apk add --no-cache curl bash openssl

CMD ["bash"]
