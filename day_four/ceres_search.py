from typing import List


def get_vertical_rows(data: str) -> List[str]:
    rows = data.split("\n")
    vertical_rows: dict[int: str] = {}
    for i, row in enumerate(rows):
        for j, letter in enumerate(row):
            if vertical_rows.get(j):
                vertical_rows[j] += letter
                continue
            vertical_rows[j] = letter
    return list(vertical_rows.values())


def get_diagonal_rows(data: str) -> List[str]:
    rows = data.split("\n")
    vertical_rows: dict[int: str] = {}
    for i, row in enumerate(rows):
        for j, letter in enumerate(row):
            if vertical_rows.get(j):
                vertical_rows[j] += letter
                continue
            vertical_rows[j] = letter
    return list(vertical_rows.values())


def get_xmas_count(data: str) -> int:
    result = 0

    xmas = "xmas"
    xmas_backwards = "samx"

    horizontal_rows = data.split("\n")
    for horizontal_row in horizontal_rows:
        if xmas or xmas_backwards in horizontal_row:
            result += 1

    vertical_rows: List[str] = get_vertical_rows(data)
    for vertical_row in vertical_rows:
        if xmas or xmas_backwards in vertical_row:
            result += 1

    return result


if __name__ == "__main__":
    x = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

    x = get_xmas_count(x)
    pass
