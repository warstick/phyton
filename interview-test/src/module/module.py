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
    
    @staticmethod
    def getInstance(name):
        target = Module.dependencyDictionary.get(name)
        if target is None:
            target = Module(name)
            Module.dependencyDictionary[name] = target
        return target
    
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

    @staticmethod
    def getInstalled():
        installed = set()
        for module in Module.dependencyDictionary.values():
            if module.isInstalled == True:
                installed.add(module)
        return installed
