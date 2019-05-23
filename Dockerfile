FROM python:2.7.10-wheezy
MAINTAINER Zheng Guang "zhuzhengguang@gmail.com"

WORKDIR /code

RUN pip install Flask
ADD . /code

EXPOSE 5000
# Start python
CMD ["python2", "app.py"]
