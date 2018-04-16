import re

'''

restriction "\.arm$"

'''

precompile=re.compile(r'\n([\d]+)\r?\n(([\d.\-e]+[ \t]+)+\"Metadata.+\"\s+\"[^M].+\"\r?\n)+')
def execute(filename, backupfiledata, modifyggpk) :
   filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
   # filedatamod=re.sub(r'\n([\d]+)\r?\n(([\d.\-e]+[ \t]+)+\"Metadata.+\"\s+\"[^M].+\"\r?\n)+', r'\n0\n', filedata)
   filedatamod=precompile.sub(r'\n0\n', filedata)
   return filedatamod, encoding, bom