from symbol_table import symbols


class AParser:
    def __init__(self, ainstr, var_pointer_incrementer):
        self.instr = ainstr
        # Method from Parser Class
        self.incrementer = var_pointer_incrementer

    def parse_instr(self):
        result = None
        try:
            result = self.parse_int(self.instr)
        except ValueError:
            result = self.parse_symbols(self.instr)

        return result

    def parse_symbols(self, instruction):
        try:
            return symbols[instruction]
        except KeyError:
            # Means custom variable -> Add to a table
            symbols[instruction] = self.incrementer()
            return symbols[instruction]

    def parse_int(self, instruction):
        convert_instr = int(instruction)
        return convert_instr
