# MD5算法实现
import math
# 初始化参数
T = [int(pow(2, 32) * abs(math.sin(i+1))) for i in range(64)]
A, B, C, D = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476

# 定义辅助函数
def F(x, y, z):
    return (x & y) | (~x & z)

def G(x, y, z):
    return (x & z) | (y & ~z)

def H(x, y, z):
    return x ^ y ^ z

def I(x, y, z):
    return y ^ (x | ~z)

# 定义循环左移函数
def rotate_left(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xffffffff

# 定义填充函数
def padding(msg):
    length_b = len(msg) * 8
    msg += b'\x80'
    while len(msg) % 64 != 56:
        msg += b'\x00'
    msg += length_b.to_bytes(8, byteorder='little')
    return msg

# 分块函数
def chunks(msg):
    return [msg[i:i+64] for i in range(0, len(msg), 64)]

#掩码
def mask(a):
    return a & 0xffffffff

#小端十六进制
def toHex(x):
    x = hex(x)[2:].zfill(8)
    return x[6:8] + x[4:6] + x[2:4] + x[0:2]

# 主循环
def md5(msg):
    global A, B, C, D
    msg = padding(msg)
    blocks = chunks(msg)
    for block in blocks:
        a, b, c, d = A, B, C, D
        X = [int.from_bytes(block[i:i+4], byteorder='little') for i in range(0, 64, 4)]
        # 第一轮
        a = mask(b + rotate_left((a + F(b, c, d) + X[0] + T[0]) & 0xffffffff, 7))
        d = mask(a + rotate_left((d + F(a, b, c) + X[1] + T[1]) & 0xffffffff, 12))
        c = mask(d + rotate_left((c + F(d, a, b) + X[2] + T[2]) & 0xffffffff, 17))
        b = mask(c + rotate_left((b + F(c, d, a) + X[3] + T[3]) & 0xffffffff, 22))
        a = mask(b + rotate_left((a + F(b, c, d) + X[4] + T[4]) & 0xffffffff, 7))
        d = mask(a + rotate_left((d + F(a, b, c) + X[5] + T[5]) & 0xffffffff, 12))
        c = mask(d + rotate_left((c + F(d, a, b) + X[6] + T[6]) & 0xffffffff, 17))
        b = mask(c + rotate_left((b + F(c, d, a) + X[7] + T[7]) & 0xffffffff, 22))
        a = mask(b + rotate_left((a + F(b, c, d) + X[8] + T[8]) & 0xffffffff, 7))
        d = mask(a + rotate_left((d + F(a, b, c) + X[9] + T[9]) & 0xffffffff, 12))
        c = mask(d + rotate_left((c + F(d, a, b) + X[10] + T[10]) & 0xffffffff, 17))
        b = mask(c + rotate_left((b + F(c, d, a) + X[11] + T[11]) & 0xffffffff, 22))
        a = mask(b + rotate_left((a + F(b, c, d) + X[12] + T[12]) & 0xffffffff, 7))
        d = mask(a + rotate_left((d + F(a, b, c) + X[13] + T[13]) & 0xffffffff, 12))
        c = mask(d + rotate_left((c + F(d, a, b) + X[14] + T[14]) & 0xffffffff, 17))
        b = mask(c + rotate_left((b + F(c, d, a) + X[15] + T[15]) & 0xffffffff, 22))
        # 第二轮
        a = mask(b + rotate_left((a + G(b, c, d) + X[1] + T[16]) & 0xffffffff, 5))
        d = mask(a + rotate_left((d + G(a, b, c) + X[6] + T[17]) & 0xffffffff, 9))
        c = mask(d + rotate_left((c + G(d, a, b) + X[11] + T[18]) & 0xffffffff, 14))
        b = mask(c + rotate_left((b + G(c, d, a) + X[0] + T[19]) & 0xffffffff, 20))
        a = mask(b + rotate_left((a + G(b, c, d) + X[5] + T[20]) & 0xffffffff, 5))
        d = mask(a + rotate_left((d + G(a, b, c) + X[10] + T[21]) & 0xffffffff, 9))
        c = mask(d + rotate_left((c + G(d, a, b) + X[15] + T[22]) & 0xffffffff, 14))
        b = mask(c + rotate_left((b + G(c, d, a) + X[4] + T[23]) & 0xffffffff, 20))
        a = mask(b + rotate_left((a + G(b, c, d) + X[9] + T[24]) & 0xffffffff, 5))
        d = mask(a + rotate_left((d + G(a, b, c) + X[14] + T[25]) & 0xffffffff, 9))
        c = mask(d + rotate_left((c + G(d, a, b) + X[3] + T[26]) & 0xffffffff, 14))
        b = mask(c + rotate_left((b + G(c, d, a) + X[8] + T[27]) & 0xffffffff, 20))
        a = mask(b + rotate_left((a + G(b, c, d) + X[13] + T[28]) & 0xffffffff, 5))
        d = mask(a + rotate_left((d + G(a, b, c) + X[2] + T[29]) & 0xffffffff, 9))
        c = mask(d + rotate_left((c + G(d, a, b) + X[7] + T[30]) & 0xffffffff, 14))
        b = mask(c + rotate_left((b + G(c, d, a) + X[12] + T[31]) & 0xffffffff, 20))
        # 第三轮
        a = mask(b + rotate_left((a + H(b, c, d) + X[5] + T[32]) & 0xffffffff, 4))
        d = mask(a + rotate_left((d + H(a, b, c) + X[8] + T[33]) & 0xffffffff, 11))
        c = mask(d + rotate_left((c + H(d, a, b) + X[11] + T[34]) & 0xffffffff, 16))
        b = mask(c + rotate_left((b + H(c, d, a) + X[14] + T[35]) & 0xffffffff, 23))
        a = mask(b + rotate_left((a + H(b, c, d) + X[1] + T[36]) & 0xffffffff, 4))
        d = mask(a + rotate_left((d + H(a, b, c) + X[4] + T[37]) & 0xffffffff, 11))
        c = mask(d + rotate_left((c + H(d, a, b) + X[7] + T[38]) & 0xffffffff, 16))
        b = mask(c + rotate_left((b + H(c, d, a) + X[10] + T[39]) & 0xffffffff, 23))
        a = mask(b + rotate_left((a + H(b, c, d) + X[13] + T[40]) & 0xffffffff, 4))
        d = mask(a + rotate_left((d + H(a, b, c) + X[0] + T[41]) & 0xffffffff, 11))
        c = mask(d + rotate_left((c + H(d, a, b) + X[3] + T[42]) & 0xffffffff, 16))
        b = mask(c + rotate_left((b + H(c, d, a) + X[6] + T[43]) & 0xffffffff, 23))
        a = mask(b + rotate_left((a + H(b, c, d) + X[9] + T[44]) & 0xffffffff, 4))
        d = mask(a + rotate_left((d + H(a, b, c) + X[12] + T[45]) & 0xffffffff, 11))
        c = mask(d + rotate_left((c + H(d, a, b) + X[15] + T[46]) & 0xffffffff, 16))
        b = mask(c + rotate_left((b + H(c, d, a) + X[2] + T[47]) & 0xffffffff, 23))
        # 第四轮
        a = mask(b + rotate_left((a + I(b, c, d) + X[0] + T[48]) & 0xffffffff, 6))
        d = mask(a + rotate_left((d + I(a, b, c) + X[7] + T[49]) & 0xffffffff, 10))
        c = mask(d + rotate_left((c + I(d, a, b) + X[14] + T[50]) & 0xffffffff, 15))
        b = mask(c + rotate_left((b + I(c, d, a) + X[5] + T[51]) & 0xffffffff, 21))
        a = mask(b + rotate_left((a + I(b, c, d) + X[12] + T[52]) & 0xffffffff, 6))
        d = mask(a + rotate_left((d + I(a, b, c) + X[3] + T[53]) & 0xffffffff, 10))
        c = mask(d + rotate_left((c + I(d, a, b) + X[10] + T[54]) & 0xffffffff, 15))
        b = mask(c + rotate_left((b + I(c, d, a) + X[1] + T[55]) & 0xffffffff, 21))
        a = mask(b + rotate_left((a + I(b, c, d) + X[8] + T[56]) & 0xffffffff, 6))
        d = mask(a + rotate_left((d + I(a, b, c) + X[15] + T[57]) & 0xffffffff, 10))
        c = mask(d + rotate_left((c + I(d, a, b) + X[6] + T[58]) & 0xffffffff, 15))
        b = mask(c + rotate_left((b + I(c, d, a) + X[13] + T[59]) & 0xffffffff, 21))
        a = mask(b + rotate_left((a + I(b, c, d) + X[4] + T[60]) & 0xffffffff, 6))
        d = mask(a + rotate_left((d + I(a, b, c) + X[11] + T[61]) & 0xffffffff, 10))
        c = mask(d + rotate_left((c + I(d, a, b) + X[2] + T[62]) & 0xffffffff, 15))
        b = mask(c + rotate_left((b + I(c, d, a) + X[9] + T[63]) & 0xffffffff, 21))
        A, B, C, D = (a + A) & 0xffffffff, (b + B) & 0xffffffff, (c + C) & 0xffffffff, (d + D) & 0xffffffff

    # 拼接4个字节得到MD5值
    md5_value = toHex(A) + toHex(B) + toHex(C) + toHex(D)
    return md5_value

# 测试代码
msg = input().encode('utf-8')
md5_value = md5(msg)
print(md5_value)