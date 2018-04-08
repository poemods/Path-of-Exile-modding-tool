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
        r'^\./Metadata/Effects/Spells/ground_effects.*\.otc$'
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
    filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
    if re.search(r'on_construction_complete', filedata) is not None :
        filedatamod=re.sub(r'on_construction_complete.*?\n', r'on_construction_complete = "DisableRendering();"\r\n', filedata, flags=re.DOTALL)
    elif re.search(r'BaseEvents[\t\r\n ]*\{', filedata) is not None :
        filedatamod=re.sub(r'(BaseEvents[\t\r\n ]*\{.*?)\}[\t\r ]*(\n|$)', r'\g<1>\ton_construction_complete = "DisableRendering();"\r\n}\r\n', filedata, flags=re.DOTALL)
    else :
        filedatamod=re.sub(r'(extends[\t\r\n ]+\".*?\")', r'\g<1>\r\n\r\nBaseEvents\r\n{\r\n\ton_construction_complete = "DisableRendering();"\r\n}\r\n', filedata, flags=re.DOTALL)
    return filedatamod, encoding, bom


