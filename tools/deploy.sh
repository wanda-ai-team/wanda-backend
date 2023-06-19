cd wanda-backend
sudo docker build -t wandabackend .
docker run -d -it -p 8000:8000 --env-file .env --name=wf wandabackend
