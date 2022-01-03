import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve (s: str) -> str:
    work = s.capitalize ()
    out = ""
    size = len (work)
    for i in range (size):
        c = work[i]

        if c.isspace ():
            out += c
            continue
        elif c.isdigit ():
            out += c
            continue
        elif c.islower () and s[i - 1].isspace ():
            out += c.upper ()
        else:
            out += c

    return out


"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, "alison heck" should be capitalised correctly as "Alison Heck".

Given a full name, your task is to capitalize the name appropriately.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    s = input ()
    result = solve (s)
    print (result)
