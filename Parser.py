from enum import Enum
from fileinput import filename
from io import TextIOWrapper

from _typeshed import FileDescriptorOrPath


class InstuctionType(Enum):
    nInstruction = 0
    cInstruction = 1
    lInstuction = 2
    aInstruction = 3


class Parser:
    def __init__(self, fileName: FileDescriptorOrPath) -> None:
        with open(fileName, "r") as f:
            self.file: TextIOWrapper = f
            self.instruction: str = ""

    def hasMoreLines(self) -> bool:
        currentPos = self.file.tell()
        line = self.file.readline()
        self.file.seek(currentPos)
        return len(line) != 0

    def advance(self):
        isInstuction = False
        while not isInstuction:
            line = self.file.readline().strip()
            if not line.startswith("//"):
                self.instruction = line
                isInstuction = True

    def getInstructionType(self):
        if not self.instruction:
            return
