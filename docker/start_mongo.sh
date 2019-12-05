 docker run --name mongodb --network=host -v /home/docker/db:/data/db -p 27017:27017 --restart=always -d mongo
