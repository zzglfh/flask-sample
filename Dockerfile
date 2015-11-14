FROM ubuntu
MAINTAINER Zheng Guang "zhuzhengguang@gmail.com"

WORKDIR /code

RUN echo "Asia/Shanghai" > /etc/timezone && \
        dpkg-reconfigure -f noninteractive tzdata
ADD . /code


# Start python
CMD ["python", "app.py"]