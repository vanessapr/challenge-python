from injector import Binder
from use_cases.i_list_use_case import IListUseCase
from use_cases.list_use_case import ListUseCase


def configure_use_case_binding(binder: Binder) -> Binder:
    binder.bind(IListUseCase, ListUseCase)
    return binder
