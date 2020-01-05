import os
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

## Read commands File
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../assets/commands.dat")
commandsData = open(file_path, "r")

def processLine(line):
        arguments = line.replace("\n", "").replace("\r", "").split(" ")
        cmd = operations[arguments[0]]
        if cmd is None:
            raise Exception("Unknown command " + line)
        print(line)
        args = arguments.copy()
        args.remove(arguments[0]) # remove command
        success = cmd.execute(args)
        for installedPackage in success:
            if len(success[installedPackage]) is 0:
                print(installedPackage)
            else:
                for message in success[installedPackage]:
                    print(installedPackage, "", message)
        print("\n")

def process():
    line = commandsData.readline()

    while line is not None and len(line) > 0:
        if line == "END":
            print(line)
            break
        processLine(line)
        line = commandsData.readline()

# kickoff the process
process()
