#!/usr/bin/python3
import argparse
import os
import time
from datetime import datetime

def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False

button_names = [
    "left_control",
    "right_control",
    "left_alt",
    "right_alt",
    "enter",
    "escape",
    "tab",
    "left_shift",
    "right_shift",
    "command",
    "up_arrow",
    "down_arrow",
    "right_arrow",
    "left_arrow",
    "backspace",
    "delete",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"
]

# Create argument parser object 
parser = argparse.ArgumentParser(
                    prog='Verify Script',
                    description='A program verifies and lists what your quiet keyboard script will do',
                    epilog='Epilog') 

parser.add_argument('location', help="The location to be followed, can be dir or file")

parser.add_argument('--verbose', action='store_true', default=False, help="Sets flag enabling verbose")

args = parser.parse_args()

def log(log_string, log_type='log'):
    '''Logging function, logs to stdout. Valid log types are 'log', 'error', and 'verbose' '''
    if log_type == 'error':
        print("[" , os.getpid() , "] " , " ERROR: " , log_string)
    elif args.verbose == True and (log_type == 'log' or log_type == 'verbose'):
        print("[" , os.getpid() , "] " , " VERBOSE: " , log_string)
    elif log_type == 'log':
        print("[" , os.getpid() , "] " , log_string)

def verifyPrint(line, line_number):
    if len(line.split()) < 2:
        log("Line " + str(line_number) + ": '" + line.strip() + "'. Incorrect syntax, no string argument", 'error')
        exit(1)
    else:
        log("       '" + str(" ".join(line.split()[1:])) + "'", 'verbose')

def verifyButton(button):
    correct_button_syntax = False

    if button_names.count(button) > 0:
        correct_button_syntax = True

    return correct_button_syntax

def verifyPress(line, line_number):
    if len(line.split()) < 2:
        log("Line " + str(line_number) + ": '" + line.strip() + "'. Incorrect syntax, no arguments", 'error')
        exit(1)
    else:
        for part in line.split()[1:]:
            if verifyButton(part) == True:
                log("       'keypress: " + part + "'", 'verbose')
            else:
                log("Line " + str(line_number) + ": '" + line.strip() + "'. Incorrect syntax, Argument '" + part + "'", 'error')
                exit(1)

def verifyDelay(line, line_number):
    if len(line.split()) != 2:
        log("Line " + str(line_number) + ": '" + line.strip() + "'. Incorrect syntax, not enough arguments", 'error')
        exit(1)
    else:
        if is_float(line.split()[1]):
            log("       '" + line.split()[1] + "' seconds", "verbose")
        else:
            log("Line " + str(line_number) + ": '" + line.strip() + "'. Incorrect syntax, argument needs to be float", 'error')
            exit(1)

def verifyComment(line, line_number):
    True

instructionVerifyDict = {
    "PRINT" : verifyPrint,
    "DELAY" : verifyDelay,
    "PRESS" : verifyPress,
    "#" : verifyComment
}

if os.path.exists(os.path.abspath(args.location)) == False:
    log("File does not exist", 'error')
    exit(1)

fp = open(args.location, 'r')

log("Starting Verification and Simulation of script file: '" + args.location + "':")
log("")

for line_number, line in enumerate(fp):
    instruction = line.split()[0]

    if instruction in instructionVerifyDict:
        log(instruction + ":", 'verbose')
        instructionVerifyDict[instruction](line, line_number)
    else:
        log("Line " + str(line_number) + ": '" + line.strip() + "'. Incorrect syntax", 'error')
        exit(1)
        
    log("Line: " + str(line_number) + " Verified!", "verbose")
    log("", 'verbose')

log("Script Syntax Verified")