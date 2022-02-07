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

手順：Fitbit API編
1.スマートフォンにFitbitをインストールする。
2.アプリ画面の説明通り、Fitbit senceとスマートフォンを同期させる。
　※Fitbitアカウントを作成する際、登録したメールアドレスとパスワードを忘れないようにする。
ここからは　https://watlab-blog.com/2021/05/30/fitbit-api/ を参照した方が分かりやすいと思う。
3.https://dev.fitbit.com/login　で登録したメールアドレスとパスワードでログインする。
4.ログインしたら https://dev.fitbit.com に遷移する。右上のManage→Register An Appをクリック。
5.下の画像のように記入する。Website URLは自身が管理しているサイトを使用するのが好ましいと思う。
![スクリーンショット (64)](https://user-images.githubusercontent.com/92623489/152735133-e0305e32-8e29-4c73-8353-bfd61fed6813.png)
6.遷移後の画面に表示される「OAuth 2.0 Client ID」と「Client Secret」を後で使うのでメモしておく。
7.「OAuth 2.0 tutorial page」をクリックするとページ遷移する。
8.1: AuthorizeのFlow typeを「Authorization Code Flow」にする。
9.1: Authorizeの下にあるURLをクリックするとページが遷移する。
10.取得したいデータを選択し許可するとページが遷移する。
11.ページのURL欄に記載の「code=」の次から「#」までの間の文字列をCode欄にコピペする。
12.Fitbit APIのページに戻り、2: Parse responseに手順11でコピペしたコードをペーストする。
13.access_tokenやrefresh_tokenが記載されたテキストが生成されるので、これを「token.txt」というファイルにして保存する。（場所はどこでもよい）

手順：pythonanywhere編
https://tutorial.djangogirls.org/ja/deploy/ を参照すると分かりやすいと思うが、途中から手順が異なるので注意してほしい。
1.pythonanywhereのアカウントを作成する。
2.「Account」ページに移動したら、「API Token」というタブを選んで、「Create new API token」のボタンを押す。
3.ロゴをクリックしてDashboardに戻り、New console:の「Bash」をクリックする。
4.コンソール画面で「pip3.6 install --user pythonanywhere」を実行する。
5.次に「pa_autoconfigure_django.py --python=3.6 https://github.com/HidetsuguSuto/SleepMondrian」を実行する。
6.コンソール画面を閉じてFilesに行く。/home/(ユーザー名)/（ユーザー名）.pythonanywhere.com　まで移動する。
7.Upload a fileをクリック。Fitbit API編で保存した「token.txt」をアップロードする。
8./home/loserruza/loserruza.pythonanywhere.com/blog　に移動し「sleep.py」を開く。
9.14、15行目にFitbit API編でメモしておいた「OAuth 2.0 Client ID」と「Client Secret」を記入する。
10.次に右上にあるWebをクリックし、左側にある（ユーザー名）.pythonanywhere.comをクリック。
11.画面を下にスクロールさせ、Virtualenv:にある Start a console in this virtualenv をクリックし仮想環境のコンソル画面を開く。
12.「pip install pycairo」と「pip install opencv-python」と「pip install fitbit」を実行する。
13.コンソール画面を閉じ、Filesの/home/loserruza/.virtualenvs/loserruza.pythonanywhere.com/lib/python3.6/site-packages/fitbit に移動する。
14.api.pyを開き、23行目と191行目にあるAPI_versionを1から1.2に変更する。
15.

手順：実行編
