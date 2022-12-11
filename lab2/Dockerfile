FROM python:3.8

RUN apt-get update -y
RUN apt install iputils-ping -y
COPY mtu_resolver.py /

ENTRYPOINT ["python3", "mtu_resolver.py"]