from enum import Enum


class InstuctionType(Enum):
    nInstruction = 0
    cInstruction = 1
    lInstuction = 2
    aInstruction = 3


class Parser:
    def __init__(self, fileName) -> None:
        with open(fileName, "r") as f:
            self.lines = f.readlines()

            # remove all \n in lines
            self.lines = [line.replace("\n", "").strip() for line in self.lines]
            self.current = -1
            self._cleanWhiteSpace_()
            self.advance()

    def hasMoreLines(self) -> bool:
        return self.current < len(self.lines) - 1

    def reset(self):
        """resets the instruction to instruction 0"""
        self.current = -1
        self.advance()

    def _getInstructionType_(self, instruction: str):
        if not instruction or instruction.__contains__("/"):
            return InstuctionType.nInstruction
        if instruction.startswith("(") and instruction.endswith(")"):
            return InstuctionType.lInstuction
        if instruction.startswith("@"):
            return InstuctionType.aInstruction
        return InstuctionType.cInstruction

    def _cleanWhiteSpace_(self):
        for line in self.lines.copy():
            trimed = line.strip()
            instructionType = self._getInstructionType_(trimed)
            # removing filler lines like comments and empty
            if instructionType == InstuctionType.nInstruction:
                self.lines.remove(line)

    def advance(self):
        self.current += 1
        self.instruction = self.lines[self.current]
        self.instructionType = self._getInstructionType_(self.instruction)

    def getSymbol(self):
        """returns the symbol of the istrcuction if its a label or A-instruction with a symbol
        other wise return empty string"""
        # if its a (lable) remove perentcies
        if self.instructionType == InstuctionType.lInstuction:
            sym = self.instruction.removeprefix("(")
            sym = sym.removesuffix(")")
            return sym
        # if its an A-instruction @x.. we check if the x is a not a number hance a symbol
        elif (
            self.instructionType == InstuctionType.aInstruction
            and not self.instruction[1].isnumeric()
        ):
            return self.instruction.removeprefix("@")
        return ""

    def getDest(self):
        """if instruction at possition self.current is a C-intruction return the destination part otherwise empty string"""
        # if there is no destination return nothing or not C-instruction
        if (
            not self.instruction.__contains__("=")
            or self.instructionType != InstuctionType.cInstruction
        ):
            return ""
        destEndInd = self.instruction.find("=")
        return self.instruction[:destEndInd]

    def getComp(self):
        """if current instruction is a C-instruction retun its computation part otherwise empty string"""

        if self.instructionType != InstuctionType.cInstruction:
            return ""

        comp = self.instruction
        # removing dest part if has
        destEndInd = self.instruction.find("=")
        if destEndInd != -1:
            comp = self.instruction[destEndInd + 1 :]

        # removing jump part if there is
        compEndInd = self.instruction.find(";")
        if compEndInd != -1:
            comp = comp[:compEndInd]

        return comp

    def getJump(self):
        """if current instruction is C-instuction return the jump part, otherwise empty string"""
        if self.instructionType != InstuctionType.cInstruction:
            return ""
        jumpStartInd = self.instruction.find(";")
        if jumpStartInd == -1:
            return ""
        return self.instruction[jumpStartInd + 1 :]

    def getCinstuctionParts(self):
        return [self.getDest(), self.getComp(), self.getJump()]
