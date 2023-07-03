# MD5算法实现
# 不允许调用任何库

# 初始化参数
T = [int(pow(2, 32) * abs(math.sin(i))) for i in range(64)]
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
    return (x << n) | (x >> (32 - n))

# 定义填充函数
def padding(msg):
    length_b = len(msg) * 8
    msg += b'\x80'
    while (len(msg) + 8) % 64 != 0:
        msg += b'\x00'
    msg += length_b.to_bytes(8, byteorder='little')
    return msg

# 分块函数
def chunks(msg):
    return [msg[i:i+64] for i in range(0, len(msg), 64)]

# 主循环
def md5(msg):
    global A, B, C, D
    msg = padding(msg)
    blocks = chunks(msg)
    for block in blocks:
        a, b, c, d = A, B, C, D
        X = [int.from_bytes(block[i:i+4], byteorder='little') for i in range(0, 64, 4)]
        # 第一轮
        a = b + rotate_left((a + F(b, c, d) + X[0] + T[0]), 7)
        d = a + rotate_left((d + F(a, b, c) + X[1] + T[1]), 12)
        c = d + rotate_left((c + F(d, a, b) + X[2] + T[2]), 17)
        b = c + rotate_left((b + F(c, d, a) + X[3] + T[3]), 22)
        # 第二轮
        a = b + rotate_left((a + G(b, c, d) + X[4] + T[4]), 7)
        d = a + rotate_left((d + G(a, b, c) + X[5] + T[5]), 12)
        c = d + rotate_left((c + G(d, a, b) + X[6] + T[6]), 17)
        b = c + rotate_left((b + G(c, d, a) + X[7] + T[7]), 22)
        # 第三轮
        a = b + rotate_left((a + H(b, c, d) + X[8] + T[8]), 7)
        d = a + rotate_left((d + H(a, b, c) + X[9] + T[9]), 12)
        c = d + rotate_left((c + H(d, a, b) + X[10] + T[10]), 17)
        b = c + rotate_left((b + H(c, d, a) + X[11] + T[11]), 22)
        # 第四轮
        a = b + rotate_left((a + I(b, c, d) + X[12] + T[12]), 7)
        d = a + rotate_left((d + I(a, b, c) + X[13] + T[13]), 12)
        c = d + rotate_left((c + I(d, a, b) + X[14] + T[14]), 17)
        b = c + rotate_left((b + I(c, d, a) + X[15] + T[15]), 22)
        A, B, C, D = (a & 0xFFFFFFFF), (b & 0xFFFFFFFF), (c & 0xFFFFFFFF), (d & 0xFFFFFFFF)

    # 拼接4个字节得到MD5值
    md5_value = '{:08x}{:08x}{:08x}{:08x}'.format(A, B, C, D)
    return md5_value

# 测试代码
msg = input().strip().replace('\r\n', '')
md5_value = md5(msg.encode('utf-8'))
print(md5_value)
