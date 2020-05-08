#!/usr/bin/python3.8

import subprocess as sp
from datetime import datetime


def currentDateTime():

    currentDT = datetime.now()
    current = currentDT.strftime("%d%b%Y %H:%M:%S")

    return current


def nmapCommand(fileName):

    # Change ip to target ip address
    ip = "127.0.0.1"

    command = "nmap -O -sV -vvvvv -T5 --script=banner -oN " + fileName + " " + ip
    sp.call(command, shell=True)

    return None


def fileNameFormat(currentDT):

    # Change targetName to your targets name
    targetName = "localhost"

    dateTimeList = list(currentDT)

    fileName = targetName + "_nmap_scan_" + fixDateTimeFormat(dateTimeList)

    return fileName


def fixDateTimeFormat(dateTimeList):

    dateTimeList[9] = "_"

    return "".join(dateTimeList) + ".txt"


def main():

    currentDT = currentDateTime()
    print("nmap_scan.py launching: " + currentDT + "\n")

    fileName = fileNameFormat(currentDT)
    print("File Name: " + fileName + "\n")

    nmapCommand(fileName)


if __name__ == "__main__":
    main()
