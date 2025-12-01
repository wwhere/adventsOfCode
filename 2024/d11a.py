
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

def do_a_pass(values):
    result = []

    for v in values:
        str_v = str(v)
        if v == 0:
            result.append(1)
        elif len(str_v) % 2 == 0:
            result.append(int(str_v[0:len(str_v)//2]))
            result.append(int(str_v[len(str_v)//2:]))
        else:
            result.append(v * 2024)

    return result

def process(filename: str) -> int:
    solution = 0
    values = []
    for line in read_lines(filename):
        str_values = line.split()
        values = [int(x) for x in str_values]

    for __ in range(25):
        values = do_a_pass(values)
    solution = len(values)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process(f'd{DAY_DATA}.ex.data') == 55312
    process(f'd{DAY_DATA}.data')
