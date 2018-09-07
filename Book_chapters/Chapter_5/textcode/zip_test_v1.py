# zip_test_v1.py
import sys
import os
import shutil
import zipfile

class ZipReplace:
    # 始化时以一个.zip的文件名和查找、替换字符串作为参数
    def __init__(self, filename, search_string, replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        # 创建一个临时的目录存储这些解压缩后的文件
        self.temp_directory = "./unzipped-{}".format(filename)

    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)

