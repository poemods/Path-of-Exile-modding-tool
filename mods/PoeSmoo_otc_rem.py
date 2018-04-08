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
        r'^\./Metadata/Monsters/Monster.otc$',
        r'^\./Metadata/Characters/Character.otc$',
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
    filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
    filedatamod=filedata

    if re.search(r'disable_rendering\s*=\s*', filedatamod) is not None :
        filedatamod=re.sub(r'disable_rendering\s*=\s*.*?\n', r'disable_rendering = true\r\n}', filedatamod)
    else :
        filedatamod=re.sub(r'(Render[\t\r\n ]*\{.*?)\}[\t\r ]*(\n|$)', r'\g<1>\tdisable_rendering = true\r\n}\r\n', filedatamod, flags=re.DOTALL)

    if re.search(r'on_construction_complete', filedatamod) is not None :
        if re.search(r'on_construction_complete.*DisableRendering', filedatamod) is None :
            filedatamod=re.sub(r'on_construction_complete.*?\n', r'on_construction_complete = "RemoveEffects();"\r\n', filedatamod, flags=re.DOTALL)
    elif re.search(r'BaseEvents[\t\r\n ]*\{', filedatamod) is not None :
        filedatamod=re.sub(r'(BaseEvents[\t\r\n ]*\{.*?)\}[\t\r ]*(\n|$)', r'\g<1>\ton_construction_complete = "RemoveEffects();"\r\n}\r\n', filedatamod, flags=re.DOTALL)
    else :
        filedatamod=re.sub(r'(extends[\t\r\n ]+\".*?\")', r'\g<1>\r\n\r\nBaseEvents\r\n{\r\n\ton_construction_complete = "RemoveEffects();"\r\n}\r\n', filedatamod, flags=re.DOTALL)
    return filedatamod, encoding, bom


