#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
        "\.dlp$"
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
   filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
   filedatamod=""
   m1f=0
   m1=re.search(r'(.*?)\r?\n', filedata)
   if m1 is not None :
      m1f=m1.end(0)
      mi=re.finditer(r'([\d.]+)', m1.group(1))
      if mi is not None :
         mil=0
         for mii in mi :
            mil+=1
         for i in range(0, mil-1) :
            filedatamod+="0 "
         filedatamod+="0\r\n"
   if len(filedata)>m1f :
      filedatamod+=filedata[m1f:]
   return filedatamod, encoding, bom

