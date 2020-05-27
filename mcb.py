#! /usr/bin/env python3
#coding:utf-8
#usage
#py.exe mcb.pyw save <keyword> クリップボードをキーワードに紐づけて保存
#py.exe mcb.pyw <keyword> キーワードに紐つけられたテキストをクリップボードにコピー
#py.exe mcb.pyw list 全キーワードをクリップボードにコピー
import shelve, pyperclip, sys
mcb_shelf=shelve.open('mcb')#mcbという名前のバイナリーファイルを作って戻り値のシェルフオブジェクトを変数に代入
#クリップボードの内容を保存
if len(sys.argv)== 3 and sys.argv[1].lower()=='save':#
    mcb_shelf[sys.argv[2]]=pyperclip.paste()#sys.argv[2]というキーに対応した値としてpyperclip.paste()の戻り値すなわちクリップボードの内容を保存
    #)を保存mcb_shelf
elif len(sys.argv)==2:
#キーワード一覧と内容の読み込み
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])#コマンドライン第一引数がすでにmcb_shelfにあるならその値をクリップボードにコピーする。
mcb_shelf.close()

#['test.py', 'a', 'b', 'c']
#第1引数：a
#第2引数：b
#第3引数：c

#lower():小文字にする。つまりsys.argv[1]にSAVEを入れても小文字に変換され、saveと等しくなるので、大文字入力に対する揺らぎに対応
#keys, 辞書型のキーを呼び出す.
