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



# -*- coding: utf-8 -*-

from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput
from werkzeug.datastructures import ImmutableMultiDict



def main():
    # do something...
    p = int(input())
    a = int(input())
    b = int(input())
    A = input().split()
    B = input().split()
    k = int(input())
    A[0] = int(A[0])
    A[1] = int(A[1])
    B[0] = int(B[0])
    B[1] = int(B[1])

    ans = add(p, a, b, A, B)
    print(ans[0], end='')
    print(" ", end='')
    print(ans[1])

    ans = sub(p, a, b, A, B)
    print(ans[0], end='')
    print(" ", end='')
    print(ans[1])

    ans = mult(p, a, b, A, k)
    print(ans[0], end='')
    print(" ", end='')
    print(ans[1])

    ans = div(p, a, b, B, k)
    print(ans[0], end='')
    print(" ", end='')
    print(ans[1])


if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
        'main',
        'ex_gcd',
        'add',
        'sub',
        'mult',
        'div'
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