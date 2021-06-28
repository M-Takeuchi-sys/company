Python version 3.8.8
Django version 3.0.5

1. git cronする 
https://github.com/M-Takeuchi-sys/company

2. プロジェクト直下でデータベースを初期化する
python manage.py migrate

3. migrationを作成する
python manage.py makemigrations myapp

4.データベースを反映させる
python manage.py migrate

以上でローカル環境で動作確認できました。
出来なかった場合、再度ご報告お願いいたします。
