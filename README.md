# fail2ban-report
This tool generate a simple report of fail2ban activity.

# Installation and Requirements

## Requirements

* It's highly reccomended that you use Python 3.

* This script requires ATLAS(Automatically Tuned Linear Algebra Software) which is a dependency of numpy. If you get an error such as:

  ```Original error was: libf77blas.so.3: cannot open shared object file: No such file or directory```

  you will need to install it with something like (on a linux system for example):

  ```bash
  sudo apt-get install libatlas-base-dev
  ```

* It also requires the following Python libraries:

  ```
  pandas
  matplotlib
  geoip2
  ```
  which can be installed using pip with the included requirements.txt file explained below.

* The Maxmind GeoLite2 Database in mmdb format which can be found [here](https://dev.maxmind.com/geoip/geoip2/geolite2/). You need to sign up for an account unfortunately so I may change this at some stage. Place the database (you aquire usually named ```GeoLite2-Country.mmdb```) in the same folder as the scripts reside.

## Installation

Clone the repository from GitHub:

```git clone git@github.com:jamespayne/fail2ban-report.git```

Change directory into the cloned repo:

```cd fail2ban-report```

### Within a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Without a virtual environment

```bash
pip3 install -r requirements.txt
```

## Usage

### Generate the report from the sample log data:

```python3 fail2ban-report.py log_sample.csv GeoLite2-Country.mmdb report_sample.pdf```

### Extract fail2ban logs in a CSV file

This requires sudo as you are reading from ```/var/log/fail2ban.log```

```
$ sudo python3 fail2ban-getlog.py log.csv
```

You can create a cron task to regulary run ```fail2ban-getlog.py log.csv``` and populate CSV file. Each time you run ```fail2ban-getlog.py```, it will append the results to log.csv so be aware this file may get quite large as time passes.

If you do decide to use cron to run the scripts and you are using a virtual environment, you need to make sure you call it from there with the full path of the python executable within the virtual environment such as:

```$HOME/fail2ban-report/.venv/bin/python3 $HOME/fail2ban-report/fail2ban-getlog.py log.csv```

or

```$HOME/fail2ban-report/venv/bin/python3 $/HOME/fail2ban-report/fail2ban-report.py log.csv GeoLite2-Country.mmdb report.pdf```

## Generate the PDF report using the CSV data and GeoLite2-Country database

```bash
python3 fail2ban-report.py log.csv GeoLite2-Country.mmdb report.pdf
```