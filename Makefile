#!make

install:
		pip3 install -r requirements.txt

run:
		./app.sh test
		#python3 ./app.py

prodtest:
		./app.sh prodtest
		#export PORT=5000 &&\
		#python3 ./wsgi.py

prod:
		./app.sh prod
		#export PORT=8000 &&\
		#uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi

build:
		docker build . -t ubuntu2

docker-dev:
		docker run --rm -ti -e DISPLAY=$(DISPLAY) \
    	-v /tmp/.X11-unix:/tmp/.X11-unix \
			-p 8000:8000 \
		ubuntu2

docker-prod:
		docker run --rm -ti \
			-p 8000:8000 \
		ubuntu2
