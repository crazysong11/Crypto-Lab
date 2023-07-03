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

#-----------------------------main-------------------------------
# -*- coding: utf-8 -*-

from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput
from werkzeug.datastructures import ImmutableMultiDict

def main():
    # do something...
    iv = 0x7380166f4914b2b9172442d7da8a0600a96f30bc163138aae38dee4db0fb0e4e

    m = input()
    m = m.encode('utf-8')

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

    print(hex(V[n])[2:].zfill(64))


if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
        'main',
        'padding',
        'move',
        'ff',
        'gg',
        'p0',
        'p1',
        'T',
        'extend',
        'CF'
    ])
    # 该段作用是关系图中不包括(exclude)哪些函数。(正则表达式规则)
    # config.trace_filter = GlobbingFilter(exclude=[
    #     'pycallgraph.*',
    #     '*.secret_function',
    #     'FileFinder.*',
    #     'ModuleLockManager.*',
    #     'SourceFilLoader.*'
    # ])
    graphviz = GraphvizOutput()
    graphviz.output_file = 'graph.png'
    with PyCallGraph(output=graphviz, config=config):
        main()