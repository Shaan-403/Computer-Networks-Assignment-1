def textEncrypt(text, encryptType = None ):
    lis = ['p', 'c', 't', 'q']
    l = len(lis)
    while (encryptType == None or (encryptType not in lis)):
        try :
            encryptType = input('Enter desired Encryption. input: \np for plain \nc for caesar \nt for transpose\nq to quit\n')
        except:
            print('Above method does not exist')
            continue
        if (encryptType not in lis):
            print('Input type Error.')
        else:
            break
    
    if (encryptType == 'p'):
        return text, 'p'

    elif (encryptType == 'q'):
        return None, 'q'

    elif (encryptType == 't'):
        return text[::-1], 't'

    elif (encryptType == 'c'):

        res = ""

        for i in range(len(text)):
            curr = text[i]

            if( curr.isupper() ):
                res += chr((ord(curr) + 2 - 65) % 26 + 65)
            elif( curr.isnumeric() ):
                res += str((int(curr) + 2)%10)
            elif( curr.islower() ):
                res += chr((ord(curr) + 2 - 97) % 26 + 97)
            else:
                res += curr
        
        return res, 'c'    
    


def DecryptText(text, encryptType):

    if(encryptType == 'p'):
        return text

    elif(encryptType == 't'):
        return text[::-1]

    elif(encryptType == 'c'):

        res = ''

        for i in range(len(text)):
            curr = text[i]

            if( curr.isupper() ):
                res += chr((ord(curr) + 24 - 65) % 26 + 65)
            elif( curr.islower() ):
                res += chr((ord(curr) + 24 - 97) % 26 + 97)
            elif( curr.isnumeric() ):
                res += str((int(curr) - 2)%10)
            else:
                res += curr

        return res

