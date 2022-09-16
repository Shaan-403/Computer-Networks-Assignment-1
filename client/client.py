import socket
import crypt_file, op_file, network

HOST = 'localhost'
PORT = 8080

if __name__ == '__main__':

    while True:

        try : 

            var_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            var_sock.connect((HOST, PORT))
            print('\nConnected to {}:{}'.format(HOST, PORT))

            cmd = input("Enter the cmd to run, type q to terminate\n")

            if cmd == 'q':
                break

            encryptcmd, encryptType = crypt_file.textEncrypt(cmd)

            if encryptType == 'q':
                break

            network.SendCommand(var_sock, encryptcmd, encryptType)

            if (cmd.startswith('dwd ')):

                file, fN = network.getFileMethod(var_sock)
                decrypt_message = crypt_file.DecryptText(fN, encryptType)

                if ('NOK' in fN):
                    print('Requested file does not exist')
                    print('NOK')
                
                else:
                    op_file.writeFileMethod(file, decrypt_message)
                    received_mess = network.outputRecieved(var_sock)
                    print(crypt_file.DecryptText(received_mess, encryptType))

            elif( cmd.startswith('upd ')):
                try:
                    file, fN = op_file.readFileMethod(cmd)

                    encrypt_message = crypt_file.textEncrypt(fN, encryptType)[0]

                    network.sendFile(var_sock, file, encrypt_message)

                    received_mess = network.outputRecieved(var_sock)
                    print(crypt_file.DecryptText(received_mess, encryptType))
                except:
                    print('Unknown error while sending the file\nNOK')
            else:
                received_mess = network.outputRecieved(var_sock)
                print(crypt_file.DecryptText(received_mess, encryptType))
        
        except ConnectionError:
            print('Socket Error')
            break
        finally :
            var_sock.close()
            print('Connection Closed\n')