import re

# Add both NULL for DEST and COMP parts

match_o = re.compile(
    r'''^([A-Z]{0,3})(=[^;\n]*|0|[A-Z])(;[A-Z]{0,3}|;|)''', re.VERBOSE)


def separator(command):
    result = []
    groups = match_o.findall(command)
    for group in groups[0]:
        if group == '':
            result.append(None)
        elif group.startswith('='):
            result.append(group.replace('=', ''))
        elif group.startswith(';'):
            result.append(group.replace(';', ''))
        else:
            result.append(group)
    return result


separator('D=M')
separator('D=D-M')
separator('AMD=D-M;JGT')
separator('D;JGT')
separator('M=D')
separator('0;JMP')
