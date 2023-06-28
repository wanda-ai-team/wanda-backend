docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
docker system prune
sudo docker build -t wandabackend:latest .
sudo docker run -d --privileged -p 8080:80 --env-file .env wandabackend:latest