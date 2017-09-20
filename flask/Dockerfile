
FROM ubuntu:16.04

RUN apt-get --yes upgrade
RUN apt-get update
RUN apt-get install --yes \
	git \
	python3 \
	python3-dev \
	python3-pip

COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt