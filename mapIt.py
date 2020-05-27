#coding:utf-8
import webbrowser, sys, pyperclip
import urllib

if len(sys.argv)> 1:
#コマンドラインから住所を取得する。
    address=''.join(sys.argv[1:])
else:
#クリップボードから住所を取得する。
    address=pyperclip.paste().encode("utf-8")
url = 'https://www.google.co.jp/maps/place/' + urllib.quote_plus(address)
webbrowser.open(url)
