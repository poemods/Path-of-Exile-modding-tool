#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
        "^\./Shaders/Renderer/Shadows.ffx$"
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
    filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
    filedatamod=re.sub(r'DECLARATIONS[^\n]*shadow_map_generation.*?\}\}', r'DECLARATIONS shadow_map_generation\r\n{{\r\n}}', filedata, flags=re.DOTALL)
    filedatamod=re.sub(r'FRAGMENT[^\n]*shadow_map_projection.*?\}\}', r'FRAGMENT shadow_map_projection\r\n{{\r\n}}', filedatamod, flags=re.DOTALL)
    return filedatamod, encoding, bom


