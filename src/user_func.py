def get_top_salary(vacancies: list[dict], top_n: int) -> list[dict]:
    """Функция для получения топ N вакансий по зарплате"""
    result = sorted(vacancies, key=lambda x: x["salary_to"], reverse=True)
    return result[:top_n]


def filter_vacancies(vacancies: list[dict], filter_words: str) -> list[dict]:
    """Функция для фильтрации вакансий по ключевым словам"""
    result = []
    for vacancy in vacancies:
        if filter_words.lower() in vacancy["name"].lower():
            result.append(vacancy)
    if not result:
        print("Подходящих вакансий не найдено")
    return result


def get_vacancies_by_salary(vacancies: list[dict], expected_salary: int) -> list[dict]:
    """Функция для фильтрации вакансий по зарплате"""
    result = []
    for vacancy in vacancies:
        if expected_salary <= vacancy["salary_to"]:
            result.append(vacancy)
    return result


def print_vacancies(vacancies: list[dict]):
    for vacancy in vacancies:
        print(
            f"{vacancy['name']}, город: {vacancy['area']}, требования: {vacancy['requirement']}, зарплата:\
{vacancy['salary_from']} - {vacancy['salary_to']}"
        )
