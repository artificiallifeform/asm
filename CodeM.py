import tables


class Code:
    def __init__(self, commands):
        self.code = '111'  # self.code[3] = a bit. 1 when M
        self.commands = commands

    def c_to_bin(self):
        if self.commands[1]:
            if "M" in self.commands[1]:
                self.code += '1'
            else:
                self.code += '0'
        else:
            self.code += '0'

        comp_bin = self.comp(self.commands)
        dest_bin = self.dest(self.commands)
        jump_bin = self.jump(self.commands)

        self.code += comp_bin
        self.code += dest_bin
        self.code += jump_bin

    def get_code(self):
        self.c_to_bin()
        return self.code

    def dest(self, coms):
        dest_com = ''
        if coms[0]:
            dest_com = coms[0]
        else:
            dest_com = "NULL"
        return tables.destT[dest_com]

    def comp(self, coms):
        comp_com = coms[1]
        return tables.compT[comp_com]

    def jump(self, coms):
        jump_com = ''
        if coms[2]:
            jump_com = coms[2]
        else:
            jump_com = "NULL"
        return tables.jumpT[jump_com]
