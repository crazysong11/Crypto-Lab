import sys


def initS(S):
    for i in range(256):
        S.append(i)

def initT(T, k):
    j = 0
    for i in range(256):
        j = j % len(k)
        T.append(k[j:j+2])
        j += 2

def SubS(S, T):
    j = 0
    for i in range(256):
        j = (j + S[i] + int(T[i],16)) % 256
        S[i],S[j] = S[j],S[i]

def keyGenerate(S, T, k):
    initS(S)
    initT(T, k)
    SubS(S, T)
    T.clear()


# -*- coding: utf-8 -*-

from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput
from werkzeug.datastructures import ImmutableMultiDict



def main():
    # do something...
    k = input().strip().replace('\r\n', '')[2:]
    S = []
    T = []
    key = []
    keyGenerate(S, T, k)
    i = 1
    j = 0
    final_ans = "0x"
    while True:
        s = sys.stdin.read(2)
        if s == "" or s == "\n" or s == "\r":
            break
        elif s == "0x":
            continue
        else:
            if i >= 256:
                i = i % 256
            # 生成密钥流
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            t = (S[i] + S[j]) % 256
            # 异或操作
            ans = hex(int(s, 16) ^ S[t])[2:].zfill(2)
            final_ans += ans
            i += 1
    print(final_ans)


if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
         'main',
         'initS',
         'initT',
         'SubS',
         'keyGenerate',
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