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
    "LIST": InstallCommand()
})

## Read commands File
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../assets/commands.dat")
print(file_path)
commandsData = open(file_path, "r")

print("file conent", commandsData)

def processLine(line):
        arguments = line.split(" ")
        cmd = operations[arguments[0]]
        if cmd is None:
            raise Exception("Unknown command " + line)
        print(line)
        args = set(arguments)
        args.remove(arguments[0]) # remove command
        success = cmd.execute(args)
        
        for installedPackage in success.values():
            print("/t", installedPackage)

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
