from datetime import datetime as dt


class Vacancy:
    """Класс для создания новых вакансий"""

    id = 1

    def __init__(
        self,
        name: str,
        area: str,
        requirement: str,
        responsibility: str,
        experience: str,
        employment: str,
        salary_from: int = None,
        salary_to: int = None,
        published_at: str = None,
    ):
        self.id = Vacancy.id
        self.name = name
        self.area = area
        if salary_from:
            self.salary_from = salary_from
        else:
            self.salary_from = 0
        if salary_to:
            self.salary_to = salary_to
        else:
            self.salary_to = 0
        self.requirement = requirement
        self.responsibility = responsibility
        self.experience = experience
        self.employment = employment
        if published_at:
            self.published_at = published_at
        else:
            self.published_at = dt.strptime(str(dt.now()), "%Y-%m-%d %H:%M:%S.%f").strftime("%d.%m.%Y %H:%M:%S")
        Vacancy.id += 1

    def __str__(self) -> str:
        """Метод для отображения информации об объекте класса для пользователей"""
        return f"{self.id}: {self.name}, город - {self.area}, требования - {self.requirement}, зарплата - от \
{self.salary_from} до {self.salary_to}\n"

    def __gt__(self, other) -> bool:
        """Метод для операции сравнения «больше»"""
        return self.salary_to > other.salary_to
