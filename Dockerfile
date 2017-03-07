FROM wangpanjun/calabash:v1.0.0

MAINTAINER xiaowangzi


ENV DEBUG FALSE

ADD ./ /app
ADD ./supervisord.conf /etc/supervisor/
ADD ./ineww.conf /etc/supervisor/conf.d/
WORKDIR /app


RUN mkdir /var/log/ineww

RUN pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
EXPOSE 9999 9001