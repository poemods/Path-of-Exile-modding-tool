#!/usr/bin/python3
import binascii
import sys
import time
import re
import os
import threading
import queue

displaylabel=""

masterfilter_restrict=[
        r'\.otc$'
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
    filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
    if re.search(r'disable_rendering\s*=\s*', filedata) is not None :
        filedatamod=re.sub(r'disable_rendering\s*=\s*.*?\n', r'disable_rendering = true\r\n}', filedata)
    else :
        filedatamod=re.sub(r'(Render[\t\r\n ]*\{.*?)\}', r'\g<1>\tdisable_rendering = true\r\n}', filedata, flags=re.DOTALL)
    return filedatamod, encoding, bom


