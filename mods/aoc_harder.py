#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
        r'^\./Metadata/Effects/Environment/.*\.aoc$',
        r'^\./Metadata/Effects/Microtransactions/.*\.aoc$',
        r'^\./Metadata/Effects/Spells/.*\.aoc$',
        r'^\./Metadata/Terrain/Doodads/.*\.aoc$',
    ]

masterfilter_exclude=[
    ]

condition=[
   "ClientAnimationController",
   #"SkinMesh",
   "FixedMesh",
   "BoneGroups",
   #"ParticleEffects",
   #"DecalEvents",
   #"Lights",
   #"Sounds",
   #"WindEvents",
   ]

def execute(filename, backupfiledata, modifyggpk):
    filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
    filedatamod=filedata
    mi=re.finditer(r'(\w+)[\t\r\n ]*\{.*?\}[\t\r ]*(\n|$)', filedata, flags=re.DOTALL)
    for mii in mi :
        tagis=mii.group(1)
        found=False
        for cond in condition :
            if cond==tagis :
                found=True
        if found is False :
            filedatamod=re.sub(tagis+r'[\t\r\n ]*\{.*?\}[\t\r ]*(\n|$)', tagis+r'\r\n{\r\n}\r\n', filedatamod, flags=re.DOTALL)
    return filedatamod, encoding, bom

