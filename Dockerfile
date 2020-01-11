FROM python:3.7

# VOLUME /CI_jenkins

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F

RUN apt-get update\
    && apt-get install -y software-properties-common git python3-pip\
    && rm -rf /var/lib/apt/lists/*

RUN apt-add-repository "deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu bionic main"

RUN apt update && apt install -y firefox


ENV APP_URL http://eventexpress.com/
ENV GIT_URL https://github.com/sboris-git/CI_jenkins.git
ENV REBUILD "FALSE"

RUN git clone $GIT_URL
WORKDIR $WORKSPACE/CI_jenkins
RUN pip install -r requirements.txt
RUN cat requirements.txt
# CMD sh -c "py.test -v /CI_jenkins/Tests/test_event_menu.py"
ENTRYPOINT ["py.test -v"]
# CMD ["-s",  "$CI_jenkins/Tests/test_linkedin_tmp_boris.py", "--alluredir=I_jenkins/Allure_results"]
