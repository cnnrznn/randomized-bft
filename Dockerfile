FROM ubuntu:xenial

RUN apt-get update
RUN apt-get install -y python3

ADD src src

ENTRYPOINT ["python3", "-u", "src/replica.py"]
