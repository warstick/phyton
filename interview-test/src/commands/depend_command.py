from module import Module

class DependCommand:
    def execute(self, args):
        depName = args[0]

        current = Module.getInstance(depName)

        for strDependency in args.subList(1, len(args)):
            dependency = Module.getInstance(strDependency)
            current.addDependency(dependency)
            dependency.addDependent(current)
        return dict()