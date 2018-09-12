# -*- coding: UTF-8 -*-
import sys
import os
import re



class Count:
    def getCharsCount(data):
        chars: int = len(data)
        print ('字符数：',chars)

    def getWordsCount(data):
         data0 = re.sub("\W"," ",data,count=0)
         data1 = re.sub ("_"," ",data0,count=0)
         words = len(data1.split())
         print ('单词数：',words)

    def getLinesCount(data):
        lines = data.count('\n')+1
        print( '行数：',lines)

    def recursiveDir(filePath):
        if  os.path.isdir(filePath):
          fileList = os.listdir(filePath)
          for file in fileList:
            newpath = filePath + '/' + file
            if os.path.isdir(newpath):
                Count.recursiveDir(newpath)  # 递归
            if os.path.isfile(newpath):
                try:
                    data = open(newpath, 'r')
                    data1 = data.read()
                    data.close()
                    print(newpath)
                    Count.getCharsCount(data1)
                    Count.getLinesCount(data1)
                    Count.getWordsCount(data1)
                except:
                    print('this file can not be opened')
        else :
            print('please input the path of folder!')

    def special_linenum(file):
        with open(file) as fp:
            content_list = fp.readlines()
            code_num = 0
            blank_num = 0
            annotate_num = 0
            for content in content_list:
                content = content.strip()
                # 统计空行
                if content == '':
                    blank_num += 1
                # 统计注释行
                elif content.startswith('#') or content.startswith('//'):
                    annotate_num += 1
                # 统计代码行
                else:
                    code_num += 1
        print('空白行：',blank_num)
        print('注释行：',annotate_num)
        print('代码行：',code_num)


def main():
    while True :
       str = sys.stdin.readline()
       list = str.split()
       filePath = list[1][0:len(str) - 1]
       if list[0]=='-s':
          Count.recursiveDir(filePath)
       elif list[0]=='-a':
          Count.special_linenum(filePath)
       else :
          if os.path.exists(filePath):
              file = open(filePath, 'r')
              data = file.read()
              file.close()
              if list[0] == '-c':
                  Count.getCharsCount(data)
              if list[0] == '-l':
                  Count.getLinesCount(data)
              if list[0] == '-w':
                  Count.getWordsCount(data)

          else:
              print('This is not a valid path or file ')

if __name__ == "__main__":
    main()