FROM ubuntu:latest
LABEL authors="zcy"

ENTRYPOINT ["top", "-b"]