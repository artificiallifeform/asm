def dec_to_bin(num):
    divisor = num
    bits = []

    if num > 0:
        while divisor != 1:
            temp = divisor % 2
            bits.insert(0, str(temp))
            divisor = int((divisor - temp) / 2)
            # pdb.set_trace()
        bits.insert(0, '1')

    for i in range(16 - len(bits)):
        bits.insert(0, '0')

    result = ''.join(bits)
    return result


def hello():
    print('Hello')
# 10 / 2    0
#  5 / 2    1
#  2 / 2    0
#  1 / 2    1
# 10 ->> 1010
