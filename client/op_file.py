import os

def writeFileMethod(data, name):
    file = open(name, 'wb')
    file.write(data)
    file.close()
    return 0

def readFileMethod(cmd):
    fP = cmd[4:]

    if os.path.isfile(fP):
        get_file_name = os.path.basename(fP)
        file = open(fP, 'rb')
        return file, get_file_name
    else:
        raise Exception('enter a valid file path')