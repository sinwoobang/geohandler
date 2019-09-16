# start from an official image
FROM python:3.7.2

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/app/src
WORKDIR /opt/services/app/src

# install our dependencies
# we use --system flag because we don't need an extra virtualenv
COPY requirements /opt/services/app/src/requirements
RUN pip install -r requirements/prod.txt

# copy our project code
COPY . /opt/services/app/src

# expose the port 49152
EXPOSE 49152

# define the default command to run when starting the container
CMD ["gunicorn", "manage:app", "--config=webserver/gunicorn_config.py"]