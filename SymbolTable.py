class SymbolTable:
    def __init__(self):
        self.table = {}
        for i in range(16):
            self.table[f"R{i}"] = i
        self.table["SP"] = 0
        self.table["LCL"] = 1
        self.table["ARG"] = 2
        self.table["THIS"] = 3
        self.table["THAT"] = 4
        self.table["SCREEN"] = 16384
        self.table["KBD"] = 24576
        self.nextAddress = 16

    def getAddress(self, sym: str, value=""):
        """gets the address of the given symbol, if the given symbol is new give it a new adress and store it in the table"""
        if sym in self.table:
            return self.table[sym]
        if not value:
            self.table[sym] = self.nextAddress
            self.nextAddress += 1
        else:
            self.table[sym] = value
        return self.table[sym]
