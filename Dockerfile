
FROM ubuntu:16.04

RUN apt-get update; apt-get --yes upgrade; apt-get install --yes git redis-server python3 python3-dev  gcc build-essential g++ libffi-dev libncurses5-dev sudo vim sqlite3 python3-pip

COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
