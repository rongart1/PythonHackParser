import sys

from HackAssembler import HackAssembler

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) != 1:
        print("Usage: python Main.py <file.asm>")
        sys.exit(1)

    assembler = HackAssembler(args[0])

    assembler.assemble()
    assembler.emitToFile()
