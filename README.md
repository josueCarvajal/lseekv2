# lseekv2
This allows you to measure the time of reading different bytes of datafiles with a cron job

Usage: lseekv2.py <Full path of the data file to read> <Full path of the output file>"
Example lseekv2.py /opt/mnt/20190731/#####.dat /tmp/metrics.csv"

Requires to be scheduled with a cron job to get different metrics after a period of time. 
The output file is in a comma separated format
