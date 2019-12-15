FROM python:3.7-slim
#add a non-root user
RUN useradd -m "docker-user"
#change to user dir
WORKDIR /home/docker-user
#copy requirements file, don't copy other files yet so that the pip install doesn't get triggered after every change
COPY ["requirements.pip", "./"]
#install required packages into home dir
RUN pip install -r "requirements.pip"
#now copy required files
COPY ["./jdcs", "./jdcs"]
COPY ["./tests", "./tests"]
COPY ["./wsgi.py", "./"]
#change to non-root user
USER docker-user
#listen port for gunicorn
ENV APP_PORT=8080
#run gunicorn
CMD ["sh", "-c", "gunicorn wsgi:app -b 0.0.0.0:$APP_PORT -w 2 --worker-tmp-dir /dev/shm"]
