#!/usr/bin/python

import os,sys
from time import time
from random import seed
from random import random
from datetime import datetime

seed(1)

def read_with_lseek(FILE, LOG):

  SIZE = os.stat(FILE).st_size

  START=time()
  for i in range(10):
    fd = os.open(FILE,os.O_RDONLY)
    LIST = [4, 4, 4, 4, 10, 10, 100, 1000, 10000, 100000]*100
    for BYTES in LIST:
      OFFSET = int(random()*(SIZE - 200000))
      os.lseek(fd,OFFSET,0)
      os.read(fd,BYTES)
      #print str(OFFSET) + "," + str(BYTES)
    os.close(fd)
  END=time()

  #print "========================================"
  #print "File: " + FILE
  #print "Elapsed Time: " + str((END-START))
  #print "========================================"
  
  log = open(LOG,"a")
  log.write(str(datetime.now()) + "," + str(END-START) + "\n")
  log.close()

if len(sys.argv) != 3: 
  print "Usage: lseekv2.py <Full path of the data file to read> <Full path of the output file>"
  print "Example lseekv2.py /opt/mnt/20190731/#####.dat /tmp/metrics.csv"
  sys.exit()

#print len(sys.argv)
#print sys.argv[1]
#print sys.argv[2]

read_with_lseek(sys.argv[1], sys.argv[2])

