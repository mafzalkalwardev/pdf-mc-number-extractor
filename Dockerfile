FROM alpine:3.20
WORKDIR /src
COPY . .
LABEL org.opencontainers.image.source="https://github.com/mafzalkalwardev/pdf-mc-number-extractor"
CMD ["sh", "-c", "echo 'pdf-mc-number-extractor source package' && ls -1"]
