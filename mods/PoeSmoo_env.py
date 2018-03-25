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

condition=[
        "FogLinear",
        "FogExp",
    ]


def execute(filename, backupfiledata, modifyggpk):
    filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
    filedatamod = re.sub(r'\n\s*\".*?\.pet\"', r'\n""', filedata)
    mii = re.search(r'\n.*?\".*?\".*\n.*?([1-9]+).*?\n(.*?\".*?\".*?\".*?\n)+', filedata)
    nombrefinal = 0
    if mii is not None :
        nombrefinal = int(mii.group(1))
        for cond in condition :
            mifog = re.finditer(r'\n\s+\"' + cond + r'\"', mii.group(0))
            for mifo in mifog :
                nombrefinal -= 1
        filedatamod = re.sub(r'(\n.*?\".*?\".*\n.*?)[1-9]+(.*?\n(.*?\".*?\".*?\".*?\n)+)', r'\g<1>' + str(nombrefinal) + r'\g<2>', filedatamod)
        for cond in condition :
            filedatamod = re.sub(r'\n\s+\"' + cond + r'\".*\n', r'\n', filedatamod)
    return filedatamod, encoding, bom

