from enum import Enum
from io import TextIOWrapper


class InstuctionType(Enum):
    nInstruction = 0
    cInstruction = 1
    lInstuction = 2
    aInstruction = 3


class Parser:

    def __init__(self, fileName) -> None:
        with open(fileName, "r") as f:
            self.lines = f.readlines()
            self.current = 0
            self._cleanWhiteSpace_()
            self.instruction: str = self.lines[0]


    def hasMoreLines(self) -> bool:
        return self.current < len(self.lines)-1

    def getInstructionType(self):
        return self._getInstructionType_(self.instruction)

    def _cleanWhiteSpace_(self):
        for line in self.lines.copy():
            trimed = line.strip()
            instructionType = self._getInstructionType_(trimed)
            #removing filler lines like comments and empty
            if(instructionType == InstuctionType.nInstruction):
                self.lines.remove(line)


    def advance(self):
        self.current += 1
        self.instruction = self.lines[self.current]



    def _getInstructionType_(self,instruction:str):
        if not instruction or instruction.__contains__('/'):
            return InstuctionType.nInstruction
        if instruction.startswith('(') and instruction.endswith(')'):
            return InstuctionType.lInstuction
        if instruction.startswith('@'):
            return InstuctionType.aInstruction
        return InstuctionType.cInstruction
