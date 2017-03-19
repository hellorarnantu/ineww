FROM wangpanjun/calabash:v1.0.0

MAINTAINER xiaowangzi

# 数据库配置
ENV INEWW_DATABASE_NAME ineww
ENV INEWW_DATABASE_USER root
ENV INEWW_DATABASE_PASSWORD root
ENV INEWW_DATABASE_HOST localhost
ENV INEWW_DATABASE_PORT 3306


ENV DEBUG FALSE

ADD ./ /app
ADD ./supervisord.conf /etc/supervisor/
ADD ./ineww.conf /etc/supervisor/conf.d/
WORKDIR /app


RUN mkdir /var/log/ineww

RUN pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
EXPOSE 9999