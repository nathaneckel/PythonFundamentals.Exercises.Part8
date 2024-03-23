import os
from os import listdir
from os.path import isfile
from typing import Tuple, List, Iterator

import directories


# os.chdir('/Users/nathan/Dev/Labs/PythonFundamentals.Exercises.Part8/Exercise2')
# # for f in os.listdir():
# with open('ChildDirectory1/child.txt', 'w') as f:
#     f.write('Test')


# def tree(dir_path):
#     with open('child.txt', 'w') as f:
#         for root, dirs, files in os.walk(dir_path):
#             f.write(f"Directory: {root}\n")
#             for file in files:
#                 f.write(f" File: {file}\n")
#
#     #dir_path = os.walk("/Users/nathan/Dev/Labs/PythonFundamentals.Exercises.Part8/Exercise2")
#     dir_path = os.walk("~/Dev/Labs/PythonFundamentals.Exercises.Part8/Exercise2")
#
#     tree(dir_path)

#
# for f in listdir(str.path):
#     if not isfile(str.path):
#         filepath = "{0:s}/~/Dev/Labs/PythonFundamentals.Exercises.Part8/Exercise2".format
#         with open(filepath, 'w') as f:
#             f.write('Hi there!')





def tree(dir_path):

    with open("dir_contents.txt", 'w') as f:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                f.write(file_path + " - I just wrote this! \n")
dir_path = "/Users/nathan/Dev/Labs/PythonFundamentals.Exercises.Part8/Exercise2"
tree(dir_path)




        # file.filename = "*"
    # file.filetext = "*"

    # directories: Iterator[tuple[str, list[str], list[str]]] = os.walk("/Users/nathan/Dev/Labs/PythonFundamentals.Exercises.Part8/Exercise2")


# for directory in directories: