#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
        "\.mtd$"
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
   filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
   filedatamod=""
   m1=re.search(r'version[ \t]+\d+', filedata, flags=re.IGNORECASE)
   if m1 is not None :
      filedatamod+=m1.group(0)+"\r\n"
   m2=re.search(r'\".*?\"', filedata)
   if m2 is not None :
      filedatamod+="1 0 "+m2.group(0)+"\r\n"
   return filedatamod, encoding, bom

