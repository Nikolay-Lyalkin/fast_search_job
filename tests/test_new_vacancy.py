def test_vacancy_init(vacancy_1):
    """Тест инициализации класса Vacancy"""
    assert vacancy_1.name == "Менеджер по продажам"
    assert vacancy_1.area == "Москва"
    assert vacancy_1.requirement == "Знание английского языка"
    assert vacancy_1.responsibility == "Организация культуры продажи продукта"
    assert vacancy_1.experience == "от 3 до 5 лет"
    assert vacancy_1.employment == "полная занятость"
    assert vacancy_1.salary_from == 150000
    assert vacancy_1.salary_to == 200000
    assert vacancy_1.published_at == "12.12.2023 15:20:48"
