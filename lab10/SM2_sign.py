import sys
import math

#-----------------------------SM3-------------------------------
#填充
def padding(m):
    m_bitlen = len(m) * 8
    m = int.from_bytes(m, byteorder='big')
    m = (m << 1) + 1
    bitlen = m_bitlen + 1
    while (bitlen % 512) != 448:
        m = m << 1
        bitlen += 1
    m = (m << 64) + m_bitlen
    return m

#循环移位
def move(a, n):
    return ((a << n) | (a >> (32 - n))) & 0xffffffff

#常量T
def T(j):
    if j <= 15:
        return 0x79cc4519
    else:
        return 0x7a879d8a

#ff函数
def ff(x, y, z, j):
    if j <= 15:
        return x ^ y ^ z
    else:
        return (x&y) | (x&z) | (y&z)

#gg函数（说的就是我）
def gg(x, y, z, j):
    if j <= 15:
        return x ^ y ^ z
    else:
        return (x&y) | (~x&z)

#置换函数0
def p0(x):
    return x ^ move(x,9) ^ move(x,17)

#置换函数1
def p1(x):
    return x ^ move(x,15) ^ move(x,23)

#压缩函数CF
def CF(V, b):

    #生成W和W'
    # 初始化W
    W = []
    for i in range(68):
        W.append(0)
    # 分割成16个32位字
    b = bin(b)[2:].zfill(512)
    j = 0
    for i in range(16):
        W[i] = int(b[j:j+32], 2)
        j += 32
    # 生成16-67号W
    for i in range(16, 68):
        W[i] = p1(W[i - 16] ^ W[i - 9] ^ move(W[i - 3], 15)) ^ move(W[i - 13], 7) ^ W[i - 6]
    # 生成W'
    W1 = []
    for i in range(64):
        W1.append(W[i] ^ W[i + 4])

    V_bin = bin(V)[2:].zfill(256)
    A = int(V_bin[0:32], 2)
    B = int(V_bin[32:64], 2)
    C = int(V_bin[64:96], 2)
    D = int(V_bin[96:128], 2)
    E = int(V_bin[128:160], 2)
    F = int(V_bin[160:192], 2)
    G = int(V_bin[192:224], 2)
    H = int(V_bin[224:256], 2)

    for j in range(64):
        ss1 = move((move(A,12) + E + move(T(j),j%32)) & 0xffffffff, 7)
        ss2 = (ss1 ^ move(A,12)) & 0xffffffff
        tt1 = (ff(A, B, C, j) + D + ss2 + W1[j]) & 0xffffffff
        tt2 = (gg(E, F, G, j) + H + ss1 + W[j]) & 0xffffffff
        D = C
        C = move(B, 9)
        B = A
        A = tt1
        H = G
        G = move(F, 19)
        F = E
        E = p0(tt2)

    A = A & 0xffffffff
    B = B & 0xffffffff
    C = C & 0xffffffff
    D = D & 0xffffffff
    E = E & 0xffffffff
    F = F & 0xffffffff
    G = G & 0xffffffff
    H = H & 0xffffffff

    ABCDEFGH = (A << 224) + (B << 192) + (C << 160) + (D << 128) + (E << 96) + (F << 64) + (G << 32) + H
    V1 = ABCDEFGH ^ V
    return V1

def SM3(m):
    iv = 0x7380166f4914b2b9172442d7da8a0600a96f30bc163138aae38dee4db0fb0e4e

    # 填充
    m = padding(m)

    # 补0，为分组做准备
    m_bin = bin(m)[2:]
    while len(m_bin) % 512 != 0:
        m_bin = "0" + m_bin

    # 明文分组
    m_bitlen = len(m_bin)
    n = m_bitlen // 512  # 组数
    B = []
    i = 0
    while i < m_bitlen:
        B.append(int(m_bin[i:i + 512], 2))
        i += 512

    # 迭代
    V = []
    V.append(iv)
    for i in range(n):
        V.append(CF(V[i], B[i]))

    return hex(V[n])[2:].zfill(64)

