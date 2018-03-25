#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
        "^\./Metadata/FmtParent\.aoc$",
        "^\./Metadata/Parent\.aoc$",
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
    filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
    filedatamod=re.sub(r'(ParticleEffects[\t\r\n ]*\{.*?)\}', r'\g<1>tick_when_not_visible = true }', filedata, flags=re.DOTALL)
    return filedatamod, encoding, bom

