from pprint import pprint


def filter_cities_list(geo_logs, contry):
    """
    Выбирает из списка с визитами по городам и странам
    данные о визитах из указанной страны.
    :param contry: страна
    :return: отфильтрованный список
    """
    if geo_logs is None:
        return []
    for visit in geo_logs.copy():
        if contry not in list(visit.values())[0]:
            geo_logs.remove(visit)
    return geo_logs


def get_unique_items(id_dict):
    """
    Вернуть все уникальные гео-ID из значений словаря
    :param id_dict: словарь
    :return: список уникальных значений
    """
    res_list = []
    if id_dict is None:
        return res_list
    for id in id_dict.values():
        res_list.extend(id)
    res_list = list(set(res_list))
    return res_list


def find_distribution(queries):
    """
    Дан список поисковых запросов. Получить распределение количества слов в них.
    Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.
    :param queries: список запросов
    :return: список распределений
    """
    if queries is None or queries == []:
        return []
    queries_list = [0, 0, 0, 0, 0, 0]  # индекс соответствует количеству слов в запросе
    for query in queries:
        word_count = len(query.split())
        queries_list[word_count] += 1
    return queries_list


def get_max_volume(stats):
    """
    Дана статистика рекламных каналов по объемам продаж.
    Напишите скрипт, который возвращает название канала с максимальным объемом.
    :param stats: статистика каналов по объемам продаж
    :return: название канала с максимальным объёмом и его объём продаж
    """
    if stats is None or stats == {}:
        return None
    res_name = ''
    max_volume = 0
    for name, volume in stats.items():
        if volume > max_volume:
            res_name = name
            max_volume = volume
    return res_name, max_volume


def list_to_dict(src_list):
    """
    Функция преобразования произвольного списка в словарь
    :param src_list: список
    :return: словарь
    """
    if src_list is None:
        return {}
    src_list.reverse()
    res_dict = {}
    for i in range(len(src_list) - 1):
        res_dict = {
            src_list[i + 1]: src_list[i]
        } if i == 0 else {
            src_list[i + 1]: res_dict
        }
    return res_dict


if __name__ == '__main__':
    print('Задание 1.')
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    pprint(filter_cities_list(geo_logs, 'Россия'))

    print('\nЗадание 2.')
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    print(get_unique_items(ids))

    print('\nЗадание 3.')
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]
    queries_list = find_distribution(queries)
    print('-' * 43)
    print(f'|{"Количество слов":^20}|{"Встречаемость, %":^20}|')
    print('-' * 43)
    for index, count in enumerate(queries_list):
        if index > 0:
            print(f'|{index:^20}|{round(count / sum(queries_list) * 100):^20}|')
    print('-' * 43)

    print('\nЗадание 4.')
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    result = get_max_volume(stats)
    print(f'Канал с максимальным объёмом продаж ({result[1]}): {result[0]}.')

    print('\nЗадание 5.')
    src_list = ['2018-01-01', 'yandex', 'cpc', 100]
    print(list_to_dict(src_list))
