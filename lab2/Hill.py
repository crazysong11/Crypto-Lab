import copy

#矩阵乘法
def matrix_mult(M, N):
    c = []
    for i in range(0, len(M)):
        temp = []
        for j in range(0, len(N[0])):
            s = 0
            for k in range(0, len(M[0])):
                s += M[i][k] * N[k][j]
            temp.append(s)
        c.append(temp)
    return c

#逆矩阵
def submatrix(A,i,j):
    p=len(A)
    q=len(A[0])
    C=[[A[x][y] for y in range(q) if y!=j] for x in range(p) if x!=i]
    return C

def det(A):
    p=len(A)
    q=len(A[0])
    if(p==1 and q==1):
        return A[0][0]
    else:
        value=0
        for j in range(q):
            value+=((-1)**(j+2))*A[0][j]*det(submatrix(A,0,j))
        return value

def inverse_matrix(A):
    p = len(A)
    q = len(A[0])
    C = copy.deepcopy(A)
    d = det(A)
    for i in range(p):
        for j in range(q):
            C[i][j] = ((-1) ** (i + j + 2)) * det(submatrix(A, j, i))
            C[i][j] = (C[i][j] * ex_gcd(d, 26)[1]) % 26
    return C

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



# -*- coding: utf-8 -*-

from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput
from werkzeug.datastructures import ImmutableMultiDict



def main():
    # do something...
    # 正片开始
    n = int(input())
    k = []
    # 创建空列表
    for i in range(n):
        k.append([])
    # 导入矩阵
    for i in range(n):
        str = input().split()
        for j in range(n):
            k[i].append(int(str[j]))

    s = input().strip().replace("\r\n", "")
    mode = int(input())
    ans = ""
    l = []
    # 密钥矩阵k

    if mode == 1:
        # length是l中字符串的组数
        length = len(s) // n
        i = 0
        # 三个字符一组存入列表l
        while True:
            if i == len(s):
                break
            l.append(s[i:i + n])
            i = i + n

        i = 0
        a = []
        for i in range(length):
            temp = []
            Temp = []
            # 计算编号
            for j in range(n):
                temp.append(ord(l[i][j]) - ord('a'))
            Temp.append(temp)
            a = matrix_mult(Temp, k)
            # 转字符串
            for j in range(n):
                a[0][j] %= 26
                a[0][j] = chr(a[0][j] + ord('a'))
                ans = ans + a[0][j]
        print(ans)

    else:
        # length是l中字符串的组数
        length = len(s) // n
        i = 0
        # 三个字符一组存入列表l
        while True:
            if i == len(s):
                break
            l.append(s[i:i + n])
            i = i + n

        i = 0
        a = []
        k = inverse_matrix(k)
        for i in range(length):
            temp = []
            Temp = []
            # 计算编号
            for j in range(n):
                temp.append(ord(l[i][j]) - ord('a'))
            Temp.append(temp)
            a = matrix_mult(Temp, k)
            # 转字符串
            for j in range(n):
                a[0][j] %= 26
                a[0][j] = chr(a[0][j] + ord('a'))
                ans = ans + a[0][j]
        print(ans)


if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
         'main',
         'matrix_mult',
         'submatrix',
         'det',
         'inverse_matrix',
         'ex_gcd',
         'draw_chessboard',
         'draw_chessman',
         'draw_chessboard_with_chessman',
         'choose_save',
         'choose_turn',
         'choose_mode',
         'choose_button',
         'save_chess',
         'load_chess',
         'play_chess',
         'pop_window',
         'tip',
         'get_score',
         'max_score',
         'win',
         'key_control'
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