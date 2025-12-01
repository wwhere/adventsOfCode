
DAY_DATA = '11a'

def read_lines(filename: str):
    """Reads a file line by line

    Args:
        filename (str): The file name

    Yields:
        str: Next line on the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            yield line.replace('\n', '')

def calculate(v):
    result = []

    str_v = str(v)
    if v == 0:
        result.append(1)
    elif len(str_v) % 2 == 0:
        result.append(int(str_v[0:len(str_v)//2]))
        result.append(int(str_v[len(str_v)//2:]))
    else:
        result.append(v * 2024)

    return result

def solve(values, loops):
    cache = [{} for __ in range(loops+1)]
    solution = 0
    for v in values:
        solution += do_a_pass(cache, v, loops)
    return solution

def do_a_pass(cache, value, loops):
    if value in cache[loops].keys():
        return cache[loops][value]
    
    result = calculate(value)
    if loops == 1:
        cache[loops][value] = len(result)
        return len(result)
    solution = 0
    for r in result:
        solution += do_a_pass(cache, r, loops-1)
    
    cache[loops][value] = solution
    return solution

def process(filename: str) -> int:
    solution = 0
    values = []
    for line in read_lines(filename):
        str_values = line.split()
        values = [int(x) for x in str_values]

    solution = solve(values, 75)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    process(f'd{DAY_DATA}.data')
