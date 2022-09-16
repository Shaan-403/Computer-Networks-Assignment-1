import op_file, crypt_file, network
from socket import *

HOST = 'localhost'
PORT = 8080

if __name__ == '__main__':

    socketlist = network.createListenSocket(HOST, PORT)
    socketaddress = socketlist.getsockname()
    print('Listening on {}'.format(socketaddress))

    while True:

        Socket_client, socketaddress = socketlist.accept()
        print('Connection from {}'.format(socketaddress))

        msg, encryptType = network.handleClientMethod(Socket_client, socketaddress)

        if(msg == 'Error'):
            print('Connection Closed')
            continue

        decryptcmd = crypt_file.textDecryptionMethod(msg, encryptType)
        print(decryptcmd)
        if( decryptcmd.startswith('dwd ') ):

            try:
                file, fileName = op_file.handleCmd(decryptcmd)
        
                encryptedName = crypt_file.textEncryptionMethod(fileName, encryptType)

                network.sendFileMethod(Socket_client, file, encryptedName)
                network.messageSent(Socket_client, crypt_file.textEncryptionMethod('OK', encryptType))
            except ( ValueError ):
                network.messageSent(Socket_client, crypt_file.textEncryptionMethod('NOT OK', encryptType))
            
        elif(decryptcmd.startswith('upd ')):

            try:
                data, fileName = network.receiveFileMethod(Socket_client)

                decryptedName = crypt_file.textDecryptionMethod(fileName, encryptType)

                op_file.writeFileMethod(data, decryptedName)
                network.messageSent(Socket_client, crypt_file.textEncryptionMethod('OK', encryptType))
            except:
                network.messageSent(Socket_client, crypt_file.textEncryptionMethod('NOT OK', encryptType))

        else:
            output = op_file.handleCmd(decryptcmd)
            print(output)
            encryptedMessage = crypt_file.textEncryptionMethod(output, encryptType)
            network.messageSent(Socket_client, encryptedMessage)