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

def gf_divmod(a, b):
    if b == 0:
        raise ZeroDivisionError
    ans = 0
    digit_a = a.bit_length()
    digit_b = b.bit_length()
    if digit_a == digit_b:
        return 1, gf_add_sub(a, b)
    while digit_a >= digit_b:
        rec = digit_a - digit_b
        a = a ^ (b << rec)
        ans = ans | (1 << rec)
        digit_a = a.bit_length()
    return ans, a

def gf_ex_gcd(a, b, poly):
    x1, y1, x2, y2 = 1, 0, 0, 1
    while b:
        q, r = gf_divmod(a, b)
        a, b = b, r
        x1, x2 = x2, x1 ^ gf_mult(q, x2, poly)
        y1, y2 = y2, y1 ^ gf_mult(q, y2, poly)
    return a, x1, y1




# -*- coding: utf-8 -*-

from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph import GlobbingFilter
from werkzeug.datastructures import ImmutableMultiDict


def main():
    # do something...
    str = input().split()
    a = int(str[0], 16)
    b = int(str[1], 16)
    [g, x, y] = gf_ex_gcd(a, b, 0x11b)
    print(hex(x)[2:].zfill(2) + " " + hex(y)[2:].zfill(2) + " " + hex(g)[2:].zfill(2))

if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
         'main',
         'gf_mult',
         'gf_divmod',
         'gf_ex_gcd',
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