#--------------------------椭圆曲线计算--------------------------
def ex_gcd(a, b):
    if a < 0 and b < 0:
        a = abs(a)
        b = abs(b)
        if b == 0:
            return a, 1, 0
        else:
            g, xtmp, ytmp = ex_gcd(b, a % b)
            x = ytmp
            y = xtmp - int(a / b) * ytmp
            x0 = x + b // g
            x1 = (x0 % (b // g) + (b // g)) % (b // g)
            y1 = (g - a * x1) // b
            return g, x1, y1
    elif a < 0 and b > 0:
        a = abs(a)
        if b == 0:
            return a, 1, 0
        else:
            g, xtmp, ytmp = ex_gcd(b, a % b)
            x = ytmp
            y = xtmp - int(a / b) * ytmp
            x0 = x + b // g
            x1 = (x0 % (b // g) + (b // g)) % (b // g)
            y1 = (g - a * x1) // b
            return g, -x1, y1
    elif a > 0 and b < 0:
        b = abs(b)
        if b == 0:
            return a, 1, 0
        else:
            g, xtmp, ytmp = ex_gcd(b, a % b)
            x = ytmp
            y = xtmp - int(a / b) * ytmp
            x0 = x + b // g
            x1 = (x0 % (b // g) + (b // g)) % (b // g)
            y1 = (g - a * x1) // b
            return g, x1, -y1
    else:
        if b == 0:
            return a, 1, 0
        else:
            g, xtmp, ytmp = ex_gcd(b, a % b)
            x = ytmp
            y = xtmp - int(a / b) * ytmp
            x0 = x + b // g
            x1 = (x0 % (b // g) + (b // g)) % (b // g)
            y1 = (g - a * x1) // b
            return g, x1, y1


# 加法
def add(p, a, b, A, B):
    if A == [0, 0]:
        return B
    elif B == [0, 0]:
        return A
    elif A[0] == B[0] and A[1] == p - B[1]:
        return [0, 0]
    elif A[0] == B[0] and A[1] == B[1]:
        lam = ((3 * A[0] ** 2 + a) * ex_gcd(2 * A[1], p)[1]) % p
    else:
        lam = ((B[1] - A[1]) * ex_gcd(B[0] - A[0], p)[1]) % p
    x = (lam ** 2 - A[0] - B[0]) % p
    y = (lam * (A[0] - x) - A[1]) % p
    return [x, y]


# 减法
def sub(p, a, b, A, B):
    B[1] = p - B[1]
    return add(p, a, b, A, B)

# 乘法
def mult(p, a, b, A, k):
    C = A
    k = k - 1
    while k:
        if k&1 == 1:
            C = add(p, a, b, C, A)
        A = add(p, a, b, A, A)
        k = k >> 1
    return C

def bytelen(a):
    return math.ceil(len(bin(a)[2:]) / 8)
#---------------------------------SM2----------------------------------
#输入
p = int(input())
a = int(input())
b = int(input())
G = list(map(int, input().split()))
n = int(input())
ida = input().strip().replace('\r\n', '')
Pa = list(map(int, input().split()))
m = input()
mode = input().strip().replace('\r\n', '')

xg = G[0]
yg = G[1]
xa = Pa[0]
ya = Pa[1]

#Za
entlen = len(ida.encode('utf-8')) * 8
ENTL = int.to_bytes(entlen, 2, byteorder='big')
a_bin = int.to_bytes(a, 32, byteorder='big')
b_bin = int.to_bytes(b, 32, byteorder='big')
xg_bin = int.to_bytes(xg, 32, byteorder='big')
yg_bin = int.to_bytes(yg, 32, byteorder='big')
xa_bin = int.to_bytes(xa, 32, byteorder='big')
ya_bin = int.to_bytes(ya, 32, byteorder='big')
Za = SM3(ENTL + ida.encode('utf-8') + a_bin + b_bin + xg_bin + yg_bin + xa_bin + ya_bin)
Za = int(Za, 16)
Za = int.to_bytes(Za, 32, 'big')

#数字签名
if mode == 'Sign':
    da = int(input())
    #A1
    M = Za + m.encode('utf-8')
    #A2
    e = SM3(M)
    e = int(e, 16)
    #A3
    k = int(input())
    #A4
    [x1, y1] = mult(p, a, b, G, k)
    #A5
    r = (e + x1) % n
    #A6
    s = ((ex_gcd(1+da, n)[1] % n) * ((k - r*da) % n)) % n
    print(r)
    print(s)

else:
    r = int(input())
    s = int(input())
    #B3
    M = Za + m.encode('utf-8')
    #B4
    e = SM3(M)
    e = int(e, 16)
    #B5
    t = (r + s) % n
    if t == 0:
        print("False")
        sys.exit(0)
    #B6
    [x1, y1] = add(p, a, b, mult(p,a,b,G,s), mult(p,a,b,Pa,t))
    #B7
    R = (e + x1) % n
    if R == r:
        print("True")
    else:
        print("False")