# fail2ban-report
This tool generates a simple report of fail2ban activity.

[Sample Log File](log.csv)

[Sample PDF report](report.pdf)

## Requirements

* Python 3
* A GeoLite2-Country.mmdb file (see setup details below)

## Setup

`pip3 install -r requirements.txt`

If you want to start from scratch and don't want to use the sample data files, delete log.csv otherwise the sample data will be added to your report. fail2ban-getlog automatically checks to see if this file exists and creates the file it doesn't. report.pdf will be overwritten when you generate a report.

Get your GeoLite2-Country.mmdb file which can be obtained by going [here](https://dev.maxmind.com/geoip/geoip2/geolite2/#Download%20Access) and clicking on the "SIGN UP FOR GEOLITE2" button. Once you have signed up, in your account summary page, you should see a link to "Download Databases". From there, download the "GeoLite2 Country" gzip which should contain the GeoLite2-Country.mmdb file. Put this file in the root directory of where the fail2ban-getlog.py and the fail2ban-report.py files are located.

## Extract fail2ban logs in a CSV file

```bash
$ ./fail2ban-getlog log.csv
```
You should create a cron task to regulary run `/.fail2ban-getlog log.csv` to update the log file as ban events occur as the fail2ban log files are rotated.

## Generate the PDF report using the CSV data and GeoLite2-Country database

```bash
./fail2ban-report log.csv GeoLite2-Country.mmdb report.pdf
```