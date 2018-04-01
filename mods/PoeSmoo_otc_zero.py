#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
        r'\.otc$'
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
    filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
    filedatamod=re.sub(r'\w*Mesh[^\";]*', r'DisableRendering(); ', filedata)
    filedatamod=re.sub(r'(DisableRendering(); ){2,}', r'DisableRendering(); ', filedatamod)
    return filedatamod, encoding, bom

