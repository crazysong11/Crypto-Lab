import hashlib
import math

def MGF(x, maskLen):
    x = int(x, 16)
    t = ""
    k = math.ceil(maskLen / hLen) - 1
    for i in range(k+1):
        t += hashlib.sha1(int.to_bytes((x<<32) + i, hLen + 4, byteorder='big')).hexdigest()
    mask = t[0:(2*maskLen)]
    return mask

# main输入部分
m = input().strip()
n = int(input())
emBits = int(input())
Mode = input().strip().replace('\r\n','')

sLen = 20
hLen = 20
emLen = math.ceil(emBits / 8)

if Mode == "Sign":
    # 签名方私钥d
    d = int(input())
    # 盐值salt，十六进制，没有0x
    salt = input().strip().replace('\r\n','')
    #M to M1
    mHash = hashlib.sha1(m.encode('utf-8')).hexdigest()
    m1 = int.to_bytes(0, 8, byteorder='big') + int.to_bytes(int(mHash, 16), 20, byteorder='big') + int.to_bytes(int(salt, 16), 20, byteorder='big')
    H = hashlib.sha1(m1).hexdigest()
    #DB to MaskedDB
    p2 = b""
    for i in range(emLen - sLen - hLen - 2):
        p2 += int.to_bytes(0, 1, byteorder='big')
    p2 += int.to_bytes(1, 1, byteorder='big')
    db = (int.from_bytes(p2, byteorder='big') << 160) + int(salt, 16)
    dbMask = MGF(H, emLen - hLen - 1)
    maskedDB = hex(db ^ int(dbMask, 16))[2:]
    #左8*emLen-emBits位设0
    maskedDB_bin = bin(int(maskedDB, 16))[2:]
    maskedDB_bin_list = list(maskedDB_bin)
    temp = 8*emLen - emBits
    for i in range(temp):
        maskedDB_bin_list[i] = '0'
    maskedDB_bin = ''.join(maskedDB_bin_list)
    maskedDB = hex(int(maskedDB_bin, 2))[2:]
    em = maskedDB + H + "bc"
    #签名
    em = int(em, 16)
    s = pow(em, d, n)
    S = hex(s)[2:]
    print(S)

else:
	# 签名方公钥
    e = int(input())
    # 签名s，十六进制，没有0x
    s = input().strip().replace('\r\n', '')
    em = pow(int(s, 16), e, n)
    mHash = hashlib.sha1(m.encode('utf-8')).hexdigest()
    if emLen < sLen + hLen + 2:
        print("False")
    else:
        if (em & 0xff) != 0xbc:
            print("False")
        else:
            maskedDB = em >> (8 * (hLen+1))
            H = (em >> 8) & 0xffffffffffffffffffffffffffffffffffffffff   #40个f
            p2 = b""
            for i in range(emLen - sLen - hLen - 2):
                p2 += int.to_bytes(0, 1, byteorder='big')
            p2 += int.to_bytes(1, 1, byteorder='big')
            #最左不是0这个先放下
            dbMask = MGF(hex(H), emLen - hLen - 1)
            db = int(dbMask, 16) ^ maskedDB
            if ((db >> 160) & 1) != int.from_bytes(p2, byteorder='big'):
                print("False")
            else:
                salt = db & 0xffffffffffffffffffffffffffffffffffffffff
                m1 = int.to_bytes(0, 8, byteorder='big') + int.to_bytes(int(mHash, 16), 20, byteorder='big') + int.to_bytes(salt, 20, byteorder='big')
                h1 = hashlib.sha1(m1).hexdigest()
                if int(h1, 16) == H:
                    print("True")
                else:
                    print("False")
