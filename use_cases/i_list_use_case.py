from abc import ABC, abstractmethod


class IListUseCase(ABC):

    @abstractmethod
    def flatten_list(self, list_str: str): pass
