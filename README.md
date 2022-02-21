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
・Fitbit sense

ソフトウェア
・pythonanywhere
・Fitbit API

環境
・Windows 10 Home ウェブブラウザはMicrosoftEdgeを使用した
(手順：Fitbit API編の13でうまくいかない場合はiMacを使用する。実験では以下のiMacを実際に使用した。
・iMac, MacOS:Big Sur Version 11.6, Processor:3.1GHz 6-Core Intel Core i5, Memory:8GB 2667MHz DDR4)

手順：Fitbit API編
1.スマートフォンにFitbitをインストールする。(AndroidならGooglePlayStoreから、iPhoneならAppStoreから)
2.アプリ画面の説明通り、Fitbit senseとスマートフォンを同期させる。
　※Fitbitアカウントを作成する際、登録したメールアドレスとパスワードを忘れないようにする。
ここからは　https://watlab-blog.com/2021/05/30/fitbit-api/ を参照した方が分かりやすいと思う。
3.https://dev.fitbit.com/login　で登録したメールアドレスとパスワードでログインする。
4.ログインしたら https://dev.fitbit.com に遷移する。右上のManage→Register An Appをクリック。
5.下の画像のように・Application Neme ・Description ・Application Website URL ・Organization ・Organization Website URL ・Terms of Service URL ・Privacy Policy URL ・OAuth 2.0 Application Type ・Redirect URL ・Default Access Type を記入、変更する。URLは自身が管理しているサイトを使用するのが好ましいと思う。
![スクリーンショット (64)](https://user-images.githubusercontent.com/92623489/152735133-e0305e32-8e29-4c73-8353-bfd61fed6813.png)
6.遷移後の画面に表示される「OAuth 2.0 Client ID」と「Client Secret」を後で使うのでメモしておく。
7.「OAuth 2.0 tutorial page」をクリックするとページ遷移する。
8.1: AuthorizeのFlow typeを「Authorization Code Flow」にする。
9.1: Authorizeの下にあるURLをクリックするとページが遷移する。
10.取得したいデータを選択し許可するとページが遷移する。
11.ページのURL欄に記載の「code=」の次から「#」までの間の文字列をCode欄にコピペする。
12.Fitbit APIのページに戻り、1A Get Codeに手順11でコピペしたコードをペーストする。するとコードが生成されるのでコピーする。（curl -i ～　oauth2/tokenまですべてコピー）
13.Terminalやコマンドプロンプトで生成されたコードをペーストし実行する。※Windowsのコマンドプロンプトではcurlが入っていない場合が多いためできない可能性がある。その場合コードをiMacに送信し、iMacのターミナル上で実行すればできるはず。
14.access_tokenやrefresh_tokenが記載されたテキストが生成されるので、これを「token.txt」というファイルにして保存する。（場所はどこでもよい）

手順：pythonanywhere編
https://tutorial.djangogirls.org/ja/deploy/ を参照すると分かりやすいと思うが、途中から手順が異なるので注意してほしい。
プログラムはUnix系で書いている。PCによっては/を抜いて'を"に変える必要がある。
1.pythonanywhereのアカウントを作成する。
2.「Account」ページに移動したら、「API Token」というタブを選んで、「Create new API token」のボタンを押す。
3.ロゴをクリックしてDashboardに戻り、New console:の「Bash」をクリックする。
4.コンソール画面で「pip3.6 install --user pythonanywhere」を実行する。
5.次に「pa_autoconfigure_django.py --python=3.6 https://github.com/HidetsuguSuto/SleepMondrian」を実行する。
6.コンソール画面を閉じてFilesに行く。/home/(ユーザー名) まで移動する。
7.Upload a fileをクリック。Fitbit API編で保存した「token.txt」をアップロードする。
8./home/(ユーザー名)/(ユーザー名).pythonanywhere.com/blog　に移動し「sleep.py」を開く。
9.14、15行目にFitbit API編でメモしておいた「OAuth 2.0 Client ID」と「Client Secret」を保存する。
10.次に右上にあるWebをクリックし、左側にある（ユーザー名）.pythonanywhere.comをクリック。
11.画面を下にスクロールさせ、Virtualenv:にある Start a console in this virtualenv をクリックし仮想環境のコンソール画面を開く。
12.「pip install pycairo」と「pip install opencv-python」と「pip install pandas」と「pip install fitbit」を実行する。
13.コンソール画面を閉じ、Filesの/home/(ユーザー名)/.virtualenvs/(ユーザー名).pythonanywhere.com/lib/python3.6/site-packages/fitbit に移動する。
14.api.pyを開き、23行目と191行目にあるAPI_versionを1から1.2に変更する。
15.Filesの /home/(ユーザー名)/(ユーザー名).pythonanywhere.com に移動し、Directoriesにstaticと入力し、New directoryを押す。
16.Filesの /home/(ユーザー名)/(ユーザー名).pythonanywhere.com/blog に移動し、views.pyを開く。
17.views.pyの303行目と307行目と315行目の(ユーザー名)を自身のユーザー名に変更する。
17.Webのページに行き、Reloadを押す。

手順：実行編
Fitbit senseを着用し一晩寝てからシステムを起動する。
システムはpythonanywhereのWebに移動し、(ユーザー名).pythonanywhere.comをクリックすると開く。
初期のログインIDとパスワードはどちらも「sleep」に設定している。
また、まだ寝てないときはデータがないためエラー画面に遷移する。
そしてタイムアウトしたり、ログインを何度も失敗すると失効するときがあるため、再度ウェブサイト開きなおさないといけない場合がある。

一時的にFitbitを使用しなくても出力を確認する手順を説明する。
1.pythonanywhereのFilesの /home/(ユーザー名)/(ユーザー名).pythonanywhere.com/blog に移動し、sleep.pyを開く。
2.5行目からすべてコメントアウトする。
3.コメントアウトしていないところにsleepEfficiency = (int) を記入し保存するする。(int)は好きな睡眠効率（0～100）を入れる。
4.Webのページに行き、Reloadを押す。
以上を行えばシステムの動作を確認できる。

プログラム改変方法

