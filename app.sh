#!/bin/bash

function prodtest(){
    export PORT=5000 &&\
    python3 ./wsgi.py
}

function prod(){
    export PORT=8000 &&\
    uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi
}

function main(){
    echo $1
    if [ $1 == "prod" ];then
        prod
    elif [ $1 == "test" ]
    then
        prodtest
    else
        python3 ./app.py
    fi
}

function finish(){
    exit 0
}

trap finish EXIT

main $1
