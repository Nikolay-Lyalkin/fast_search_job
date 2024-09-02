from abc import ABC, abstractmethod

from src.new_vacancy import Vacancy


class ParentSaveFile(ABC):

    @abstractmethod
    def save_vacancies(self, vacancies: list[dict]) -> None:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, del_vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def open_file(self) -> None:
        pass
