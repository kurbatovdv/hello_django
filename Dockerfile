# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=hello_django Version=0.0.1
EXPOSE 3000

# Indicate where uwsgi.ini lives
ENV UWSGI_INI uwsgi.ini

RUN apt-get update -y && apt-get install libldap2-dev libsasl2-dev ldap-utils -y

WORKDIR /app
ADD . /app

# Using pip:
RUN python3 -m pip install -r requirements.txt
CMD exec gunicorn web_project.wsgi:application --bind 0.0.0.0:3000 --workers 3

# Using pipenv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "hello_django"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m hello_django"
