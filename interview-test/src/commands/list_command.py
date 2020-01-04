from module import Module

class ListCommand:
    def execute(self, args):
        result = dict()
        for m in Module.getInstalled():
            result[m.getName()] = ""
        return result
