FROM wangpanjun/calabash:v1.0.0

MAINTAINER xiaowangzi

# 数据库配置
ENV CALABASH_DATABASE_NAME ineww
ENV CALABASH_DATABASE_USER root
ENV CALABASH_DATABASE_PASSWORD root
ENV CALABASH_DATABASE_HOST 47.93.39.190
ENV CALABASH_DATABASE_PORT 3306


ENV DEBUG FALSE

ADD ./ /app
ADD ./supervisord.conf /etc/supervisor/
ADD ./ineww.conf /etc/supervisor/conf.d/
WORKDIR /app


RUN mkdir /var/log/ineww

RUN pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
EXPOSE 9999 9001