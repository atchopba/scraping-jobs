# The docker image we base our one from
FROM python:3.10.1

# Information of the maintainer of this file
MAINTAINER "Who I am <atchopba@gmail.com>"

# We copy the content of the directory to /opt/app in the container
# COPY . /opt/app

ADD *.py /
ADD requirements.txt /

#
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# We change of directory to /opt/app
WORKDIR .

# We execute by default the jobs_index.py file
ENTRYPOINT ["python", "./index.py"]
