FROM python:3.8
RUN mkdir /config
ADD requirements.txt /config/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /config/requirements.txt
RUN mkdir /src
WORKDIR /src