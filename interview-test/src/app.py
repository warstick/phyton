"""
    IDE: Visual Code
    Author: Mani
    Date: 01-05-2020
"""
import os
import sys
from commands.depend_command import DependCommand
from commands.install_command import InstallCommand
from commands.list_command import ListCommand
from commands.remove_command import RemoveCommand

## Create Dictonary for Operations
operations = dict({
    "DEPEND": DependCommand(),
    "INSTALL": InstallCommand(),
    "REMOVE": RemoveCommand(),
    "LIST": ListCommand()
})

# Read the command line argument if you don't find take the default commands file path
def getFileName():
    fileName = None
    if len(sys.argv) is 2:
        fileName = sys.argv[1]
    return "../assets/commands.dat" if fileName is None else fileName

## Read commands File
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, getFileName())
# Read the command the file
commandsData = open(file_path, "r")

def processLine(line):
        # Replacing NewLine / Carriage Return with empty and break the line into List
        arguments = line.replace("\n", "").replace("\r", "").split(" ")
        cmd = operations[arguments[0]] #arguments[0] - Read the Operation Type
        if cmd is None:
            raise Exception("Unknown command " + line)
        print(line)
        args = arguments.copy()
        args.remove(arguments[0]) # remove command - Operation Type
        success = cmd.execute(args)
        # Loop through the Return values from the Execute Function of every operation
        for installedPackage in success:
            # For Handling List Command Values
            if len(success[installedPackage]) is 0:
                print(installedPackage)
            else:
                for message in success[installedPackage]:
                    print(installedPackage, "", message)
        print("\n")

def process():
    #read Each Line
    line = commandsData.readline()

    while line is not None and len(line) > 0:
        # if line consisting of END it wil break the loop
        if line == "END":
            print(line)
            break
        #Process Command
        processLine(line)
        # Read Next Line
        line = commandsData.readline()

# kickoff the process
try:
    process()
except:
    print("something went wrong")
finally:
    #Close the File Stream
    commandsData.close()
