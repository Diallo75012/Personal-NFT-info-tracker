# initially 3.9 but we put 3.8 because of our local environment python which is a 3.8.10
FROM python:3.8-buster 

# install nginx in container and copy our config default file to nginx default location, create log links
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# prepare directories for our app inside the container and copy files and dirs to the right place. define working directory and install requirements.txt, then set owner of the dirs
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/webapp
COPY requirements.txt start-server.sh /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY . /opt/app/webapp/
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

# expose the port 8020 (nginx reverse proxy) for contaienr to receive connections on it and launch the gunicor http server to have a container ready waiting for connections (8020 -> 8010)
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]

# think for the future in how to improve this Dockerfile and make container accepting connections for ssh for example...
