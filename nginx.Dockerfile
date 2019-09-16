FROM nginx:latest

COPY ./webserver/nginx/nginx.conf /etc/nginx/nginx.conf
