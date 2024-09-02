from src.get_vacancies_hh import HH
from src.new_vacancy import Vacancy
from src.save_vacancies import SaveJSON
from src.user_func import filter_vacancies, get_top_salary, get_vacancies_by_salary, print_vacancies
from src.vacancies import Vacancies

hh_api = HH()
cls_vacancies = Vacancies()
hh_vacancies = hh_api.get_vacancies("Python")
vacancies_object_list = cls_vacancies.cast_to_object_list(hh_api)
vacancy = Vacancy(
    "Junior разработчик",
    "Москва",
    "Знание языка програмирования - Python",
    "Написание простых скриптов",
    "от 3 до 5 лет",
    "полная занятость",
    120000,
    150000,
)

json_saver = SaveJSON()
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy)


def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    salary_range = int(input("Введите ожидаемую зарплату: "))  # Пример: 100000
    top_n = int(input("Введите количество вакансий для вывода в топ N зарплат: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower()

    filtered_vacancies = filter_vacancies(vacancies_object_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    top_vacancies = get_top_salary(ranged_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
