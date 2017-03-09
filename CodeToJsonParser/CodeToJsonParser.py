#!/usr/local/bin/python
import os
import signal
import sys
import pyperclip
import json


while True:
    # ctrl-c to quit
    data = {}

    input_code = []
    while True:
        input_function = input("New function name:\n")
        text = ""

        if input_function == "":

            pyperclip.copy(json.dumps(data))

            print("Data copied to clipboard.")

            break
        else:
            data[input_function] = {}

            print("Paste the Lines of code:\n")
            data[input_function]["header"] = input()

            while True:
                line = input()
                if line:
                    input_code.append(line)
                else:
                    break

            data[input_function]["lines"] = input_code
            input_code = []

