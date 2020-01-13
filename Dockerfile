FROM python:3.7

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F

RUN apt-get update\
    && apt-get install -y software-properties-common git python3-pip\
    && rm -rf /var/lib/apt/lists/*
    
# Install Firefox browser
RUN apt-add-repository "deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu bionic main"
RUN apt update && apt install -y firefox


ENV APP_URL http://eventexpress.com/
ENV GIT_URL https://github.com/sboris-git/CI_jenkins.git
# ENV PATH_PROJECT /CI_jenkins
ENV REBUILD "FALSE"

# Get POM tests from git
RUN git clone $GIT_URL
WORKDIR $WORKSPACE/CI_jenkins

# Create venv
RUN pip install -r requirements.txt
# WORKDIR $WORKSPACE/CI_jenkins/SelectedTestsToBeRun
# WORKDIR $WORKSPACE/CI_jenkins/Tests
WORKDIR $WORKSPACE/CI_jenkins
RUN ls Tests
RUN pwd
# ENTRYPOINT ["/bin/bash"]
CMD ["py.test", "-v", "--rootdir=Tests", "--alluredir=/CI_jenkins/Reports_Allure"]
# CMD ["py.test", "-v", "--rootdir=Tests", "--alluredir=Reports_Allure"]

# py.test -v --rootdir=Tests --alluredir=Reports_Allure
# CMD ["py.test", "-v", "--setup-show", "--alluredir=/CI_jenkins/Reports_Allure"]

