from module.module import Module

class RemoveCommand:
    def execute(self, args):
        d = Module.getInstance(args[0])
        if d is not None:
            return self.uninstall(d)
        result = dict()
        result[args[0]] = "is not installed"
        return result

    def uninstall(self, parent):
        result = dict()
        installedDependents = set()
        for dep in parent.getDependents():
            if dep.isInstalled == True:
                installedDependents.add(dep)
        if len(installedDependents) is 0:
            result[parent.getName()] = "successfully removed"
            parent.setInstalled(False)

            for dependency in parent.getDependencies():
                if dependency.isInstalled == True:
                    result.update(self.uninstall(dependency))
        else:
            result[parent.getName()] = "is still needed."
        return result