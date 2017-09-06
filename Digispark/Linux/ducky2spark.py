#!/usr/bin/python
# Coding : utf-8
"""
    Script : ducky2spark
    Version : 1.0
    function : convert ducky scripts to binary and arduino files
"""

#imports
import os
from subprocess import Popen,PIPE

#Strings used in programme
cf2c = "Choose .duck files to convert"
cb2i = "Concert binary file to arduino script"
cd2i = "Convert ducky script to arduino"
wiyc = "What is your choice : "

def choosfile():
    directory = Popen("ls ./scripts", stdout=PIPE)
    output = "..\n" + directory.stdout.read()
    output = output.split('\n')
    output.pop(-1)
    files = ""
    print output

def main():
    choix = ""
    while(choix not in ['1','2']):
        print("1) "+cd2i)
        print("2) "+cb2i)
        choix = raw_input(wiyc)
    if choix == '1':
        print("[+] You chose to convert from binary to ino script")
    else:
        print("[+] You chose to convert from ducky script to ino script")
    choosfile()


if __name__ == '__main__':
    main()
