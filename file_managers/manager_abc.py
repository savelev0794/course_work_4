"""Абстрактные методы для обработки json для удобства вынесены в отдельный файл"""
from abc import abstractmethod


class FileManager:
    @abstractmethod
    def add_vacancy(self, vacancy: dict):
        pass

    @abstractmethod
    def delete_vacancy(self, index: int):
        pass

    @abstractmethod
    def order_by(self, field: str):
        pass

    @abstractmethod
    def filter(self, salary_from: int, salary_to: int):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_best_vacancy(self):
        pass
