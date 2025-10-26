def STRIP_SPACE(raw: str) -> str:
    return raw.replace(' ', '')

def BYTE(number: str) -> list[int]:
    number = STRIP_SPACE(number)
    return [int(char) for char in number]

def TO_DEC(binary: str) -> int:
    binary = STRIP_SPACE(binary)
    # return sum(int(bit) * 2 ** i for i, bit in enumerate(reversed(binary)))
    output = 0
    for i, bit in enumerate(reversed(binary)):
        output += int(bit) * 2 ** i
    return output

def list_to_tuple(ls: list) -> tuple:
    new_arguments = ()
    for i, arg in enumerate(ls):
        ls[i] = tuple(arg)
        new_arguments = tuple(new_arguments + ls[i])
    return new_arguments

def tuple_to_int(tup: tuple) -> int:
    return "".join(map(str, tup))

# Альтернативные варианты которые ломали мою концепцию, 
# и использовали слишком высокий уровень абстракции: 

# def AND(a, b):
#     return 1 if a == 1 and b == 1 else 0

# def OR(a, b):
#     return 1 if a == 1 or b == 1 else 0

# def NOT(a):
#     return 1 if a == 0 else 0

# def XOR(a, b):
#     return 1 if a != b else 0

# def NAND(a, b):
#     return NOT(AND(a, b))