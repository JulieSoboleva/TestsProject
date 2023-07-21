import pytest

from tasks import filter_cities_list, find_distribution, list_to_dict,\
    get_unique_items, get_max_volume


@pytest.mark.parametrize(
    'visit_list, contry, expected', [
        (None, 'Россия', []),
        ([], 'Греция', []),
        ([{'visit1': ['Москва', 'Россия']}], None, []),
        ([{'visit1': ['Москва', 'Россия']}], '', []),
        (None, None, []),
        ([], '', []),
        ([{'visit1': ['Москва', 'Россия']},
          {'visit2': ['Дели', 'Индия']},
          {'visit3': ['Владимир', 'Россия']},
          {'visit4': ['Лиссабон', 'Португалия']},
          {'visit5': ['Париж', 'Франция']},
          {'visit6': ['Лиссабон', 'Португалия']},
          {'visit7': ['Тула', 'Россия']},
          {'visit8': ['Тула', 'Россия']},
          {'visit9': ['Курск', 'Россия']},
          {'visit10': ['Архангельск', 'Россия']}], 'Россия',
         [{'visit1': ['Москва', 'Россия']},
          {'visit3': ['Владимир', 'Россия']},
          {'visit7': ['Тула', 'Россия']},
          {'visit8': ['Тула', 'Россия']},
          {'visit9': ['Курск', 'Россия']},
          {'visit10': ['Архангельск', 'Россия']}]),
        ([{'visit1': ['Москва', 'Россия']},
          {'visit2': ['Дели', 'Индия']},
          {'visit3': ['Владимир', 'Россия']},
          {'visit4': ['Лиссабон', 'Португалия']},
          {'visit5': ['Париж', 'Франция']},
          {'visit6': ['Лиссабон', 'Португалия']},
          {'visit7': ['Тула', 'Россия']},
          {'visit8': ['Тула', 'Россия']},
          {'visit9': ['Курск', 'Россия']},
          {'visit10': ['Архангельск', 'Россия']}], 'Кипр', [])
    ]
)
def test_filter_cities_list(visit_list, contry, expected):
    assert filter_cities_list(visit_list, contry) == expected


@pytest.mark.parametrize(
    'ids, expected', [
        (None, []),
        ({}, []),
        ({'user1': [213, 213, 213, 15, 213],
          'user2': [54, 54, 119, 119, 119],
          'user3': [213, 98, 98, 35]}, [98, 35, 15, 213, 54, 119]),
        ({'user1': [1, 1, 1, 1, 1],
          'user2': [2, 2, 2, 2, 2]}, [1, 2])
    ]
)
def test_get_unique_items(ids, expected):
    assert get_unique_items(ids) == expected


@pytest.mark.parametrize(
    'queries, expected', [
        (None, []),
        ([], []),
        ([''], [1, 0, 0, 0, 0, 0]),
        (['смотреть сериалы онлайн',
          'новости спорта',
          'афиша кино',
          'курс доллара',
          'сериалы этим летом',
          'курс по питону',
          'сериалы про спорт'], [0, 0, 3, 4, 0, 0]),
        (['кино', 'спорт', 'python', 'java', 'SQL'], [0, 5, 0, 0, 0, 0])
    ]
)
def test_find_distribution(queries, expected):
    assert find_distribution(queries) == expected


@pytest.mark.parametrize(
    'stats, expected', [
        (None, None),
        ({}, None),
        ({'facebook': 55, 'yandex': 120, 'vk': 115,
          'google': 99, 'email': 42, 'ok': 98}, ('yandex', 120)),
        ({'facebook': 55, 'yandex': 55, 'vk': 55,
          'google': 55, 'email': 55, 'ok': 55}, ('facebook', 55)),
        ({'vk': 115}, ('vk', 115))
    ]
)
def test_get_max_volume(stats, expected):
    assert get_max_volume(stats) == expected


@pytest.mark.parametrize(
    'src_list, expected', [
        (None, {}),
        ([], {}),
        (['One'], {}),
        (['One', 'Two'], {'One': 'Two'}),
        (['2018-01-01', 'yandex', 'cpc', 100],
         {'2018-01-01': {'yandex': {'cpc': 100}}})
    ]
)
def test_list_to_dict(src_list, expected):
    assert list_to_dict(src_list) == expected
