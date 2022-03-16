FROM debian:stable-slim
RUN apt-get update && apt-get install -y cron curl
RUN bash -c '(crontab -l 2>/dev/null; echo "*/5 * * * * /usr/bin/curl -k http://172.16.11.11/scheduler/MINUTE5") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "*/15 * * * * /usr/bin/curl -k http://172.16.11.11/scheduler/MINUTE15") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "*/30 * * * * /usr/bin/curl -k http://172.16.11.11/scheduler/MINUTE30") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "*/45 * * * * /usr/bin/curl -k http://172.16.11.11/scheduler/MINUTE45") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "6 */1 * * * /usr/bin/curl -k http://172.16.11.11/scheduler/HOUR1") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "11 */2 * * * /usr/bin/curl -k http://172.16.11.11/scheduler/HOUR2") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "16 */3 * * * /usr/bin/curl -k http://172.16.11.11/scheduler/HOUR3") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "21 */6 * * * /usr/bin/curl -k http://172.16.11.11/scheduler/HOUR6") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "26 */12 * * * /usr/bin/curl -k http://172.16.11.11/scheduler/HOUR12") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "7 12 */1 * * /usr/bin/curl -k http://172.16.11.11/scheduler/DAY1") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "12 12 */2 * * /usr/bin/curl -k http://172.16.11.11/scheduler/DAY2") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "17 12 */3 * * /usr/bin/curl -k http://172.16.11.11/scheduler/DAY3") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "22 12 */4 * * /usr/bin/curl -k http://172.16.11.11/scheduler/DAY4") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "27 12 */5 * * /usr/bin/curl -k http://172.16.11.11/scheduler/DAY5") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "32 12 */6 * * /usr/bin/curl -k http://172.16.11.11/scheduler/DAY6") | crontab -'
RUN bash -c '(crontab -l 2>/dev/null; echo "37 12 */7 * * /usr/bin/curl -k http://172.16.11.11/scheduler/WEEK") | crontab -'
ENTRYPOINT ["cron", "-f"]