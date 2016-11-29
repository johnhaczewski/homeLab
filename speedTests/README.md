# speedTest Scripts

> Test your internet connection speed and ping using [speedtest.net](http://www.speedtest.net) from the CLI. This is then parsed for upload to InfluxDB to be used in a Grafana dashboard.

## Install

```
These are currently setup to be ran in a crontab

*/10 * * * * /home/user/speedtest-cli --simple > /var/log/speedtests/wan_speedtests.log && /home/user/speed_parse.py
```

## Usage

```
For a manual run:

user@ubuntu:~/git/nformant/homeLab$ /home/user/speedtest-cli --simple
Ping: 16.953 ms
Download: 17.44 Mbit/s
Upload: 2.36 Mbit/s
```


## Related

- [speedtest-cli](https://github.com/sivel/speedtest-cli) - Test your download speed using speedtest.net
