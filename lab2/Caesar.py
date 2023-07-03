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

def caesar_en(str1, k, b):
    result = ""
    for c in str1:
        p = str(chr((k * (ord(c) - 97) + b) % 26 + 97))
        result = result + p
    return result

def caesar_de(str1, k, b):
    result = ""
    for c in str1:
        p = str(chr((ex_gcd(k, 26)[1] * ((ord(c) - 97) + 26 - b)) % 26 + 97))
        result = result + p
    return result

# -*- coding: utf-8 -*-

from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput
from werkzeug.datastructures import ImmutableMultiDict



def main():
    # do something...
    while True:
        s = input().split()
        [k, b] = [int(s[0]), int(s[1])]
        p = input()
        mode = int(input())
        if ex_gcd(k, 26)[0] == 1:
            if mode == 1:
                print(caesar_en(p, k, b).strip().replace('\r', '').replace('\n', ''))
            elif mode == 0:
                print(caesar_de(p, k, b).strip().replace('\r', '').replace('\n', ''))
        else:
            print("invalid key")


if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
         'main',
         'ex_gcd',
         'Caesar_en',
         'Caesar_de',
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