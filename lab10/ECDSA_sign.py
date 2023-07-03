import gmpy2

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

# 除法
def div(p, a, b, B, k):
    k_inv = ex_gcd(k, p)[1]
    ans = mult(p, a, b, B, k_inv)
    return ans[0], p - ans[1]

# 签名
def sign():
    global p,a,b,k,G,n,H,d
    P = mult(p, a, b, G, k)
    print(P)
    r = P[0] % 13
    print(r)
    s = (int(gmpy2.invert(k, n)) * (H + d * r)) % n
    print(s)
    print([r, s])
    print("接下来是验证")
    w = int(gmpy2.invert(s, n))
    print(w)
    u1 = H * w
    print(u1)
    u2 = r * w
    print(u2)
    X = add(p, a, b, mult(p, a, b, G, u1), mult(p, a, b, Q, u2))
    print(X)
    v = X[0] % n
    print(v)


p = 11
a = 1
b = 6
k = 6
G = [5,9]
n = 13
H = 20220529
d = 5
Q = [8,3]

sign()