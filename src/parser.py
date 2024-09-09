from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def get_vacancies(self, keyword: str) -> None:
        pass
