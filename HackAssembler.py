import os

import Code
from Parser import InstuctionType, Parser
from SymbolTable import SymbolTable


class HackAssembler:
    def __init__(self, fileName: str):
        self.fileName = fileName
        # building path
        self.base = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(self.base, *fileName.split("/"))

        self.parser: Parser = Parser(path)
        self.symbolTable = SymbolTable()
        self.outPutLines = []

    def assemble(self):
        """assembles the file held by the class into a new file holding the binary code"""
        ended = False
        while not ended:
            # if current line is c-instuction convert it to binray and append to output
            if self.parser.instructionType == InstuctionType.cInstruction:
                destBin = Code.convertDest(self.parser.getDest())
                compBin = Code.convertComp(self.parser.getComp())
                jumpBin = Code.convertJump(self.parser.getJump())
                fullBinary = "111" + compBin + destBin + jumpBin
                self.outPutLines.append(fullBinary)

            # if the instruction is a label dont add it to output but translate to line number of next instruciton to be translated
            if self.parser.instructionType == InstuctionType.lInstuction:
                self.symbolTable.getAddress(
                    self.parser.getSymbol(), str(len(self.outPutLines))
                )

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
        name = self.fileName.split("/")
        name = name[len(name) - 1]
        name = name.replace(".asm", ".hack")
        path = os.path.join(self.base, name)
        with open(path, "x") as file:
            file.writelines(line + "\n" for line in self.outPutLines)
