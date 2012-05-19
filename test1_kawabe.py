# -*- coding: utf-8 -*-
import os

def fizz_buzz(line):
    """引数：文字列
    スペース(' ')区切りで文字列を読み込み
    最初の数値の倍数は'F'で置換
    2番目の数値の倍数は'B'で置換
    公倍数は'FB'で置換
    3番めの数値までカウントアップして出力
    """
    splitedline = line.split(' ')
    firstnum = int(splitedline[0])
    secondnum = int(splitedline[1])
    lastnum = int(splitedline[2])

    results = []
    for i in range(1, lastnum + 1):
        if i % firstnum == 0 and i % secondnum == 0:
            results.append('FB')
        elif i % firstnum == 0:
            results.append('F')
        elif i % secondnum == 0:
            results.append('B')
        else:
            results.append(i)
    
    for j in results[0:len(results)-1]:
        print(j),
    print(results[len(results)-1])
    return

filename =  raw_input('file path is :')
if os.path.isfile(filename) == False:
    #ファイルパスが不正の場合
    print('"' + filename + '"' + ' is invalid filepath.')
else:
    try:
        target_file = open(filename)
        for line in target_file:
            fizz_buzz(line)
    except IOError:
        #ファイルオープン失敗時例外
        print('failed to open ' + '"' + filename + '"')
    else:
        target_file.close()
