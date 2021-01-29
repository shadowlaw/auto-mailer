FROM python:3

RUN mkdir /etc/opt/auto-mailer

WORKDIR /etc/opt/auto-mailer

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT python run.py
