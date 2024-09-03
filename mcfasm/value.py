import interpreter
import compiler
import var
from typing import Union, Literal

operations = [
    "+", "-", "%", "/", "*", ">", "<"
]

# int|float|short|long|double|byte

def solve_two_products(rhs: str, lhs: str):
    pass

def get_type(hs: str) -> Literal["int", "string", "storage", "float", "null"]:
    if hs.find('"') >= 0: return 'string'
    
    try:
        result = int(hs)
    except:
        result = None

    if result != None: return 'int'

    try:
        result = int(hs)
    except:
        result = None

    if result != None: return 'float'

    try:
        result = compiler.storages[hs]
    except:
        result = None

    if result != None: return 'storage'
    return 'null'

def resolve_two(lhs: str, rhs: str, op: str):
    lhs_t = get_type(lhs)
    rhs_t = get_type(rhs)

    lhs_obj = {}

def find_nearest_op(eq: str, start_index: int=None) -> Union[int, str]|int:
    smallest = 999
    smallest_op = None

    for op in operations:
        found = eq.find(op, start_index)

        if found >= 0:
            smallest = found
            smallest_op = op

    if smallest_op == None: return -1

    return smallest, smallest_op


def solve(eq: str):
    eq.replace(" ", "")

    operations_list = []
    last_index = 0

    while True:
        last_index, op = find_nearest_op(eq, last_index)

        if last_index == -1:
            break

        operations_list.append({
            'index': last_index,
            'op': op,
        })

    if len(operations_list) == 0: return

    previous_index = 0
    for i, op in enumerate(operations_list):
        try:
            next_op = operations_list[i + 1]
        except:
            next_op = {'index': len(eq)}

        lhs = eq[previous_index:op["index"]]
        rhs = eq[op["index"] + 1:next_op["index"]]

        r = resolve_two(lhs, rhs)

    