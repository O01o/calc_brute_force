from itertools import permutations
import numpy as np

def operator_number_calc(num1: int, num2: int, operator_num: int) -> float:
    assert operator_num in [0, 1, 2, 3]
    try:
        if operator_num == 0: return num1 + num2
        if operator_num == 1: return num1 - num2
        if operator_num == 2: return num1 * num2
        if operator_num == 3: return num1 / num2
    except ZeroDivisionError: return 0

def print_formula(num: int, bracket_array: tuple, operator_array: str) -> str:
    formula: str = ""
    formula += f"{num}"
    for i, operator_str in enumerate(operator_array):
        operator_num = int(operator_str)
        assert operator_num in [0, 1, 2, 3]
        if operator_num == 0: formula += "+"
        if operator_num == 1: formula += "-"
        if operator_num == 2: formula += "*"
        if operator_num == 3: formula += "÷"
        formula += f"{num}"
    return formula

def get_hit_number(fnum: float) -> int:
    if fnum % 1 > 1e-02: return 0
    if int(fnum) == 1: return 1
    elif int(fnum) == 2: return 2
    elif int(fnum) == 3: return 3
    elif int(fnum) == 4: return 4
    elif int(fnum) == 5: return 5
    elif int(fnum) == 6: return 6
    elif int(fnum) == 7: return 7
    elif int(fnum) == 8: return 8
    elif int(fnum) == 9: return 9
    else: return 0

def bracket_order_calc(num: int, clause: int, bracket_tuple: tuple, operator_array: str):
    num_array: list[int] = [num,]*clause
    bracket_list: list[int] = list(bracket_tuple)
    operator_list: list[str] = [ s for s in operator_array ]
    # print(operator_array, num_array)
    while bracket_list:
        bracket = bracket_list.pop(0)
        operator_num = int(operator_list.pop(bracket))
        for i in range(len(bracket_list)): 
            if bracket_list[i] > bracket: bracket_list[i] -= 1
        num_array[bracket] = operator_number_calc(num1=num_array[bracket], num2=num_array[bracket+1], operator_num=operator_num)
        num_array.pop(bracket+1)
        # print(bracket, bracket_list, operator_num, num_array)
    return num_array[0]

if __name__ == '__main__':
    print("num?", end=" ")
    num = int(input()) #4
    print("clause?", end=" ")
    print()
    clause = int(input()) #4
    operators = clause - 1
    bracket_array_pattern: list[tuple] = list(permutations([ i for i in range(operators) ]))
    operator_array_pattern: list[str] = [ np.base_repr(i, 4, operators)[-operators:] for i in range(4**operators) ]
    # print(bracket_array_pattern, operator_array_pattern)
    
    hit_number_formula_list_list: list[list[str]] = [[] for i in range(1, 10)]
    # print(hit_number_formula_list_list)

    for bracket_array in bracket_array_pattern:
        for operator_array in operator_array_pattern:
            value = bracket_order_calc(num, clause, bracket_array, operator_array)
            hit_number = get_hit_number(value)
            if hit_number != 0:
                hit_number_formula_list_list[hit_number-1].append(f"{print_formula(num, bracket_array, operator_array)}, {bracket_array}")
                # print(print_formula(num, bracket_array, operator_array), bracket_array, hit_number)

    for i, hit_number_formula_list in enumerate(hit_number_formula_list_list):
        number = i + 1
        print(number)
        for hit_number_formula in hit_number_formula_list:
            print(hit_number_formula)
        print()