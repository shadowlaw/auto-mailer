FROM python:3

RUN mkdir /etc/opt/auto-mailer

WORKDIR /etc/opt/auto-mailer

COPY . .

VOLUME /etc/opt/auto-mailer/app/logs
VOLUME /etc/opt/auto-mailer/app/config
VOLUME /etc/opt/auto-mailer/app/assets/message_data/email

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update -y
RUN apt-get install -y tzdata

ENTRYPOINT python run.py
