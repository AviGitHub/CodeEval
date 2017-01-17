import sys
import math

debug = False
#debug = True
segment = ''
key_values = ()
key_dict = {}

def build_key_values():
    global key_values
    key_values = []

    for i in range(1,7):
        for j in range(0, int(math.pow(2, i))):
            tmp_append = str_base(j,2).zfill(i)
            if tmp_append.__len__() == i:
                key_values.append(tmp_append)
    for i in range(1,7):
        stoper = ''
        for j in range(0,i):
            stoper+='1';
        if debug:
            print('stoper: ', stoper)
        key_values.remove(stoper)

    if debug:
        for i in range(0, key_values.__len__() -1):
            print( key_values[i])



def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)




def consume_chunk():
    global segment
    global key_dict
    chunk_len = segment[0:3]
    if debug:
        print('chunk_len: ', chunk_len)
    chunk_len_len = int(chunk_len, base=2)
    if debug:
        print(chunk_len_len)
    stopper = ''

    for i in range(0, chunk_len_len):
        stopper += '1'

    segment = segment[3:]
    next_key = segment[0: chunk_len_len]
    while next_key != stopper:
        print(key_dict[next_key], end="")
        segment = segment[chunk_len_len:]
        next_key = segment[0: chunk_len_len]

    segment = segment[chunk_len_len:]


def decrypt(line):
    if debug:
        print('original: ', line)
    first0 = line.index('0')
    first1 = line.index('1')
    start = min(first0, first1)
    key = line[0:start]

    if debug:
        print(key)

    global key_dict
    key_dict = {}
    index = 0
    for char in key:
        key_dict[key_values[index]] = char
        index += 1

    if debug:
        for inner_key, value in key_dict.items():
            print('key: ', inner_key, ' value: ', value)

    global segment
    segment = line[start:line.__len__()]
    if debug:
        print(segment)

    while segment != '000':
        consume_chunk()
    print()


with open(sys.argv[1], 'r') as test_cases:
    build_key_values()
    lines = test_cases.read().splitlines()
    lines = list(filter(None,lines))

    for i in lines:
        decrypt(i)
