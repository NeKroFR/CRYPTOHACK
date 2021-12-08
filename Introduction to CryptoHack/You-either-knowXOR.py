msg =  [i for i in bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")]
#Find the key:
findkey = list("crypto{")
key = ''
for i in range(len(findkey)):
    key += chr(msg[i]^ord(findkey[i]))
key += 'y'
print("Key:",key)

#Decrypt the code:
flag=''
key = [ord(i) for i  in key]

while len(key) < len(msg):
    key += key
print("flag:",end=' ')
for i in range (len(msg)):
    print(chr(msg[i]^key[i]), end ='')
