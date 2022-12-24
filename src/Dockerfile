FROM python:3.7.16-slim

WORKDIR /app

COPY ./ /app/

RUN pip install pyTelegramBotApi mysql-connector-python watchdog psutil

# RUN chmod +x ./start.sh

ENTRYPOINT python start_db.py ; python bot.py
# ENTRYPOINT ["tail", "-f", "/dev/null"]