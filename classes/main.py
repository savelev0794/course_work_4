"""Файл, реализующий основную логику взаимодействия с пользователем"""
import json

from classes.api_classes import HH, SJ
from file_managers.json_manager import JsonManager
from utils.func import vacancy_view

json_saver = JsonManager()

json_saver.clear()


def main():

    while True:
        keyword = input('Введите название должности / профессии: ')
        hh_vacancy = HH(keyword)
        sj_vacancy = SJ(keyword)
        dict_for_job = {'HH': hh_vacancy.get_vacancies(), 'SJ': sj_vacancy.get_vacancies()}

        with open('job.json', 'w', encoding='utf-8') as file:
            json.dump(dict_for_job, file, ensure_ascii=False, indent=2)

        for data in dict_for_job.values():
            for i, item in enumerate(data, 1):
                print(f"----------------<{i}>-----------------")
                print(vacancy_view(vacancy=item))
                json_saver.add_vacancy(item)

        ask_delete = input('Хотите удалить одну из вакансий в списке? да/нет: ')
        if ask_delete == 'да':
            user_delete = input(
                "Введите индекс вакансии для удаления вакансии: "
            ).strip()

            if user_delete.isnumeric():
                index = int(user_delete) - 1
                op_code = json_saver.delete_vacancy(index=index)

                if op_code == -1:
                    print("Такой вакансии нет")
                else:
                    print("Вакансия успешно удалена")
                    best_vacancy = input('Хотите посмотреть лучшую по зарплате вакансию из списка? да/нет: ')
                    if best_vacancy == 'да':
                        print(f"ЛУЧШАЯ ВАКАНСИЯ ПО ЗАРПЛАТЕ!\n"
                              f"{json_saver.get_best_vacancy()}")
                    else:
                        print('До свидания!')
                        break
        elif ask_delete == 'нет':
            best_vacancy = input('Хотите посмотреть лучшую по зарплате вакансию из списка? да/нет: ')
            if best_vacancy == 'да':
                print(f"ЛУЧШАЯ ВАКАНСИЯ ПО ЗАРПЛАТЕ!\n"
                      f"{json_saver.get_best_vacancy()}")
            else:
                print('До свидания!')
        break


if __name__ == '__main__':
    main()
