from module.module import Module

class InstallCommand:
    def execute(self, args):
        result = dict()
        for depName in args:
            dep = Module.getInstance(depName)
            self.install(dep, result)
        return result

    def install(self, current, result):
        if current.isInstalled == False:
            current.setInstalled(True)
            for dependency in current.getDependencies():
                if dependency.isInstalled == False:
                    self.install(dependency, result)
            result[current.getName()] = ["successfully installed"]
        else:
            result[current.getName()] = ["is already installed"]
        return result