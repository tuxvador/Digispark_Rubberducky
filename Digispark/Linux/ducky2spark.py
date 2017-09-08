#!/usr/bin/python
# Coding : utf-8
"""
    Script : ducky2spark
    Version : 1.0
    function : convert ducky scripts to binary and arduino files
"""

#imports
import os
from fnmatch import fnmatch
from subprocess import Popen,PIPE

#Strings used in programme
cf2c = "Choose file to convert : "
cb2i = "Convert ducky script to arduino script"
cd2i = "Concert binary file to arduino script"
wiyc = "What is your choice : "
convbin = "Converting file to bin"
convino = "Converting file to ino"
duckencoder = "java -jar ./exes/duckencoder.jar -i"

def choosfile(choix):
    files = ""
    path = ""
    mapping = ""
    length = 0

    if choix == 1:
        path = "./bin/"
    if choix == 2:
        path = "./scripts/"

    for files in os.walk(path):
        length = len(files)
        files = files[2]

    choix = -1
    for i,j in enumerate(files):
        print(str(i+1)+") "+j)
    while choix not in range(0,length):
        choix = int(raw_input(cf2c))-1
    path = path+files[choix]
    ifbin = path.find("./bin/")
    if(ifbin < 0):
        execute = os.popen(duckencoder).read()
        print(execute)

def main():
    choix = ""
    while(choix not in [1,2]):
        print("1) "+cd2i)
        print("2) "+cb2i)
        choix = int(raw_input(wiyc))
    choosfile(choix)


if __name__ == '__main__':
    main()
