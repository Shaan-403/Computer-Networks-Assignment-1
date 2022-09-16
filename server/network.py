import socket

def createListenSocket(host, port):
    var_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    var_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    var_sock.bind((host, port))
    var_sock.listen(100)
    return var_sock


def receivemsg(var_sock):

    data = bytearray()
    msg = ''
    while not msg:
        receiverawdata = var_sock.recv(8192)
        if not receiverawdata:
            raise ConnectionError()
        data = data + receiverawdata
        if b':' in receiverawdata:
            msg = data.rstrip(b':')
    msg = msg.decode('utf-8')

    encryptionType = msg[-1]
    msg = msg[:-2]

    return msg, encryptionType


def handleClientMethod(var_sock, address):
    try:
        msg, encryptionType = receivemsg(var_sock)
        return msg, encryptionType
    except ( ConnectionError, BrokenPipeError ):
        return 'Error', 0
    
def messageSent(var_sock, msg):
    msg = str(msg) +'\0'
    try:
        var_sock.sendall(msg.encode('utf-8'))
        print("Outgoing Messages")
        return 0
    except ( ConnectionError, BrokenPipeError ):
        print('Connection Error')
    finally:
        print('Connection Closed')
        var_sock.close()

def sendFileMethod(var_sock, file, fN):
    fN = fN + '\0'
    try:
        print('FileName Sending... ')
        var_sock.sendall(fN.encode('utf-8'))
        print('Outgoing Data... ')
        var_sock.sendfile(file)
    except ( ConnectionError, BrokenPipeError ):
        print('Error in Sending file')

def receiveFileMethod(var_sock):
    try:
        print('File Name Recieved')
        fN = var_sock.recv(8192).rstrip(b'\0').decode('utf-8')
        print('File Data Recieved')
        data = var_sock.recv(8192)

        return data, fN
    except ( ConnectionError ):
        print('Connection Error')
