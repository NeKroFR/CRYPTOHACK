from base64 import b64encode

msg ='72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
decoded = bytes.fromhex(msg)
print(b64encode(decoded))

