import pytest
from project import check_range, calculate_closest, repeated_numbers


def test_check_range():
    assert check_range(50) == True
    assert check_range(0) == True
    assert check_range(100) == True
    assert check_range(-50) == False
    assert check_range(150) == False


def test_type_error():
    with pytest.raises(TypeError):
        check_range("cat")


def test_calculate_closest():
    assert calculate_closest([32, 40, 30, 33, 29], 26.24) == [29, 30, 32, 33, 40]
    assert calculate_closest([7, 11, 3, 7, 5], 5.28) == [5, 7, 7, 3, 11]
    assert calculate_closest([7, 12, 17, 12], 9.6) == [12, 12, 7, 17]


def test_repeated_numbers():
    assert repeated_numbers([7, 12, 17, 12]) == [12]
    assert repeated_numbers([7, 12, 7, 12]) == [7, 12]
    assert repeated_numbers([1, 1]) == [1]