from src.user_func import filter_vacancies, get_top_salary, get_vacancies_by_salary


def test_get_top_salary(list_vacancies):
    """Тест функции получения топ N зарплат"""
    assert get_top_salary(list_vacancies, 1) == [
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
        }
    ]


def test_filter_vacancies(list_vacancies):
    """Тест функции фильтра вакансий по определённому слову"""
    assert filter_vacancies(list_vacancies, "Junior") == [
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
        }
    ]


def test_get_vacancies_by_salary(list_vacancies):
    """Тест функции фильтра вакансий по зарплате"""
    assert get_vacancies_by_salary(list_vacancies, 25000) == [
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
        }
    ]
