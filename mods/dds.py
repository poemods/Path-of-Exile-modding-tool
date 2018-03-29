#!/usr/bin/python3
import binascii
import sys
import time
import re
import os
import brotli
import kivy_img_dds
import npedotnet_dds
from PIL import Image

displaylabel=""

masterfilter_restrict=[
        "\.dds$"
        #"/Art/2DArt/.*\.dds$",
        #"/Art/2DItems/.*\.dds$",
        #"/Art/Microtransactions/.*\.dds$",
        #"/Art/Models/.*\.dds$",
        #"/Art/particles/.*\.dds$",
        #"/Art/Textures/Characters/.*\.dds$",
        #"/Art/Textures/Doodads/.*\.dds$",
        #"/Art/Textures/Environment/.*\.dds$",
        #"/Art/Textures/Interface/2D/.*\.dds$",
        #"/Art/Textures/Items/.*\.dds$",
        #"/Art/Textures/Misc/.*\.dds$",
        #"/Art/Textures/Monsters/.*\.dds$",
        #"/Art/Textures/NPC/.*\.dds$",
        #"/Art/Textures/Pet/.*\.dds$",
        #"/Metadata/EnvironmentSettings/.*\.dds$",
        #"/minimap/.*\.dds$",
    ]

masterfilter_exclude=[
        #"/art/2dart/cubemaps/",
    ]

with open(os.path.join("assets", "minimal.dds"), "rb") as fin :
   minimaldds=fin.read()

'''

Unsupported FOURCC 71

Invalid mipmap without flags 8

Truncated image for mipmap 8 6
Truncated image for mipmap 0 1

rgba 5548
s3tc_dxt1 8747
s3tc_dxt2 118
s3tc_dxt3 1536
s3tc_dxt4 4495
s3tc_dxt5 18098
luminance_alpha 1

'''

def execute(filename, filedata, modifyggpk):
    if filedata[0] == ord("*") and filedata[3]>=0x20 :
        return None, None, None
    reencodeneeded=False
    if filedata[:4] != b'DDS ' :
        reencodeneeded=True
        size = int.from_bytes(filedata[:4], 'little')
        filedata = brotli.decompress(filedata[4:])
        if len(filedata)!=size :
            print("Error wrong size after brotli decode")
            return None, None, None
    #try:
        #dds = kivy_img_dds.DDSFile(data=filedata)
        #width, height = dds.size
        # print("%d x %d : %s : %s" % (width, height, str(dds.dxt), filename))
        # dds.images[0]
    #except Exception as e :
    #    print("%s %s" % (filename, str(e)))

    dds = npedotnet_dds.DDSReader()
    ddsw = dds.getWidth(filedata)
    ddsh = dds.getHeight(filedata)
    mipmap = dds.getMipmap(filedata)
    try :
        ddstype = dds.getType(filedata)
        #print("%4d x %4d %2d 0x%08x %s" % (ddsw, ddsh, mipmap, ddstype, filename))
    except Exception as e :
        print("%4d x %4d %2d %s " % (ddsw, ddsh, mipmap, filename) + str(e))

    #ARGB = npedotnet_dds.Order(16, 8, 0, 24)
    #RGBA = npedotnet_dds.Order(24, 16, 8, 0)
    #img = dds.read(filedata, RGBA, 0)
    #byteimg=b''
    #for pix in img :
    #    byteimg+=(pix).to_bytes(8, byteorder='little', signed=True)
    #image = Image.frombytes('RGBA', (w, h), byteimg)
    #image.show()

    # dds.images[0]



    #if reencodeneeded is True :
    #    filedatal=len(filedata)
    #    newdecsize = (filedatal).to_bytes(4, byteorder='little', signed=True)
    #    filedatamod = newdecsize + brotli.compress(filedata)
    #else :
    #    filedatamod = filedata
    #return filedatamod, None, None
    return None, None, None


























