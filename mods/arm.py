#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
        "\.arm$"
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
   filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
   filedatamod=re.sub(r'\n([\d]+)\r?\n(([\d.\-e]+[ \t]+)+\"Metadata.+\"\s+\"[^M].+\"\r?\n)+', r'\n0\n', filedata)
   return filedatamod, encoding, bom

