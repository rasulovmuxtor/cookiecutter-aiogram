# Cookiecutter Aiogram

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter),
Cookiecutter Aiogram is a framework for jumpstarting
production-ready Aiogram projects quickly.

## Features

- For Aiogram 2.22.2
- Works with Python 3.9
- Default integration
  with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying
  simple issues before submission to code review

## Usage

Let's create an aiogram project called "Manager Bot". Rather than
using `copy-paste`

Install Cookiecutter:

    $ pip install "cookiecutter>=1.7.0"

run this command:

    $ cookiecutter https://github.com/rasulovmuxtor/cookiecutter-aiogram

You'll be prompted for some values. Provide them, then an Aiogram project will
be created for you.

    Cloning into 'cookiecutter-django'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.

    project_name [The botfather]: Manager Bot
    project_slug [reddit_clone]: managerbot
    description [Group manager bot]: helps you to manage your groups.
    author_name [Daniel Roy Greenfeld]: Mukhtor Rasulov
    username [example.com]: managerbot
    version [0.1.0]: 0.0.1
    Select open_source_license:
    1 - Not open source
    2 - MIT
    3 - BSD
    4 - GPLv3
    5 - Apache Software License 2.0
    Choose from 1, 2, 3, 4, 5 [1]: 1
    use_fastapi [n]: y
    keep_envs_in_vcs [y]: y

Enter the project and take a look around:

    $ cd managerbot/
    $ ls

Create a git repo and push it there:

    $ git init
    $ git add .
    $ git commit -m "initial commit"
    $ git remote add origin https://github.com/rasulovmuxtor/managerbot.git
    $ git push -u origin master

Now take a look at your repo.

### PROJECT IS OPEN TO PULL REQUESTS

## Thanks to:

- Mukhtor Rasulov [Telegram](https://t.me/mukhtorr)
  , [LinkedIn](https://www.linkedin.com/in/mukhtor/)
