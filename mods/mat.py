#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
        "\.mat$"
        ]

masterfilter_exclude=[
    ]

condition={
   "my_default" : "Additive",
   "Opaque" : "OpaqueNoShadow",
   "OpaqueNoShadow" : "OpaqueNoShadow",
   "AlphaTest" : "AlphaTest",
   "AlphaBlend" : "AlphaBlend",
   "ShadowOnlyAlphaTest" : "Additive",
   "PremultipliedAlphaBlend" : "Additive",
   "MultiplicitiveBlend" : "Additive",
   "AlphaTestWithShadow" : "Additive",
   }

def execute(filename, backupfiledata, modifyggpk):
   filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
   filedatamod=""
   m1=re.search('(Version\s.*\n?)', filedata, flags=re.IGNORECASE)
   if m1 is not None :
      filedatamod+=m1.group(1)
   m2=re.search('BlendMode\s+(\w+)', filedata)
   if m2 is not None :
      blendmode=condition["my_default"]
      for cond in condition :
         if cond == m2.group(1) :
            blendmode=condition[cond]
      filedatamod+="BlendMode "+blendmode+"\r\n"
   m3=re.search('ColourTexture\s.*[\n$]?', filedata)
   if m3 is not None :
      filedatamod+=m3.group(0)
   return filedatamod, encoding, bom

