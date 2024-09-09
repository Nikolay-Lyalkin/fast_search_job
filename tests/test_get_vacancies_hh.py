from unittest.mock import patch

from src.get_vacancies_hh import HH


@patch("requests.get")
def test_get_vacancies(mock_get):
    """Функуия-тест для проверки. что json-файл читается корректно"""
    hh_vacancies = HH()
    mock_get.return_value.json.return_value = {"items": {"page": "Python"}}
    assert hh_vacancies.get_vacancies("Python") == [
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
        "page",
    ]
