"""
    IDE: Visual Code
    Author: Mani
    Date: 01-05-2020
"""
from module.module import Module

class DependCommand:
    # This method is for adding the dependencies and dependents.
    def execute(self, args):
        depName = args[0]
        currentModule = Module.getInstance(depName)
        for strDependency in args[1:]:
            dependency = Module.getInstance(strDependency)
            currentModule.addDependency(dependency)
            dependency.addDependent(currentModule)
        return dict()