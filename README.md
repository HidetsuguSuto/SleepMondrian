# SleepMondrian
最上(2021)のプロジェクト
SleepMondrian
室蘭工業大学 システムデザイン学研究室 18024171 最上徹義
「睡眠状態誤認メタ認知のための定性的可視化手法の提案」で使用したシステムの説明です。

使用したもの
ハードウェア：
・PC（
　デバイス名	DESKTOP-1ES8Q3U
　プロセッサ	Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz   2.90 GHz
　実装 RAM	16.0 GB
　システムの種類	64 ビット オペレーティング システム、x64 ベース プロセッサ
　エディション	Windows 10 Home
　バージョン	21H1
　インストール日	‎2021/‎08/‎28）
・Fitbit sence

ソフトウェア
・pythonanywhere
・Fitbit API

手順（Fitbit）
1.スマートフォンにFitbitをインストールする。
2.アプリ画面の説明通り、Fitbit senceとスマートフォンを同期させる。
　※Fitbitアカウントを作成する際、登録したメールアドレスとパスワードを忘れないようにする。
3.https://dev.fitbit.com/login　で登録したメールアドレスとパスワードでログインする。
4.ログインしたら https://dev.fitbit.com に遷移する。右上のManage→Register An Appをクリック。
5.下の画像のように記入する。Website URLは自身が管理しているサイトを使用するのが好ましいと思う。
![スクリーンショット (64)](https://user-images.githubusercontent.com/92623489/152735133-e0305e32-8e29-4c73-8353-bfd61fed6813.png)
6.遷移後の画面に表示される「OAuth 2.0 Client ID」と「Client Secret」を後で使うのでメモしておく。
7.「OAuth 2.0 tutorial page」をクリックすると画面遷移する。
8.AuthorizeのFlow typeを「Authorization Code Flow」にする。
9.
