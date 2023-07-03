# -*- coding: utf-8 -*-

from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput
from werkzeug.datastructures import ImmutableMultiDict



def main():
    # do something...
    while True:
        k = input().strip().replace("\r\n", "")
        s = input().strip().replace("\r\n", "")
        mode = int(input())
        ans = ""

        for i in range(len(s)):
            ans = ans + chr(ord(s[i]) ^ ord(k[i % len(k)]))

        print(ans)


if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
         'main',
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