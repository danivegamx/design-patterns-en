"""
 Design Patterns v1

 Design -> Structure -> Facade
 Python
 Daniel Vega Ceja, 2015
"""

# The layers, are representations of compilation process.

# Define Scanner.
class Scanner:
    def __init__(self):
        self.name = "Scanner"

# Define Parser.
class Parser:
    def __init__(self):
        self.name = "Parser"

# Define Compiler. Representation for Scanner and Parser.
class Compiler:
    def __init__(self):
        self.name = "Compiler"
        self.scanner = Scanner()
        self.parser = Parser()

    def compile(self):
        print("Compiling...")
        print("%s has been initialized..." % self.scanner.name)
        print("%s has been initialized..." % self.parser.name)

if __name__ == "__main__":
    compiler = Compiler()
    compiler.compile()
