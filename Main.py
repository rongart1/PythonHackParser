import Parser
import os

base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, "testFiles", "max", "max.asm")

parser = Parser.Parser(path)

while parser.hasMoreLines():
    sym = parser.getSymbol()
    print(f'{parser.current}: {parser.instruction}    label: {sym}    C-parts: {parser.getCinstuctionParts()}')
    parser.advance()

print(parser.lines)