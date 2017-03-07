FROM wangpanjun/calabash:v1.0.0

MAINTAINER xiaowangzi


RUN pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
EXPOSE 9999 9001