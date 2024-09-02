import json
import os
from unittest.mock import mock_open, patch

from src.save_vacancies import SaveJSON


def test_save_vacancies_in_json(hh_vacancies_2):
    """Тест метода сохранения файла JSON"""
    file_path = "../test_save_vacancies.json"
    full_path = os.path.abspath(file_path)
    saver_json = SaveJSON(full_path)

    result = saver_json.save_vacancies(hh_vacancies_2)

    with open(full_path, "r", encoding="utf-8") as f_obj:
        saved_data = json.load(f_obj)
        print(saved_data)


def test_open_file():
    """Тест чтения файла JSON"""
    saver_json = SaveJSON()
    mock_data = (
        '[{"name": "Vacancy 1", "area": {"name": "Moscow"}, "snippet": {"requirement": "Requirements for Vacancy 1",'
        '"responsibility": "Responsibilities for Vacancy 1"}, "experience": {"name": "No experience"}, "employment": '
        '{"name": "Full-time"}, "salary": {"from": 1000, "to": 2000}, "published_at": "2020-01-01"}]'
    )
    with patch("builtins.open", mock_open(read_data=mock_data)):
        data = saver_json.open_file()
        assert data == [
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
            }
        ]
