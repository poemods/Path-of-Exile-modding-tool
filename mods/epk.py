'''

restriction "\.epk$"

'''

def execute(filename, backupfiledata, modifyggpk):
    filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
    filedatamod=""
    return filedatamod, encoding, bom

