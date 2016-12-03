FROM python:3-onbuild
EXPOSE 5000
EXPOSE 80
RUN apt update && apt install nginx -y
COPY nginx.config /etc/nginx/sites-available/default
ENV FLASK_APP run_server.py
ENTRYPOINT service nginx start && flask run