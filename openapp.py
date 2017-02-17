#!/usr/bin/env python
# coding:utf-8
import os
import getpass

__version__ = 1.0
__author__ = sherry


app_path = '/Applications'
zsh_path = '~/.zshrc'

# list dir app
def get_dir_list(path):
    dir_list = os.listdir(path)
    return dir_list

# filter the app list
def filter_list(dir_list):
    app_dict = {}
    for app in dir_list:
        if app.endswith('.app'):
            app_dict[app[:-4].replace(" ", "").lower()] = app[:-4]

    del dir_list
    return app_dict


def generate_command_lines(app_dict):
    commands = []
    for line in app_dict.keys():
        open_command = "\"open /Applications/" + app_dict[line] + ".app\""
        alias_command = "alias " + line + "=" + open_command
        echo_command = "echo \'" + alias_command +  "\' >>~/.zshrc"
        os.system(echo_command)
        commands.append(echo_command)
    return commands

def get_user():
    return getpass.getuser()

def get_path(path):
    return '/Users/' + get_user() + path

if __name__ == '__main__':
    list = filter_list(get_dir_list(app_path))
    print generate_command_lines(list)
    os.system("source ~/.zshrc")
    # print list

# TODO:
'''
# 用click的库
## 加一个openapp 的快捷键: 方便管理所有alias .
# 其中包括: 添加参数, 即可:
    1. 删除
    2. 添加(?)
    3. update
    4. 查找(search)
    5. 重置

'''

'''
脑洞大开, 做一个GUI
'''
