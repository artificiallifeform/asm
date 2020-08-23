from symbol_table import symbols


class SParser:
    def __init__(self, ainstr):
        self.instr = ainstr

    def parse_instr(self):
        result = None
        try:
            result = self.parse_int(self.instr)
        except ValueError:
            result = self.parse_symbols(self.instr)

        return result

    def parse_symbols(self, instruction):
        return symbols[instruction]

    def parse_int(self, instruction):
        convert_instr = int(instruction)
        return convert_instr
