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
        "\.ao$"
    ]

masterfilter_exclude=[
    ]

condition=[
    #"AnimationController",
    "Hull",
    #"AttachedAnimatedObjects",
    ]

def execute(filename, backupfiledata, modifyggpk):
    filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
    filedatamod=re.sub(r'Hull[\t\r\n ]*\{.*?\}', r'Hull\r\n{\r\n}', filedata, flags=re.DOTALL)
#     filedatamod=filedata
#     mi=re.finditer(r'((\w+)[\t\r\n ]*\{.*?\})', filedatamod, flags=re.DOTALL)
#     for mii in mi :
#         tagis=mii.group(2)
#         for cond in condition :
#             if cond==tagis :
#                 filedatamod=re.sub(tagis+r'[\t\r\n ]*\{.*?\}', tagis+r'\r\n{\r\n}', filedatamod, flags=re.DOTALL)
    return filedatamod, encoding, bom

