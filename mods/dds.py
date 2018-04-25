import brotli
import kivy_img_dds

'''

restriction "\.dds$"

'''

#with open(os.path.join("assets", "minimal.dds"), "rb") as fin :
#   minimaldds=fin.read()

def execute(filename, filedata, modifyggpk):
    if filedata[0] == ord("*") and filedata[3]>=0x20 :
        return None, None, None
    reencodeneeded=False
    if filedata[:4] != b'DDS ' :
        reencodeneeded=True
        size = int.from_bytes(filedata[:4], 'little')
        filedata = brotli.decompress(filedata[4:])
        if len(filedata)!=size :
            print("Error wrong size after brotli decode %s" % (filename))
            return None, None, None

    try :
        dds = kivy_img_dds.DDSFile(filedata)

        # reduce image size :
        #
        #   -  by factor 3 :
        # filedata = dds.stripratiomipmap(3)
        #
        #   -  or max size allowed = width or height 32 :
        # filedata = dds.stripbiggermipmapthan(32)

        filedata = dds.stripbiggermipmapthan(32)

    except Exception as e :
        print("%s %s" % (str(e), filename))
        return None, None, None

    # uncomment this to reencode dds files with brotli :
    # (if they were encoded originally)
    #
    #if reencodeneeded is True :
    #    filedatal=len(filedata)
    #    newdecsize = (filedatal).to_bytes(4, byteorder='little', signed=False)
    #    filedata = newdecsize + brotli.compress(filedata)

    return filedata, None, None


























