# coding=utf-8
"""
@author:FiaFia
@data:2018/7/9
@version:Python3.6
@FileName: CopyFile.py
"""
import sys
import os
import shutil


def copyFile(filelist, targetDir):
    log = open('running.log', 'w')
    with open(fileList) as f:
        for line in f.readlines():
            line = line.strip('\r\n')
            basename = os.path.basename(line)
            exists = os.path.exists(line)
            if exists:
                fullPath = os.getcwd() + '\\' + targetDir + '\\' + basename
                print('Copy %s to %s' % (line, fullPath))
                log.write('Copy %s to %s \r\n' % (line, fullPath))
                shutil.copy(line, targetDir +'\\' + basename)
            else:
                print("%s not exists" % line)
                log.write("%s not exists \r\n" % line)
    log.close()


if __name__ == '__main__':
    #fileList = 'filelist.txt'
    fileList = input('Please input filelist:')
    targetDir = 'NewFolder'
    copyFile(fileList, targetDir)
