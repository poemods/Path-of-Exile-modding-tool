#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
        r'\.(ao|aoc|otc)$'
    ]

masterfilter_exclude=[
    ]

condition_aoc=[
   "ClientAnimationController",
   "BoneGroups",
   ]
condition_ao=[
   "AnimationController",
   ]

def execute(filename, backupfiledata, modifyggpk):
   filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
   filedatamod=filedata
   if filename.endswith(".aoc") is True :
      mi=re.finditer(r'(\w+)[ \t\r\n]*\{.*?\}', filedata, flags=re.DOTALL)
      for mii in mi :
         miig=mii.group(1)
         found=False
         for cond in condition_aoc :
            if cond==miig :
               found=True
         if found is False :
            filedatamod=re.sub(miig+r'[ \t\r\n]*\{.*?\}', miig+r'\r\n{\r\n}', filedatamod, flags=re.DOTALL)
   elif filename.endswith(".otc") is True :
      filedatamod=re.sub(r'\".*?;.*?\"', r'"DisableRendering();"', filedata)
      filedatamod=re.sub(r'(Render[\t\r\n ]*\{.*?)\}', r'\g<1>\tdisable_rendering = true\r\n}', filedatamod, flags=re.DOTALL)
   elif filename.endswith(".ao") is True :
      mi=re.finditer(r'(\w+)[ \t\r\n]*\{.*?\}', filedata, flags=re.DOTALL)
      for mii in mi :
         miig=mii.group(1)
         found=False
         for cond in condition_ao :
            if cond==miig :
               found=True
         if found is False :
            filedatamod=re.sub(miig+r'[ \t\r\n]*\{.*?\}', miig+r'\r\n{\r\n}', filedatamod, flags=re.DOTALL)
   return filedatamod, encoding, bom

