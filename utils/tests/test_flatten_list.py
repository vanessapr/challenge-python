import pytest
from utils.flatten_list import flatten


def test_flatten_should_raise_error_if_entry_is_not_list():
    with pytest.raises(TypeError):
        flatten('This is string')


def test_flatten_should_return_same_list_if_entry_is_simple_list():
    assert [1, 2, 3, 4] == flatten([1, 2, 3, 4])


def test_flatten_should_return_flatten_list_if_entry_is_nested_list():
    assert [1, 2, 3, 3, 4, 5] == flatten([1, 2, 3, [3, 4, [5]]])
