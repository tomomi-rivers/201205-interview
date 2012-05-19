# -*- coding: utf-8 -*-
import sys, os

def makelower(line):
    """引数：文字列（要素：文字）
    戻り値：リスト(要素：文字）
    アルファベット以外を除去し、大文字は小文字に変換したリストを作成
    """
    alphalist = []
    for n in line:
        if n.isalpha() == False:
            continue
        else:
           alphalist.append(n)
    lowalpha = None
    alphastring = []
    for m in alphalist:
        if str(m).islower() == False:
            lowalpha = str(m).lower()
        else:
            lowalpha = m
        alphastring.append(lowalpha)
    return alphastring

def checkpangram(targetstring):
    """引数：リスト（要素：文字）
       アルファベットの書く文字が引数に存在するかチェック
       存在しない場合は出力対象とする
       すべて存在する場合は"None"を表示
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    nopresent_list = []
    for k in list(alphabet):
        if (k in targetstring) == False:
            nopresent_list.append(k)
    if len(nopresent_list) == 0:
        print('NONE')
    else:
        for l in nopresent_list[0:len(nopresent_list)-1]:
            print(l),
        print(nopresent_list[len(nopresent_list)-1])
    return

if len(sys.argv) != 2:
    #引数が存在しない場合
    print('please provide just one argument as a filepath')
else:
    param = sys.argv[1]
    if os.path.isfile(param) == False:
    #ファイルパスが不正の場合
        print('"' + param + '"' + ' is invalid filepath.')
    else:
        try:
            loweredline = []
            target_file = open(param)
            for line in target_file:
                loweredline = makelower(line)
                checkpangram(loweredline)
        except IOError:
            print('failed to open' + "'" + param + '"')
        else:
            target_file.close()
