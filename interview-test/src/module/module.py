"""
    IDE: Visual Code
    Author: Mani
    Date: 01-05-2020
"""
# This Class Holds the Each Module / Package information
# Like Depednecies, IsModule Installed or not and Dependants
class Module:
    # varibles definition
    dependencyDictionary = dict()
    dependencies = set()
    dependents = set()
    name= ''
    isInstalled = False

    # constructor
    def __init__(self, name):
        self.name = name
        self.dependencies = set()
        self.dependents = set()
    
    # This static Method is for check the whether module is existed or not.
    # If it is not existed create new moudle with the name and save it in Dependency Dictionary.
    @staticmethod
    def getInstance(name):
        target = Module.dependencyDictionary.get(name)
        if target is None:
            target = Module(name)
            Module.dependencyDictionary[name] = target
        return target
    
    # Method Definitions.
    def getName(self):
        return self.name
    
    def setInstalled(self, installed):
        self.isInstalled = installed
    
    def hasDependencies(self):
        return len(self.dependencies) > 0

    def getDependencies(self):
        return self.dependencies

    def addDependency(self, d):
        return self.dependencies.add(d)
    
    def getDependents(self):
        return self.dependents

    def hasDependents(self):
        return len(self.dependents) > 0

    def addDependent(self, d):
        return self.dependents.add(d)
    
    def getAll(self):
        return self.dependencyDictionary.values()

    # This static Method is returns the installed Packages / Modules
    # from the saved dictionary
    @staticmethod
    def getInstalled():
        installed = set()
        for module in Module.dependencyDictionary.values():
            if module.isInstalled is True:
                installed.add(module)
        return installed
