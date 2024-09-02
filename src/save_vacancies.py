import json
import os
from typing import Any

from src.new_vacancy import Vacancy
from src.parent_save_file import ParentSaveFile
from src.vacancies import Vacancies


class SaveJSON(ParentSaveFile):
    """Класс для работы с файлом JSON в котором хранится информация о вакансиях"""

    def __init__(self, path_file: str = "../data/vacancies.json") -> None:
        self.path_file = path_file

    def save_vacancies(self, vacancies: Vacancies):
        """Метод сохраняет вакансии в JSON файл"""
        list_vacancies = []
        for vacancy in vacancies:
            list_vacancies.append(vacancy)
        full_path = os.path.abspath(self.path_file)
        try:
            with open(full_path, "w", encoding="utf-8") as f_obj:
                json.dump(list_vacancies, f_obj, ensure_ascii=False)
        except FileNotFoundError:
            print("Файл не найден")

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Метод для добавления новой вакансии в файл"""
        full_path = os.path.abspath(self.path_file)
        with open(full_path, "r", encoding="utf-8") as f_obj:
            vacancies_from_file = json.load(f_obj)
            if vacancy.__dict__ in vacancies_from_file:
                print("Данная вакансия уже существует")
            else:
                vacancies_from_file.append(vacancy.__dict__)
                with open(full_path, "w", encoding="utf-8") as f_obj:
                    json.dump(vacancies_from_file, f_obj, ensure_ascii=False)

    def delete_vacancy(self, del_vacancy: Vacancy) -> None:
        """Метод для удаления вакансии из файла"""
        full_path = os.path.abspath(self.path_file)
        with open(full_path, "r", encoding="utf-8") as f_obj:
            dict_vacancies = json.load(f_obj)
        for i in range(0, len(dict_vacancies)):
            if dict_vacancies[i]["id"] == del_vacancy.id:
                del dict_vacancies[i]
        with open(full_path, "w", encoding="utf-8") as f_obj:
            json.dump(dict_vacancies, f_obj, ensure_ascii=False)

    def open_file(self) -> Any:
        """Метод для чтения вакансий из JSON файла"""
        full_path = os.path.abspath(self.path_file)
        with open(full_path, "r", encoding="utf-8") as f_obj:
            result = json.load(f_obj)
        return result
