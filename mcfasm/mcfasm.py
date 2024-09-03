import compiler

class Project():
    def __init__(self, main_fp: str):
        self.files = [main_fp]
        return self
    
    def compile(self):
        for file in self.files:
            with open(file, "r") as read:
                compiler.CompileDumps(read.read())