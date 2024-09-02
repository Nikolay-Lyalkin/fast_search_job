from src.vacancies import Vacancies


def test_cast_to_object_list(hh_vacancies):
    """Тест инициализации класса Vacancies"""
    vacancies = Vacancies()
    assert vacancies.cast_to_object_list(hh_vacancies) == [
        {
            "id": 4,
            "name": "Vacancy 1",
            "area": "Moscow",
            "salary_from": 1000,
            "salary_to": 2000,
            "requirement": "Requirements for Vacancy 1",
            "responsibility": "Responsibilities for Vacancy 1",
            "experience": "No experience",
            "employment": "Full-time",
            "published_at": "2020-01-01",
        },
        {
            "id": 5,
            "name": "Vacancy 2",
            "area": "Saint-Petersburg",
            "salary_from": 0,
            "salary_to": 0,
            "requirement": "Requirements for Vacancy 2",
            "responsibility": "Responsibilities for Vacancy 2",
            "experience": "1 year",
            "employment": "Part-time",
            "published_at": "2020-01-02",
        },
    ]
