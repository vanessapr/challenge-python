import pytest
from use_cases.list_use_case import ListUseCase
from use_cases.exceptions import InvalidEntryList


def test_list_use_case_should_raise_error_if_entry_invalid():
    list_use_case = ListUseCase()
    with pytest.raises(InvalidEntryList):
        list_use_case.flatten_list('1, 2, [3, 4, [5, 6], 7], 8')


def test_list_use_case_should_return_a_flatten_list_if_entry_valid():
    list_use_case = ListUseCase()
    result = list_use_case.flatten_list('[1, 2, [3, 4, [5, 6], 7], 8]')
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]