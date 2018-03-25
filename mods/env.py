#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
        "\.env$"
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
   filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
   filedatamod=re.sub(r'\n.*?\".*?\".*\n.*?[1-9]+.*?\n(.*?\".*?\".*?\".*?\n)+', r'\n""\r\n0\r\n', filedata)
   return filedatamod, encoding, bom

