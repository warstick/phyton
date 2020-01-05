from module.module import Module

class DependCommand:
    def execute(self, args):
        depName = args[0]

        currentModule = Module.getInstance(depName)

        for strDependency in args[1:]:
            dependency = Module.getInstance(strDependency)
            currentModule.addDependency(dependency)
            dependency.addDependent(currentModule)
        return dict()