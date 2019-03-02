# Number place

## Python3

左側のplayer-boardに回答をつけて行きます
数字を埋め終わったら,finishボタンをクリックします.
confirmボタンをクリックすることで,あらかじめ与えられた問題と,自分が入力した箇所を比較することができます.
自分が入力した箇所は,緑色でマークアップされます.

![Screenshot-img](img/Screenshot.png)

## TODO
- [X] RESET選択範囲 というボタンを作る
   -> Confirm buttonで代用
- [X] BaseとなるPlayerを作る
- [X] BaseとなるComputerを作る
- [ ] 並列化
- [X] Computer 実装
- [ ] pyqt5 -> Tkinter

## Install

`sudo pip install pyqt5`

## thinking Code

[Prolog](https://en.wikipedia.org/wiki/Prolog)っぽく解いてみたい.

[事実]
- マス目は9×9, 問題は与えられる.

[ルール]
- 縦横の９マスには同じものが入らない.
- 3×3の同じボックスには同じものが入らない.
- 1から9までの数字が入る.

# 参考

[数独を数学する]:(http://www.seidosha.co.jp/book/index.php?id=2050)
