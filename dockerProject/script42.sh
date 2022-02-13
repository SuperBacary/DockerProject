docker container stop python
docker container rm python
docker rmi python:latest

docker volume create monvolume
docker build -t python .
docker run -idt --name python -p 4242:5000 --mount source=monvolume,target=/data python
