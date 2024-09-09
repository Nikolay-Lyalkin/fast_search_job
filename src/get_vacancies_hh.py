from typing import Any

import requests

from src.parser import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter

    """

    def __init__(self) -> None:
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    def get_vacancies(self, keyword: str) -> Any:
        """Метод для получения вакансий с платформы HH, принимает на слово по которому осуществляется поиск"""
        self.params["text"] = keyword
        while self.params.get("page") != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            result = response.status_code
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.params["page"] += 1
        return self.vacancies
