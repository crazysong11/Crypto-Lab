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

#f函数（直接加K）
def f(b, c, d, t):
    if t <= 19:
        return ((b&c) | (~b&d)) + 0x5A827999
    elif t <= 39:
        return (b ^ c ^ d) + 0x6ED9EBA1
    elif t <= 59:
        return ((b&c) | (b&d) | (c&d)) + 0x8F1BBCDC
    else:
        return (b ^ c ^ d) + 0xCA62C1D6

#sha1全过程
def sha1(m):

    # 填充
    m = padding(m)

    # 补0，为分组做准备
    m_bin = bin(m)[2:]
    while len(m_bin) % 512 != 0:
        m_bin = "0" + m_bin

    A = 0x67452301
    B = 0xefcdab89
    C = 0x98badcfe
    D = 0x10325476
    E = 0xc3d2e1f0

    cnt = 0
    while cnt != len(m_bin):

        s = m_bin[cnt:cnt + 512]
        M = []
        W = []

        # 分组装填
        i = 0
        while i < len(s):
            M.append(int(s[i:i + 32], 2))
            W.append(int(s[i:i + 32], 2))
            i += 32

        # 扩充子明文
        for i in range(16, 80):
            W.append(0)
        for i in range(16, 80):
            W[i] = W[i - 3] ^ W[i - 8] ^ W[i - 14] ^ W[i - 16]
            W[i] = move(W[i], 1)

        # 80轮迭代
        a = A
        b = B
        c = C
        d = D
        e = E
        for t in range(80):
            temp = (move(a, 5) + e + W[t] + f(b, c, d, t))  # f函数包含了K
            e = d
            d = c
            c = move(b, 30)
            b = a
            a = temp & 0xffffffff

        A = (A + a) & 0xffffffff
        B = (B + b) & 0xffffffff
        C = (C + c) & 0Xffffffff
        D = (D + d) & 0xffffffff
        E = (E + e) & 0xffffffff

        cnt += 512
        M.clear()
        W.clear()

    ans = hex(A)[2:].zfill(8) + hex(B)[2:].zfill(8) + hex(C)[2:].zfill(8) + hex(D)[2:].zfill(8) + hex(E)[2:].zfill(8)
    return ans

#HMAC
def hmac(k, m):
    ipad = 2839300502811373503439205293737708591701512762007800950576754188082255912250868771558043969023579549393183217027726457827853763419000450106303596260111926
    opad = 4837326782567525228081609018960540563639614335272549767649284913029028591242220870061852687966098491558756591973163594817824930269408174255183904739449948
    k_bitlen = len(k) * 4
    k = int(k, 16)

    #补位
    while k_bitlen < 512:
        k = k << 1
        k_bitlen += 1

    #求k异或ipad
    k_ipad = (k ^ ipad).to_bytes(64, byteorder='big')

    #拼接
    m = m.encode('utf-8')
    byte1 = k_ipad + m

    #求第一个hash并转字节
    H1 = int(sha1(byte1),16).to_bytes(20, byteorder='big')

    #求k异或opad
    k_opad = (k ^ opad).to_bytes(64, byteorder='big')

    #拼接
    byte2 = k_opad + H1

    #求第二个hash
    H2 = sha1(byte2)
    return H2

#--------------------------main--------------------------

# -*- coding: utf-8 -*-

from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput
from werkzeug.datastructures import ImmutableMultiDict

def main():
    # do something...
    k = input()
    m = input()
    ans = hmac(k, m)
    print(ans)


if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
        'main',
        'padding',
        'move',
        'f',
        'sha1',
        'hmac'
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