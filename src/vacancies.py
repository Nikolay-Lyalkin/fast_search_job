from src.get_vacancies_hh import HH
from src.new_vacancy import Vacancy


class Vacancies:
    """Класс для работы с массивом вакансий, принимает на вход данные от класса HH, возвращает список словарей"""

    def __init__(self) -> None:
        self.object_list = []

    def cast_to_object_list(self, vacancies: HH) -> list[dict]:
        """Метод для преобразования данных из класса НН в экземпляры класса Vacancy"""
        for vacancy in vacancies.vacancies:
            if vacancy["salary"]:
                self.object_list.append(
                    Vacancy(
                        vacancy["name"],
                        vacancy["area"]["name"],
                        vacancy["snippet"]["requirement"],
                        vacancy["snippet"]["responsibility"],
                        vacancy["experience"]["name"],
                        vacancy["employment"]["name"],
                        vacancy["salary"]["from"],
                        vacancy["salary"]["to"],
                        vacancy["published_at"],
                    ).__dict__
                )
            else:
                self.object_list.append(
                    Vacancy(
                        vacancy["name"],
                        vacancy["area"]["name"],
                        vacancy["snippet"]["requirement"],
                        vacancy["snippet"]["responsibility"],
                        vacancy["experience"]["name"],
                        vacancy["employment"]["name"],
                        None,
                        None,
                        vacancy["published_at"],
                    ).__dict__
                )
        return self.object_list
