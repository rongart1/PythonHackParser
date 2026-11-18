class SymbolTable:
    def __init__(self):
        self.table = {}
        for i in range(16):
            self.table[f"R{i}"] = i
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
