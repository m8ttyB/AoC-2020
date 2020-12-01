import pytest

import day_01 as aoc

sum_of_two_testdata = [
    (3, [0,3], (0,3)),
    (11, [0,1,2,3,4,5,6], (5,6)),
    (20, [0,1], -1)
]
@pytest.mark.parametrize("search_for,num_list,expected", sum_of_two_testdata)
def test_sum_of_two_numbers(search_for, num_list, expected):
    assert aoc.find_sum_two_numbers(search_for, num_list) == expected


sum_of_three_testdata = [
    (3, [0,1,2], (0,1,2)),
    (11, [0,1,2,3,4,5,20], (2,4,5)),
    (-1, [0,1,2,20], -1),
]
@pytest.mark.parametrize("search_for,num_list,expected", sum_of_three_testdata)
def test_sum_of_three_numbers(search_for, num_list, expected):
    assert aoc.find_sum_three_numbers(search_for, num_list) == expected
