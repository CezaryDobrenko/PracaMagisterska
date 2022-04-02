FROM debian:stable-slim
RUN apt-get update && apt-get install -y cron curl
RUN bash -c '(crontab -l 2>/dev/null; echo "*/5 * * * * /usr/bin/curl -k http://172.16.11.11/scheduler/MINUTE5") | crontab -'
ENTRYPOINT ["cron", "-f"]