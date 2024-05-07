#!/bin/bash

# IMAGE=$1
IMAGE=gym:environments
echo $IMAGE

xhost +;
docker run --rm -it --privileged \
	--runtime=nvidia \
	--gpus all \
	--net host \
	-e DISPLAY \
	--ipc=host \
	-v /tmp/.X11-unix/:/tmp/.X11-unix \
	-v ~/.Xauthority:/root/.Xauthority \
	-e XAUTHORITY=/root/.Xauthority \
	-v ./:/root/ws/ \
	-w /root/ws/ \
	--name gym_envs \
	$IMAGE bash
