import re

from dec_to_bin import dec_to_bin
from parse_c_code import separator
from CodeM import Code
from AInstrParser import AParser


class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.commands = []
        self.currentC = 0
        self.commandType = None

        # Store custom variable RAM addresses here (start from 16)
        self.var_pointer = 16

    def read_program(self):
        with open(self.filename) as file:
            for line in file.readlines():
                if line.startswith('//') or line == '\n':
                    continue
                self.commands.append(line.replace('\n', ''))

    def parse_commands(self, result_filename):
        for command in self.commands:
            if (command.startswith('@')):
                self.commandType = 'A_COMMAND'
                aInstr = AParser(command.replace("@", ""),
                                 self.increment_var_pointer)
                aInstValue = aInstr.parse_instr()
                aBinary = dec_to_bin(aInstValue)
                self.write_to_file(aBinary, result_filename)
            else:
                self.commandType = 'C_COMMAND'
                cMnemonics = separator(command)
                cBinary = Code(cMnemonics)
                self.write_to_file(cBinary.get_code(), result_filename)

    def write_to_file(self, instr, result_filename):
        with open(result_filename, 'a') as file:
            file.write(instr + '\n')

    def increment_var_pointer(self):
        temp = self.var_pointer
        self.var_pointer += 1
        return temp


parsed_asm = Parser('test.asm')
parsed_asm.read_program()
parsed_asm.parse_commands('test.hack')
