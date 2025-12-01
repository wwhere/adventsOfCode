"""Advent of Code specific utilities"""
from aoc_tools import read_lines
from typing import NamedTuple
from collections import defaultdict
from functools import cache


class SellerNumber(NamedTuple):
    price_change: int
    bananas: int


class Seller(NamedTuple):
    last_secret_number: int
    buy_orders: defaultdict


@cache
def calculate_secret_number(x: int):
    x = (x ^ (x * 64)) % 16777216
    x = (x ^ (x // 32)) % 16777216
    return (x ^ (x * 2048)) % 16777216


@cache
def get_secret_number(start_number: int, iterations: int) -> Seller:
    x = start_number
    price_changes: list[SellerNumber] = []
    used_keys: list[str] = []
    buy_orders = defaultdict(lambda: 0)
    last_price = 0
    for i in range(iterations):
        x = calculate_secret_number(x)
        price = int(str(x)[-1:])
        if i > 0:
            price_changes.append(SellerNumber(price_change=price-last_price, bananas=price))
        if i > 3:
            key = ','.join(str(price_changes[x].price_change) for x in range(i-4, i))
            if key not in used_keys:
                buy_orders[key] += price_changes[i-1].bananas
                used_keys.append(key)
        last_price = price
    return Seller(last_secret_number=x, buy_orders=buy_orders)


def get_sum_of_last_secret_numbers(filename: str, iterations: int) -> int:
    solution = 0
    for line in read_lines(filename):
        secret_number, __ = get_secret_number(int(line), iterations)
        solution += secret_number

    print(f'{filename}: {solution}')
    return solution


def get_most_buyable_bananas(filename: str, iterations: int) -> int:
    buy_orders = defaultdict(lambda: 0)
    for line in read_lines(filename):
        __, seller_buy_orders = get_secret_number(int(line), iterations)
        for key, value in seller_buy_orders.items():
            buy_orders[key] += value

    best_key = ''
    best_value = 0
    for key, value in buy_orders.items():
        if best_key == '' or value > best_value:
            best_key, best_value = key, value

    print(f'{filename}: {best_key} --- {best_value}')
    return best_value


def part_1() -> None:
    assert get_sum_of_last_secret_numbers('d22.1.data', 2000) == 37327623
    get_sum_of_last_secret_numbers('d22.2.data', 2000)


def part_2() -> None:
    assert get_most_buyable_bananas('d22.3.data', 2000) == 23
    get_most_buyable_bananas('d22.2.data', 2000)


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
