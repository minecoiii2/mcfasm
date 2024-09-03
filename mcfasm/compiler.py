import re
import lexer

scores = []
storages = []

def CompileDumps(contents: str):
    contents = re.sub(r'#.*\n', '\n', contents)

    lines = contents.split("\n")

    for line in lines:
        lexer.read_line(line)