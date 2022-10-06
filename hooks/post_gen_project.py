from __future__ import print_function

import os
import random
import shutil
import string

try:
    # Inspired by
    # https://github.com/django/django/blob/master/django/utils/crypto.py
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

DEBUG_VALUE = "debug"


def remove_pycharm_files():
    idea_dir_path = ".idea"
    if os.path.exists(idea_dir_path):
        shutil.rmtree(idea_dir_path)


def remove_heroku_files():
    file_names = ["Procfile", "runtime.txt"]
    for file_name in file_names:
        os.remove(file_name)


def append_to_gitignore_file(ignored_line):
    with open(".gitignore", "a") as gitignore_file:
        gitignore_file.write(ignored_line)
        gitignore_file.write("\n")


def remove_aws_dockerfile():
    shutil.rmtree(os.path.join("compose", "production", "aws"))


def remove_fastapi_files():
    shutil.rmtree(os.path.join('main.py'))


def remove_open_source_files():
    file_names = ["CONTRIBUTORS.txt", "LICENSE"]
    for file_name in file_names:
        os.remove(file_name)


def main():
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_open_source_files()

    if "{{ cookiecutter.use_pycharm }}".lower() == "n":
        remove_pycharm_files()

    if "{{ cookiecutter.keep_envs_in_vcs }}".lower() == "y":
        append_to_gitignore_file(".env")
        append_to_gitignore_file(".envs/*")

    if "{{ cookiecutter.use_fastapi }}".lower() == "n":
        remove_fastapi_files()

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


if __name__ == "__main__":
    main()
