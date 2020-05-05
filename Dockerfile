FROM ubuntu:19.10 as builder

COPY . /web
WORKDIR /web

# Layer 0
RUN apt update &&\
    apt install make python3 python3-pip -y &&\
    pip3 install --upgrade pip &&\
    python3 -m pip install -r requirement.txt

EXPOSE 8000
ENTRYPOINT [ "make", "prod" ]
