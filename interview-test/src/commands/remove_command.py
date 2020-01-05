from module.module import Module

class RemoveCommand:
    def execute(self, args):
        d = Module.getInstance(args[0])
        if d is not None:
            return self.uninstall(d, False)
        result = dict()
        result[args[0]] = ["is not installed"]
        return result

    def uninstall(self, parent, isInnerDependency):
        result = dict()
        installedDependents = set()
        for dep in parent.getDependents():
            if dep.isInstalled == True:
                installedDependents.add(dep)
        if len(installedDependents) is 0:
            messages = list()
            if isInnerDependency == True:
                messages.append("is no longer needed")
            messages.append("is not installed") if parent.isInstalled == False else messages.append("successfully removed")
            result[parent.getName()] = messages
            parent.setInstalled(False)

            for dependency in parent.getDependencies():
                if dependency.isInstalled == True:
                    result.update(self.uninstall(dependency, True))
        else:
            result[parent.getName()] = ["is still needed."]
        return result