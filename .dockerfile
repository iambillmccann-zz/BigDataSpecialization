FROM cloudera/quickstart
CMD "/usr/bin/docker-quickstart"

docker run --hostname=quickstart.cloudera --privileged=true -t -i -p 8888:8888 -p 80:80 -p 7180:7180 4239cd2958c6 /usr/bin/docker-quickstart