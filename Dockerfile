FROM python:3.7

# VOLUME /CH_096_TAQC

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F

RUN apt-get update\
    && apt-get install -y software-properties-common git python3-pip\
    && rm -rf /var/lib/apt/lists/*

RUN apt-add-repository "deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu bionic main"

RUN apt update && apt install -y firefox


ENV APP_URL http://eventexpress.com/
ENV GIT_URL https://github.com/mehalyna/CH_096_TAQC.git
ENV REBUILD "FALSE"

RUN git clone $GIT_URL

RUN pip install -r /CH_096_TAQC/requirements.txt

CMD sh -c "py.test -v /CH_096_TAQC/Tests/test_event_menu.py"