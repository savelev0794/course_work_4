class Vacancy:
    """Скрипт запроса на платформу"""
    def __init__(self, keyword, page=0):
        self.url: str = 'https://api.hh.ru/vacancies'
        self.params: dict = {
            'text': keyword,
            'page': page
        }

    def get_vacancies(self):
        pass
