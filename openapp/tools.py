#!/usr/bin/env python
# coding:utf-8
import os

basedir = '~/.zshrc'

def log(*args):
    print args



# 统计file的行数
def count_file_line(path):
    command = 'cat ' + path + '|wc -l'
    return os.system(command)

# 参考: https://github.com/MrKiven/Todo.py/blob/master/Todos/log.py


# Python 库click的使用, 代替arg
# http://www.xiaoh.me/2016/01/29/click-command/

# 删除已经添加的行数
# 参考 http://stackoverflow.com/questions/2329417/fastest-way-to-delete-a-line-from-large-file-in-python
# TODO:把对文件的操作写成类,方便调用
def delete_added_lines(path):
    return


if __name__ == '__main__':
    print count_file_line(basedir)


# TODO: Chrome打不开 因为进行了转义:
# open /Applications/Google\ Chrome.app
# 而不是: open /Applications/Google Chrome.app

# TODO: log 参考: https://github.com/AdamEECS/chest/blob/master/cn_parser.py

class DirMap(object):
    __slot__ = ()
    def __init__(self, dir_list):
        self.dir_list = dir_list
        self.app_list = self.get_all_list()
        self.app_map = self.generate_all_map()

    def get_all_list(self):
        for dir in self.dir_list:
            self.app_list += os.listdir(dir)
        return self.app_list

    def generate_all_map(self):
        app_map = {}
        for app in self.app_list:
            if app.endswith('.app'):
                self.app_map[app[:-4].replace(" ", "").lower()] = app[:-4]
        return app_map

    def __del__(self):
        del self.dir_list, self.app_list, self.app_map

    # def



class EditFile(object):
    __slot__ = ()

    '''
     初始化类:
     @:param file_path: 需要修改的文件地址, 例如: '/Application', '~/Application'
    '''

    def __init__(self, file_path, app_path):
        self.file_size = 0
        self.file_path = file_path
        self.dir_path = app_path
        self.dir_list = []
        self.app_dict = {}

    def __del__(self):
        del self.file_size, self.file_path, self.dir_path, self.dir_list

    def __repr__(self):
        return self.file_path

    # 对文件的操作
    # 包括: 读文件, 计算文件, 写文件, 重置文件
    def read(self):
        return

    def count_file_line(self):
        command = 'cat ' + self.file_path + '|wc -l'
        return os.system(command)

    def reset_file(self):
        return

    # 对目录的操作
    def get_dir_list(self):
        return os.listdir(self.dir_list)

    # 生成命令行
    def generate_command_lines(self):
        commands = []
        for line in self.app_dict.keys():
            open_command = "\"open /Applications/" + self.app_dict[line] + ".app\""
            alias_command = "alias " + line + "=" + open_command
            echo_command = "echo \'" + alias_command +  "\' >>~/.zshrc"
            os.system(echo_command)
            commands.append(echo_command)
        return commands

    def




'''
class FunctionalList:
    # 一个列表的封装类，实现了一些额外的函数式
    # 方法，例如head, tail, init, last, drop和take。

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # 如果键的类型或值不合法，列表会返回异常
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def append(self, value):
        self.values.append(value)

    def head(self):
        # 取得第一个元素
        return self.values[0]

    def tail(self):
        # 取得除第一个元素外的所有元素
        return self.valuse[1:]

    def init(self):
        # 取得除最后一个元素外的所有元素
        return self.values[:-1]

    def last(self):
        # 取得最后一个元素
        return self.values[-1]

    def drop(self, n):
        # 取得除前n个元素外的所有元素
        return self.values[n:]

    def take(self, n):
        # 取得前n个元素
        return self.values[:n]
'''
