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
    elif A[0] == B[0] and A[1] == -B[1]:
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
    B[1] = -B[1]
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

#---------------------------------main-------------------------------
while True:
    p = int(input())
    a = int(input())
    b = int(input())
    G = input().split()
    op = int(input())
    G[0] = int(G[0])
    G[1] = int(G[1])
    if op == 1:
        Pm = input().split()
        k = int(input())
        Pb = input().split()
        Pm[0] = int(Pm[0])
        Pm[1] = int(Pm[1])
        Pb[0] = int(Pb[0])
        Pb[1] = int(Pb[1])
        C1 = mult(p, a, b, G, k)
        C2 = add(p, a, b, Pm, mult(p, a, b, Pb, k))
        print(C1[0], end='')
        print(" ", end='')
        print(C1[1])
        print(C2[0], end='')
        print(" ", end='')
        print(C2[1])
    else:
        C1 = input().split()
        C2 = input().split()
        n = int(input())
        C1[0] = int(C1[0])
        C1[1] = int(C1[1])
        C2[0] = int(C2[0])
        C2[1] = int(C2[1])
        m = sub(p, a, b, C2, mult(p, a, b, C1, n))
        print(m[0], end='')
        print(" ", end='')
        print(m[1])