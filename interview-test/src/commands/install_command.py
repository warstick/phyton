from module.module import Module

class InstallCommand:
    # Execute the installation of the module / package
    def execute(self, args):
        result = dict()
        for depName in args:
            dep = Module.getInstance(depName)
            self.install(dep, result)
        return result

    # Recurssive funtion for the installing the module / package with dependency modules / packages
    def install(self, current, result):
        if current.isInstalled is False:
            current.setInstalled(True)
            for dependency in current.getDependencies():
                if dependency.isInstalled is False:
                    self.install(dependency, result)
            result[current.getName()] = ["successfully installed"]
        else:
            result[current.getName()] = ["is already installed"]
        return result