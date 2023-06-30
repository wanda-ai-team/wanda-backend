docker build -t wandabackend:latest .
docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
docker system prune
docker run -d --privileged -p 8080:8080 --env-file .env wandabackend:latest