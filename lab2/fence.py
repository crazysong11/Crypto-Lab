# -*- coding: utf-8 -*-

from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput
from werkzeug.datastructures import ImmutableMultiDict



def main():
    # do something...
    while True:
        k = int(input())
        s = input().strip().replace("\r\n", "")
        mode = int(input())
        l = [

        ]
        ans = ""

        if mode == 1:
            while len(s) % k != 0:
                s = s + "0"
            j = 0
            for i in range(k):
                l.append([])
            for i in range(len(s)):
                if j == k:
                    j = 0
                l[j].append(s[i])
                j += 1
            for i in range(k):
                ans = ans + "".join(l[i])
            ANS = ans.replace("0", "")
            print(ANS)

        else:
            row_len = len(s) // k if len(s) % k == 0 else len(s) // k + 1
            for i in range(k):
                l.append([])
                for j in range(row_len):
                    l[i].append("0")
            empty = k * row_len - len(s)
            for i in range(empty):
                l[k - 1 - i][row_len - 1] = "*"
            n = 0
            for i in range(k):
                for j in range(row_len):
                    if l[i][j] == "*":
                        break
                    l[i][j] = s[n]
                    n += 1
                    if j == row_len:
                        break
            for j in range(row_len):
                for i in range(k):
                    ans = ans + l[i][j]
            ANS = ans.strip().replace("*", "")
            print(ANS)

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