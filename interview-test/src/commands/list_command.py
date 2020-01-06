from module.module import Module

class ListCommand:
    # This method returns the information about the installed modules / packages
    def execute(self, args):
        result = dict()
        for m in Module.getInstalled():
            result[m.getName()] = []
        return result
