# Python Project: Find a file using a string 🐍

This repo contains a code that will return the file path that contains the file with your string.


```
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
```
DEFINITION OF CONCEPTS

1. The Python OS library was created to be able to interact with the Operating system of a computer and carry out OS related tasks.

2. chdir- change directory

3. listdir - list directories
4. abs_path - absolute path

## CODE EXPLANATION

##### First step: import module:
The os module is a python library that facilates the interaction with your operating system

```
import os
```

##### second step: write a code that will ask the user for the string to search for and the file path to find the string
```
text = input("Enter the text your are searching for: ")
path = input("Enter the path to the file containing the text: ")

```
##### third step: define the function that will help look up the directory, change to the directory and list the directory

```
def lookup_files(path):
    f = 0
    os.chdir(path)
    files = os.listdir()
    #print(files)
```
##### fourth step: Iterate through the file path and look for the file with the specific string and return it

```
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
```
