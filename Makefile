export VERSION=latest

build:
	docker-compose build

up: build
	docker-compose up 

rm:
	docker-compose rm -f
