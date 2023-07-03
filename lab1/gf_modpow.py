def gf_mult(a, b, poly):
    ans = 0
    digit_1 = poly.bit_length() - 1
    while b:
        if not k % 2 == 0:
            ans = ans ^ a
        a, b = a << 1, b >> 1
        if a >> digit_1:
            a = a ^ poly
    return ans

def gf_modpow(a, k, poly):
    ans = 1
    while k:
        if not k % 2 == 0:
            ans = gf_mult(ans, a, 0x11b)
        k = k // 2
        a = gf_mult(a, a, 0x11b)
    return ans


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
    k = int(str[1])
    print(hex(gf_modpow(a, k, 0x11b))[2:])

if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
         'main',
         'gf_mult',
         'gf_modpow',
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