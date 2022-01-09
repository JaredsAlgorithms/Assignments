#!/usr/bin/env python3.9

import random
import math

import itertools

"""
Question 1
"""


class OfflineSkiSolution:
    def solution(self, rental_price: int,
                 purchase_price: int, days: int) -> bool:

        return (purchase_price >= (rental_price * days))

    def tests(self):
        assert(self.solution(100, 50, 2) == True)
        assert(self.solution(100, 50, 1) == False)


class ReverseListSolution:
    def solution(container: list) -> list:
        end = len(container) - 1
        for x, _ in enumerate(container):
            if x < end:
                container[x], container[end] = container[end], container[x]
                end -= 1
        return container

    def tests(self, iterations: int, bound: int = 323) -> None:

        for _ in range(0, iterations):
            candidate = [random.randint(0, bound) for _ in range(0, 100)]
            assert(candidate[::-1] == self.solution(candidate))


class PythagoreanTripleSolution:

    def solution(self, integers: tuple[int, int]) -> list[tuple[int, int, int]]:
        a, b = integers  # a is lower bound and b is upper bound
        if not(isinstance(a, int)
               and isinstance(b, int)
               and a < b):
            raise ValueError(
                f'[ERROR] Expected integers for `a` ({a}) and `b` ({b}), where a < b')
        candidates = [_ for _ in range(a, b+1)]
        """
        Given a = 1 and b = 4
        - (1, 2, 3)
        - (2, 3, 4)
        are all valid combinations
        """

        return [candidate for candidate in
                itertools.combinations(candidates, 3) if self.validator(candidate)]

    def validator(self, container: list[int, int, int]) -> bool:
        x, y, z = container  # raise ValueError if container len != 3
        # x ^ 2 + y ^ 2 = z ^ 2
        # where x, y and z are perfect squares
        return z == math.sqrt(x ** 2 + y ** 2) and x <= y <= z


def sum_exclude(container: list[int], index: int):
    value = 0
    for x in container:
        if(x != index):
            value += x
    return value


def missing_integer(container: list[int], index=None) -> int:
    summation_original = sum(container)  # O(n)
    random_index = random.randint(
        0, len(container) - 1) if index is None else index  # O(1)
    element_missing = container[random_index]  # O(1)
    summation_new = sum_exclude(container, element_missing)
    return abs(summation_new - summation_original)


def test_missing_integer():
    iterations = 100
    container = [_ for _ in range(0, iterations)]
    for x in range(0,  len(container)):
        assert(missing_integer(container, index=x) == container[x])
    for _ in range(0, iterations):
        random_index = random.randint(0, len(container) - 1)
        assert(missing_integer(container, index=random_index)
               == container[random_index])


test_missing_integer()
