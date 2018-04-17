# darkflow-docker

Creates a docker image with tensorflow 1.5 and darkflow. 

To create docker image clone this repo

git clone https://github.com/qwertangel/darkflow-docker.git

and then run this command from directory which has Dockerfile...

docker build -t darkflow .

To start container

docker run -v /tmp:/images -ti darkflow bash

This maps /tmp on your host machine to /images folder inside container and starts interactive container. Change as per your need.
Once inside container you can run command like 

flow --imgdir /images/testImages/ --model /darkflow/cfg/yolo.cfg --load /yolo.weights

detect.py file reads a rtsp stream, grabs a frame and runs it through predection, filters out everything other than 'person' lable and then if size of detection is more than a specific size (don't want people far away to be detected) then draw a box around that person and save images. Next planning to add some sort of push notification to cell phone with detected image.
