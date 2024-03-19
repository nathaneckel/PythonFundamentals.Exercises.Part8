import os
from os import listdir
from os.path import isfile
def tree():

    str.path = os.walk("/Users/nathan/Dev/Labs/PythonFundamentals.Exercises.Part8/Exercise2")
# path = os.walk("~/Dev/labs/Exercise2")


for f in listdir(str.path):
    if not isfile(str.path):
        filepath = "{0:s}/dummy.txt".format(str.path)
        with open(filepath, 'w') as f:
            f.write('Hi there!')

            # file.filename = "myfile.txt"
            #     file.filetext = "mytext"
            # #directories = os.walk("~/Dev/labs/Exercise2")
            # directories = os.walk("/Users/nathan/Dev/Labs/PythonFundamentals.Exercises.Part8/Exercise2")
            # for directory in directories:
            #     with open(directory[0]+"\\"+filename, "w") as file:
            #         file.write(filetext)