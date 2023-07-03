while True:
    MIX_C = [[0x2, 0x3, 0x1, 0x1], [0x1, 0x2, 0x3, 0x1], [0x1, 0x1, 0x2, 0x3], [0x3, 0x1, 0x1, 0x2]]
    MIX_C_inv = [[0xe, 0xb, 0xd, 0x9], [0x9, 0xe, 0xb, 0xd], [0xd, 0x9, 0xe, 0xb], [0xb, 0xd, 0x9, 0xe]]
    RCon = [0x01000000, 0x02000000, 0x04000000, 0x08000000, 0x10000000, 0x20000000, 0x40000000, 0x80000000, 0x1B000000,
            0x36000000]

    S_BOX = [
        [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
        [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
        [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
        [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
        [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
        [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
        [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
        [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
        [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
        [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
        [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
        [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
        [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
        [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
        [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
        [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
    ]

    S_BOX_inv = [
        [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
        [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
        [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
        [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
        [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
        [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
        [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
        [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
        [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
        [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
        [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
        [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
        [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
        [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
        [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
        [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]
    ]


    # -------------------------产生状态矩阵-------------------------------
    def state_gen(s):
        s = s[2:]
        state = [
            [],
            [],
            [],
            []
        ]
        i = 0
        while i < 32:
            state[(i // 2) % 4].append(s[i:i + 2])
            i += 2
        return state


    # ---------------------------字节替换---------------------------------

    # 字节替换
    def SubBytes(state):
        for i in range(4):
            for j in range(4):
                string = state[i][j]
                row = int(string[0], 16)
                line = int(string[1], 16)
                state[i][j] = hex(S_BOX[row][line])[2:].zfill(2)
        return state


    # 逆字节替换
    def SubBytes_inv(state):
        for i in range(4):
            for j in range(4):
                string = state[i][j]
                row = int(string[0], 16)
                line = int(string[1], 16)
                state[i][j] = hex(S_BOX_inv[row][line])[2:].zfill(2)
        return state


    # ---------------------------行移位-----------------------------------

    # 循环左移函数
    def list_move_left(A, a):
        for i in range(a):
            A.append(A[0])
            A.remove(A[0])
        return A


    # 循环右移函数
    def list_move_right(A, a):
        for i in range(a):
            A.insert(0, A.pop())
        return A


    # 行移位
    def left_shift(state):
        for i in range(4):
            list_move_left(state[i], i)
        return state


    # 逆行移位
    def right_shift(state):
        for i in range(4):
            list_move_right(state[i], i)
        return state


    # ---------------------------列混合-----------------------------

    # 有限域乘法
    def gf_mult(a, b, poly):
        ans = 0
        digit_1 = poly.bit_length() - 1
        while b:
            if b & 1:
                ans = ans ^ a
            a, b = a << 1, b >> 1
            if a >> digit_1:
                a = a ^ poly
        return ans


    # 矩阵乘法
    def matrix_mult(M, N):
        c = []
        for i in range(len(M)):
            temp = []
            for j in range(len(N[0])):
                s = 0
                for k in range(len(M[0])):
                    s ^= gf_mult(M[i][k], int(N[k][j], 16), 0x11b)
                temp.append(hex(s)[2:].zfill(2))
            c.append(temp)
        return c


    # 列混合
    def MixColumn(state):
        return matrix_mult(MIX_C, state)


    # 逆列混合
    def MixColumn_inv(state):
        return matrix_mult(MIX_C_inv, state)


    # --------------------------轮密钥加-----------------------------

    # 取出数据字符串
    def string_gen(state):
        ans = "0x"
        for i in range(4):
            for j in range(4):
                ans = ans + state[j][i].zfill(2)
        return ans


    # 轮密钥加
    def RoundKeyAdd(state, key):
        a = int(string_gen(state), 16)
        K = int(key, 16)
        return a ^ K


    # -------------------------密钥拓展------------------------------

    # 密钥扩展
    def key_extend(key):

        # T函数（参数是int）
        def T(key):
            key = hex(key)[2:].zfill(8)
            # 转列表
            l = []
            l.append(key[0:2])
            l.append(key[2:4])
            l.append(key[4:6])
            l.append(key[6:8])
            # 字移位
            l = list_move_left(l, 1)
            # S盒替换
            for i in range(4):
                row = int(l[i][0], 16)
                line = int(l[i][1], 16)
                l[i] = hex(S_BOX[row][line])[2:].zfill(2)
            # Rcon常量异或
            ans = "0x" + "".join(l)
            return int(ans, 16) ^ RCon[round]

        # 密钥扩展算法
        w = []
        key = key[2:]
        w.append(int(key[0:8], 16))
        w.append(int(key[8:16], 16))
        w.append(int(key[16:24], 16))
        w.append(int(key[24:], 16))
        round = -1
        for i in range(4, 44):
            if i % 4 != 0:
                w.append(w[i - 4] ^ w[i - 1])
            else:
                round += 1
                w.append(w[i - 4] ^ T(w[i - 1]))
        i = 0
        ans = []
        while True:
            ans.append(
                "0x" + hex(w[i])[2:].zfill(8) + hex(w[i + 1])[2:].zfill(8) + hex(w[i + 2])[2:].zfill(8) + hex(w[i + 3])[
                                                                                                          2:].zfill(8))
            i += 4
            if i > 43:
                break
        return ans


    # ------------------------AES总体算法----------------------------
    def AES(s, k, mode):
        # 产生状态矩阵
        state = state_gen(s)
        # 密钥扩展，判断运行模式
        key = key_extend(k)
        if mode == 1:
            # 初始轮密钥加
            state = state_gen("0x" + hex(RoundKeyAdd(state, key[0]))[2:].zfill(32))
            # 10轮轮函数
            for cnt in range(10):
                state = SubBytes(state)
                left_shift(state)
                if cnt < 9:
                    state = MixColumn(state)
                state = state_gen("0x" + hex(RoundKeyAdd(state, key[cnt + 1]))[2:].zfill(32))
        else:
            # 初始轮密钥加
            key = key[::-1]
            state = state_gen("0x" + hex(RoundKeyAdd(state, key[0]))[2:].zfill(32))
            # 10轮轮函数
            for cnt in range(10):
                right_shift(state)
                state = SubBytes_inv(state)
                state = state_gen("0x" + hex(RoundKeyAdd(state, key[cnt + 1]))[2:].zfill(32))
                if cnt < 9:
                    state = MixColumn_inv(state)
        # 还原密文
        return string_gen(state)


    # ---------------------------main-------------------------------
    n = int(input())
    s = input().strip().replace("\r\n", "")
    k = input().strip().replace("\r\n", "")
    mode = int(input())
    ans = s
    for i in range(n):
        ans = AES(ans, k, mode)
    print(ans)