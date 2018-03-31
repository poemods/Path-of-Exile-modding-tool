#!/usr/bin/python3
import binascii
import sys
import time
import re
import os
import brotli
import kivy_img_dds
#import npedotnet_dds
#from PIL import Image

displaylabel=""

masterfilter_restrict=[
        "\.dds$"
    ]

masterfilter_exclude=[
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

    try :
        # max size allowed = 64 width or 64 height
        dds = kivy_img_dds.DDSFile(filedata, 64)
        filedata = dds.out
        #print("%d x %d : %d" % (dds.width, dds.height, dds.count))
    except Exception as e :
        print("%s %s" % (str(e), filename))
        return None, None, None

    #try :
    #    dds = npedotnet_dds.DDSReader()
    #    ddsw = dds.getWidth(filedata)
    #    ddsh = dds.getHeight(filedata)
    #    mipmap = dds.getMipmap(filedata)
    #    ddstype = dds.getType(filedata)
    #    if ddstype in npedotnet_dds.imagetype :
    #        print("%4d x %4d %2d 0x%08x %s %s" % (ddsw, ddsh, mipmap, ddstype, npedotnet_dds.imagetype[ddstype], filename))
    #    RGBA = npedotnet_dds.Order(24, 16, 8, 0)
    #    byteimg = dds.read(filedata, RGBA, 0)
    #    image = Image.frombytes('RGBA', (ddsw, ddsw), byteimg)
    #    image.show()
    #except Exception as e :
    #    print("%s %s" % (str(e), filename))

    #if reencodeneeded is True :
    #    filedatal=len(filedata)
    #    newdecsize = (filedatal).to_bytes(4, byteorder='little', signed=True)
    #    filedatamod = newdecsize + brotli.compress(filedata)
    #else :
    #    filedatamod = filedata
    return filedata, None, None


























