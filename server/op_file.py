import os
import subprocess


def handleCmd(command):

    if ( command.startswith('cd ') ):
        #checking if the path is a directory
        filepath = command[3:]

        if os.path.isdir(filepath):
            os.chdir(filepath)
            return 'OK'
        else:
            return 'Directory Specified is not valid\nNOT OK'

    elif (command == 'ls'):
        res = subprocess.run(command, capture_output=True).stdout.decode('utf-8')
        return res

    elif (command == 'cwd'):
        res = subprocess.run('pwd', capture_output=True).stdout.decode('utf-8')
        return res
    
    elif ( command.startswith('dwd ') ):
        #checking if the path is a file
        filepath = command[4:]
        
        if os.path.isfile(filepath):
            fN = os.path.basename(filepath)
            file = open(filepath, 'rb')
            return file, fN
        else:
            return 'NOK'
    
    return 'Command invalid'

def writeFileMethod(data, name):
    file = open(name, 'wb')
    file.write(data)
    file.close()
    print('Successful write File')
    return 0