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

with open(os.path.join("assets", "minimal.env"), "rb") as fin :
   filedatamod=fin.read()

def execute(filename, backupfiledata, modifyggpk):
   return filedatamod, None, None

