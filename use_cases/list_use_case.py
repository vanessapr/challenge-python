from json import loads
from use_cases.i_list_use_case import IListUseCase
from use_cases.exceptions import InvalidEntryList
from utils.flatten_list import flatten


class ListUseCase(IListUseCase):
    def __init__(self):
        pass

    def flatten_list(self, list_str: str):
        try:
            return flatten(loads(list_str))
        except Exception as e:
            print(type(e).__name__)
            raise InvalidEntryList()
