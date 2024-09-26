# フルスタックWeb開発

## Django+React(Next.js)+Docker



### 環境構築
- docker-compose up --build -d

#### backend(Django)
- docker-compose exec -it backend /bin/bash
- pip freeze > requirements.locl
- django-admin startproject config .
- python manage.py runserver 0:5000 --settings config.settings.development
- http://localhost:5000/

#### frontend(React(Next.js))
- docker-compose exec -it frontend /bin/bash
- yarn create next-app frontend --ts --eslint
- yarn dev
- http://localhost:3000
- yarn add @mui/material @emotion/react @emotion/styled
- yarn add @mui/x-data-grid
- yarn add axios
- yarn add swr
- yarn add react-hook-form
- yarn add @mui/icons-material

#### database(MySQL)

#### 参照サイト
- [DockerでDjango・React環境を構築する](https://qiita.com/shiranon/items/b3efd3ed7ce473c6ad83)
- [DockerでReact＋Django+Nginx＋MySQLの環境構築](https://qiita.com/greenteabiscuit/items/c40ba038703c9f33499b)
- [モダンなWebアプリ(Django, Next.js, Docker, AWS)を開発する #環境構築編](https://qiita.com/azumarions/items/2b7f9730196e943134f6)



### github(ssh)
- mkdir ~/.ssh
- ssh-keygen -t ed25519 -C "miya.taka.0096@gmail.com"
- touch ~/.ssh/config
- cat ~/.ssh/id_ed25519.pub
- githubにsshキーを登録
- ssh -T git@github.com

#### 参照サイト
- [UbuntuからGitHubへのSSH接続設定](https://zenn.dev/perilla/scraps/351f43bfcd13ec)
- [GitHubにSSH接続する完全版](https://bkbkb.net/articles/ssh_github)



### その他
- 現在のディレクトリ以下すべてのファイルパーミッションを変更するには `sudo chmod -R 777 .` を実行
- gitのブランチ名を変更するときは
  - 現在いるブランチの名前を変更する場合： `git branch -m <新しいブランチ名>`
  - 他のブランチ名を変更する場合： `git branch -m <古いブランチ名> <新しいブランチ名>`
- githubアカウントが同一であれば、新たにSSH鍵の登録はいらない