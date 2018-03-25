#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
        "\.ffx$"
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
    filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
    filedatamod=re.sub(r'(DECLARATIONS|FRAGMENT).*?(\w+).*?\}\}', r'\g<1> \g<2>\r\n{{\r\n}}', filedata, flags=re.DOTALL)
    return filedatamod, encoding, bom

