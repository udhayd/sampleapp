FROM ubuntu
RUN apt-get update && apt-get install -y python3 python3-setuptools python3-dev build-essential python3-pip
RUN pip3 install flask
COPY app.py /opt/
ENTRYPOINT python3 /opt/app.py
