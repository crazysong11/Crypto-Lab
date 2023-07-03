import gmpy2

def ex_gcd(a,b):
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

def CRT(a, m):
    M = m[0] * m[1] * m[2]
    #M是积
    M0 = m[1] * m[2]
    M1 = m[0] * m[2]
    M2 = m[0] * m[1]
    #t是M的逆元
    t0 = ex_gcd(M0, m[0])[1]
    t1 = ex_gcd(M1, m[1])[1]
    t2 = ex_gcd(M2, m[2])[1]

    x = a[0] * M0 * t0 + a[1] * M1 * t1 + a[2] * M2 * t2
    if x % M == 0:
        return M
    else:
        return x % M


# -*- coding: utf-8 -*-





# do something...
n = int(input())
e = int(input())
c = []
m = []
for i in range(n):
    c.append(int(input()))
    m.append(int(input()))
crt = CRT(c, m)
ans = gmpy2.iroot(crt, e)[0]
print(ans)