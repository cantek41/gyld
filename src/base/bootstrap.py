
import json



class Bootstrap():
    def __init__(self, executors):
        self.executors = executors

    def run(self):
        bootstrap= {}
        for key, executor in self.executors.items():
            if isinstance(executor, dict):
               bootstraps = {}
               for ky,executr in executor.items():
                   bootstraps[ky]=executr.bootstrap()
               bootstrap[key]=bootstraps
            else:
                bootstrap[key] = executor.bootstrap()
        return bootstrap