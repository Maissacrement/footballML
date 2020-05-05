FROM ubuntu:19.10 as builder

ENV DEV_HOME=/home/developer \
    uid=1000 gid=1000

# DEV USER
RUN mkdir -p ${DEV_HOME} ${DEV_HOME}/app && \
    echo "developer:x:${uid}:${gid}:Developer,,,:${DEV_HOME}:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group &&\
    rm -rf /var/cache/apk/*

COPY . ${DEV_HOME}/app
WORKDIR ${DEV_HOME}/app

# Layer 0
RUN apt update &&\
    apt install make python3.8 python3-pip -y &&\
    pip3 install --upgrade pip

# ADD REPO RIGTH
RUN chown -R developer:developer ${DEV_HOME}/app

RUN python3 -m pip install -r requirement.txt

USER developer

EXPOSE 8000
ENTRYPOINT [ "make", "prod" ]
