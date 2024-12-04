import re


PUZZLE = "https://adventofcode.com/2024/day/3"


def get_mul_sum_from_scrambled_memory(memory: str, part: int) -> int:
    result = 0

    # Regex pattern to match `mul(x,y)` where x and y are numbers
    pattern = r"mul\(\d+,\d+\)"
    if part == 2:
        pattern += r"|do\(\)|don't\(\)"

    mul_enabled = True

    # Find all matches
    valid_multiply_functions = re.findall(pattern, memory)
    for multiply_func in valid_multiply_functions:
        if multiply_func == "do()":
            mul_enabled = True
            continue
        if multiply_func == "don't()":
            mul_enabled = False
            continue
        if not mul_enabled:
            continue
        args = multiply_func.strip("mul(").strip(")")
        num_one, num_two = args.split(",")
        result += int(num_one) * int(num_two)

    return result


def get_results(data: str, part: int):
    return get_mul_sum_from_scrambled_memory(data, part)
