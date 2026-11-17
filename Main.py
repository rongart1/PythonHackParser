import Parser
import os

base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, "testFiles", "add", "Add.asm")

parser = Parser.Parser(path)

while parser.hasMoreLines():
    print(parser.getInstructionType())
    parser.advance()

print(parser.getInstructionType())
