#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
        "/Chests/Breach/.*\.ot$"
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
    filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
    filedatamod=filedata+"\r\nMinimapIcon\r\n{\r\n\ticon = \"Breach\"\r\n}"
    return filedatamod, encoding, bom

