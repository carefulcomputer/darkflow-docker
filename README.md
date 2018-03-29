# darkflow-docker

Creates a docker image with tensorflow 1.5 and darkflow. 

To create docker image run

docker build -t darkflow .

To run container

docker run -v /tmp:/images -ti darkflow bash

This maps /tmp to /images inside container and starts interactive container. Change as per your need.
Once inside container you can run command like 

flow --imgdir /images/testImages/ --model /darkflow/cfg/yolo.cfg --load /yolo.weights
