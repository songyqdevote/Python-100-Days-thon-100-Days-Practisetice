#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :access_song.py
# @Time      :2021/1/7 21:35
# @Author    :宋业强
class  Test:

    def __init__(self, foo):
        self.__foo = foo

        def __bar(self):
            print(self.__foo)
            print('__bar')

def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)




if __name__ == "__main__":
    main()
