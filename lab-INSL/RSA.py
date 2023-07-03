import random
import math


# Miller-Rabin
def MR(n):
    if n % 2 == 0 and n > 2:
        return False
    elif n == 2:
        return True
    else:
        k = -1
        while True:
            k += 1
            q = (n - 1) // int(pow(2, k))
            if q % 2 != 0:
                break

        for j in range(10):
            flag = 0
            x = 0
            a = random.randint(1, n - 1)
            if int(pow(a, q, n)) != 1:
                x = 1
            for i in range(k):
                if int(pow(a, q * pow(2, i), n)) == n - 1:
                    flag = 1
            if flag == 0 and x == 1:
                return False
        return True


# 快速幂
def fastExpMod(b, e, m):
    mont = MontMul(2 ** 64, m)
    result = 1
    while e != 0:
        if e % 2 != 0:
            result = mont.ModMul(result, b)
            result %= m
        e >>= 1
        b = mont.ModMul(b, b)
        b %= m
    return result


# 蒙哥马利模乘器
class MontMul:
    def __init__(self, R, N):
        self.N = N
        self.R = R
        self.logR = int(math.log(R, 2))
        N_inv = MontMul.modinv(N, R)
        self.N_inv_neg = R - N_inv
        self.R2 = (R * R) % N

    # 扩展欧几里得
    @staticmethod
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = MontMul.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    # 逆元
    @staticmethod
    def modinv(a, m):
        g, x, y = MontMul.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    # REDC算法
    def REDC(self, T):
        N, R, logR, N_inv_neg = self.N, self.R, self.logR, self.N_inv_neg

        m = ((T & int('1' * logR, 2)) * N_inv_neg) & int('1' * logR, 2)  # m = (T%R * N_inv_neg)%R
        t = (T + m * N) >> logR  # t = int((T+m*N)/R)
        if t >= N:
            return t - N
        else:
            return t

    # 模乘
    def ModMul(self, a, b):
        if a >= self.N or b >= self.N:
            raise Exception('input integer must be smaller than the modulus N')

        # 转换为蒙哥马利表示法
        R2 = self.R2
        aR = self.REDC(a * R2)
        bR = self.REDC(b * R2)
        T = aR * bR
        # 蒙哥马利约减
        abR = self.REDC(T)
        # 转换回常规表示
        return self.REDC(abR)


# -----------main------------
p = int(input())
q = int(input())
e = int(input())
m = int(input())
op = int(input())

if (MR(p) == False or MR(q) == False):
    print("Mole ! Terminate !")
else:
    n = p * q
    if op == 1:
        c = fastExpMod(m, e, n)
    else:
        phi = (p - 1) * (q - 1)
        mon = MontMul(2 ** 64, n)
        d = mon.modinv(e, phi)
        c = fastExpMod(m, d, n)

    print(c)
