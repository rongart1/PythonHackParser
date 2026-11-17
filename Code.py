import CinstructionDicts

class Code:
    '''a class used for turning C-instuctions into binary code'''

    def convertDest(dest):
        return CinstructionDicts.DEST_DICT[dest]

    def convertComp(comp):
        return CinstructionDicts.COMP_DICT[comp]

    def comvertJump(jump):
        return CinstructionDicts.JUMP_DICT[jump]




