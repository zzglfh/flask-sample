FROM python:2.7.10-wheezy
MAINTAINER Zheng Guang "zhuzhengguang@gmail.com"

WORKDIR /code

RUN echo "Asia/Shanghai" > /etc/timezone && \
        dpkg-reconfigure -f noninteractive tzdata
RUN apt-get update && apt-get -qqy install python-pip &&  pip install Flask
ADD . /code

EXPOSE 5000
# Start python
CMD ["python2", "app.py"]
