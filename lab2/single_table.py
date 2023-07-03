

# -*- coding: utf-8 -*-

from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput
from werkzeug.datastructures import ImmutableMultiDict



def main():
    # do something...
    while True:
        t1 = input()
        t2 = input()
        s = input()
        mode = int(input())
        ans = ""

        # 加密模式
        if mode == 1:
            # 创建加密字典
            en_dict = {}
            for i in range(len(t1)):
                en_dict[t1[i]] = t2[i]
            for c in s:
                ans = ans + en_dict[c]

        # 解密模式
        elif mode == 0:
            # 创建解密字典
            de_dict = {}
            for i in range(len(t1)):
                de_dict[t2[i]] = t1[i]
            for c in s:
                ans = ans + de_dict[c]
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