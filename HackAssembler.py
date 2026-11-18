import Code
from Parser import InstuctionType, Parser
from SymbolTable import SymbolTable


class HackAssembler:
    def __init__(self, fileName: str):
        self.fileName = fileName
        self.parser: Parser = Parser(fileName)
        self.symbolTable = SymbolTable()
        self.outPutLines = []

    def assemble(self):
        """assembles the file held by the class into a new file holding the binary code"""
        ended = False

        instructionCount = 0
        while not ended:
            if self.parser.instructionType != InstuctionType.lInstuction:
                instructionCount += 1
            # if the instruction is a label dont add it to output but translate to line number instructionCount
            else:
                self.symbolTable.getAddress(
                    self.parser.getSymbol(), str(instructionCount)
                )

            if self.parser.hasMoreLines():
                self.parser.advance()
            else:
                ended = True

        self.parser.reset()
        ended = False
        while not ended:
            # if current line is c-instuction convert it to binray and append to output
            if self.parser.instructionType == InstuctionType.cInstruction:
                destBin = Code.convertDest(self.parser.getDest())
                compBin = Code.convertComp(self.parser.getComp())
                jumpBin = Code.convertJump(self.parser.getJump())
                fullBinary = "111" + compBin + destBin + jumpBin
                self.outPutLines.append(fullBinary)

            if self.parser.instructionType == InstuctionType.aInstruction:
                address = 0
                if self.parser.getSymbol():
                    address = int(self.symbolTable.getAddress(self.parser.getSymbol()))
                else:
                    address = int(self.parser.instruction[1:])
                binaryAddress = format(address, "015b")
                fullBinary = "0" + binaryAddress
                self.outPutLines.append(fullBinary)
            if self.parser.hasMoreLines():
                self.parser.advance()
            else:
                ended = True

    def emitToFile(self):
        name = self.fileName.replace(".asm", ".hack")
        with open(name, "x") as file:
            file.writelines(line + "\n" for line in self.outPutLines)
