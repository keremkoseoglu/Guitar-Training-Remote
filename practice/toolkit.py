import inspect, practice, sys
import os

class Toolkit:

    _MODULE_EXTENSIONS = ('.py', '.pyc', '.pyo')

    def get_all_practices(self):
        output = []

        modules = self.get_all_modules()

        for m in modules:
            module_name = "practice." + m
            module = __import__(module_name, fromlist=[""])

            for name, obj in inspect.getmembers(module, inspect.isclass):
                if name != "AbstractPractice":
                    output.append(obj)

        return output

    def get_all_modules(self):
        output = []
        path = os.path.join(os.getcwd() + "/practice")
        files = [f for f in os.listdir(path)]
        for f in files:
            if f[:2] != "__" and f[:8] != "abstract" and f[:7] != "toolkit":
                fname = os.path.splitext(f)[0]
                output.append(fname)
        return output