def SendCommand(socket, cmd, encryptType):

    cmd += ':' + str(encryptType) + ':'
    socket.sendall(cmd.encode('utf-8'))
    return 0

def outputRecieved(socket):
    raw = bytearray()
    Clog = ''
    while not Clog:
        recieverawdata = socket.recv(8192)
        if not recieverawdata:
            raise ConnectionError()
        raw = raw + recieverawdata
        if b'\0' in recieverawdata:
            Clog = raw.rstrip(b'\0')
    Clog = Clog.decode('utf-8')
    return Clog

def getFileMethod(socket):
    try:
        get_file_name = socket.recv(8192).rstrip(b'\0').decode('utf-8')
        raw = socket.recv(8192)

        return raw, get_file_name
    except:
        raise ConnectionError()

def sendFile(sock, file, get_file_name):
    get_file_name = get_file_name + '\0'
    try:
        print('File Sending...... : ')
        sock.sendall(get_file_name.encode('utf-8'))
        print('Data Sending...... : ')
        sock.sendfile(file)
    except ( ConnectionError, BrokenPipeError ):
        raise ConnectionError()


