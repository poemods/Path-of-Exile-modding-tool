#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
        "\.atlas$"
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
   filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
   filedatamod=re.sub(r'\d+(\s+)\d+(\s+)\d+(\s*\n|$)', r'0\g<1>0\g<2>0\r\n', filedata)
   filedatamod=re.sub(r'\n\d+(\s+)\d+\s*\n', r'\n0 0\r\n', filedatamod)
   return filedatamod, encoding, bom

