#!/usr/bin/python3
import binascii
import sys
import time
import re
import os
import brotli
from wand.image import Image

displaylabel=""

masterfilter_restrict=[
        #"/Art/2DArt/.*\.dds$",
        #"/Art/2DItems/.*\.dds$",
        "/Art/Microtransactions/.*\.dds$",
        "/Art/Models/.*\.dds$",
        "/Art/particles/.*\.dds$",
        #"/Art/Textures/Characters/.*\.dds$",
        "/Art/Textures/Doodads/.*\.dds$",
        "/Art/Textures/Environment/.*\.dds$",
        #"/Art/Textures/Interface/2D/.*\.dds$",
        "/Art/Textures/Items/.*\.dds$",
        "/Art/Textures/Misc/.*\.dds$",
        "/Art/Textures/Monsters/.*\.dds$",
        "/Art/Textures/NPC/.*\.dds$",
        "/Art/Textures/Pet/.*\.dds$",
        "/Metadata/EnvironmentSettings/.*\.dds$",
        "/minimap/.*\.dds$",
    ]

masterfilter_exclude=[
        "/art/2dart/cubemaps/",
    ]

with open(os.path.join("assets", "minimal.dds"), "rb") as fin :
   minimaldds=fin.read()

def execute(filename, filedata, modifyggpk):
    if filedata[0] == b'*' and filedata[3]>=0x20 :
        return None, None, None
    reencodeneeded=False
    if filedata[:4] != b'DDS ' :
        reencodeneeded=True
        size = int.from_bytes(filedata[:4], 'little')
        filedata = brotli.decompress(filedata[4:])
        if len(filedata)!=size :
            return None, None, None
    try :
        maxw=20.0
        with Image(blob=filedata) as img :
            mw=img.width
            mh=img.height
            if mw>=mh :
                resizeratio=maxw/mw
            else :
                resizeratio=maxw/mh
            if resizeratio<0.9 :
                newwidth=int(mw*resizeratio)
                newheight=int(mh*resizeratio)
                img.resize(newwidth, newheight)
                filedata=img.make_blob()
    except :
        return None, None, None
    if reencodeneeded is True :
        filedatal=len(filedata)
        newdecsize = (filedatal).to_bytes(4, byteorder='little', signed=True)
        filedatamod = newdecsize + brotli.compress(filedata)
    else :
        filedatamod = filedata
    return filedatamod, None, None












