FROM ubuntu:22.04
WORKDIR /app
ADD https://example.com/scripts/setup.sh /app/setup.sh
RUN chmod +x /app/setup.sh && /app/setup.sh
USER app
CMD ["/app/run"]
