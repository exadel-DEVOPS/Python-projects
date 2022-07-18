# Import modules

import os

# ask user to enter text and path
text = input("Enter the text your are searching for: ")
path = input("Enter the path to the file containing the text: ")


# define a function that will help check the file path input
def lookup_files(path):
    f = 0
    os.chdir(path)
    files = os.listdir()
    #print(files)


# iterate through the files in the file path
    for file_name in files:
        abs_path = os.path.abspath(file_name)
        if os.path.isdir(file_name):
            lookup_files(abs_path)
        if os.path.isfile(abs_path):
            f = open(file_name, 'r')
            if text in f.read():
                f = 1
                print(text +  " ", "found in")
                last_path = os.path.abspath(file_name)
                print(last_path)
                return True

        if f == 1:
            print(text + "not found")
            return False

lookup_files(path)