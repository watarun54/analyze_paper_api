FROM python:3.6

RUN mkdir /app
ENV APP_ROOT /app
WORKDIR $APP_ROOT

ADD ./requirements.txt $APP_ROOT/requirements.txt
RUN pip install -r $APP_ROOT/requirements.txt
