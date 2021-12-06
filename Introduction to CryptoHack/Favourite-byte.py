text = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
flag_ord =  [i for i in bytes.fromhex(text)]

flag = [0 for i in range(len(flag_ord))]
o = 1
possibleflag=''
for o in range (256):
    for i in range (len(flag_ord)):
        flag[i] = flag_ord[i] ^ o
    for C in flag:
        possibleflag += chr(C)
    if "crypto" in possibleflag:
        print(possibleflag)
        break
    else:
        possibleflag=''
    
