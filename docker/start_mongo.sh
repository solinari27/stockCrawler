 docker run --name mongodb -v /home/docker/db:/data/db -p 27017:27017 --restart=always -d mongo --bind_ip 0.0.0.0
