import pytest

from src.get_vacancies_hh import HH
from src.new_vacancy import Vacancy
from src.vacancies import Vacancies


@pytest.fixture(scope="function")
def vacancy_1():
    return Vacancy(
        "Менеджер по продажам",
        "Москва",
        "Знание английского языка",
        "Организация культуры продажи продукта",
        "от 3 до 5 лет",
        "полная занятость",
        150000,
        200000,
        published_at="12.12.2023 15:20:48",
    )


@pytest.fixture(scope="function")
def vacancy_2():
    return Vacancy(
        "Python разработчик",
        "Москва",
        "знание языка пайтон",
        "анализировать базы данных",
        "от 1 до 3 лет",
        "полная занятость",
        120000,
        140000,
    )


@pytest.fixture
def list_vacancies():
    return [
        {
            "id": 1729,
            "name": "Программист Python",
            "area": "Камышин",
            "salary_from": 10000,
            "salary_to": 15000,
            "requirement": "Знание баз данных SQL и NoSQL. Способность работать в команде.",
            "responsibility": "Проводить код-ревью.",
            "experience": "От 3 до 6 лет",
            "employment": "Полная занятость",
            "published_at": "2024-08-14T15:12:11+0300",
        },
        {
            "id": 320,
            "name": "Trainee/Intern/Junior Python backend developer",
            "area": "Санкт-Петербург",
            "salary_from": 10000,
            "salary_to": 30000,
            "requirement": "Для этого мы ищем начинающего, сообразительного, амбициозного интерна-джуна питониста.",
            "responsibility": "Писать тесты.",
            "experience": "Нет опыта",
            "employment": "Стажировка",
            "published_at": "2024-08-24T20:41:10+0300",
        },
    ]


@pytest.fixture(scope="function")
def hh_vacancies():
    test_hh_vacancies = HH()
    test_hh_vacancies.vacancies = [
        {
            "name": "Vacancy 1",
            "area": {"name": "Moscow"},
            "snippet": {
                "requirement": "Requirements for Vacancy 1",
                "responsibility": "Responsibilities for Vacancy 1",
            },
            "experience": {"name": "No experience"},
            "employment": {"name": "Full-time"},
            "salary": {"from": 1000, "to": 2000},
            "published_at": "2020-01-01",
        },
        {
            "name": "Vacancy 2",
            "area": {"name": "Saint-Petersburg"},
            "snippet": {
                "requirement": "Requirements for Vacancy 2",
                "responsibility": "Responsibilities for Vacancy 2",
            },
            "experience": {"name": "1 year"},
            "employment": {"name": "Part-time"},
            "salary": None,
            "published_at": "2020-01-02",
        },
    ]
    return test_hh_vacancies


@pytest.fixture(scope="function")
def hh_vacancies_2():
    test_hh_vacancies = HH()
    test_vacancies = Vacancies()
    test_hh_vacancies.vacancies = [
        {
            "name": "Vacancy 1",
            "area": {"name": "Moscow"},
            "snippet": {
                "requirement": "Requirements for Vacancy 1",
                "responsibility": "Responsibilities for Vacancy 1",
            },
            "experience": {"name": "No experience"},
            "employment": {"name": "Full-time"},
            "salary": {"from": 1000, "to": 2000},
            "published_at": "2020-01-01",
        },
        {
            "name": "Vacancy 2",
            "area": {"name": "Saint-Petersburg"},
            "snippet": {
                "requirement": "Requirements for Vacancy 2",
                "responsibility": "Responsibilities for Vacancy 2",
            },
            "experience": {"name": "1 year"},
            "employment": {"name": "Part-time"},
            "salary": None,
            "published_at": "2020-01-02",
        },
    ]

    return test_vacancies.cast_to_object_list(test_hh_vacancies)
