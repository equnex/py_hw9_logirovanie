import pytest
from game import normalize_city, rule_check



def test_normalize_city_lowercases():
    """
    *Тест на позитивычах
    """
    assert normalize_city("МОСКВА") == "москва"



def test_normalize_city_isdigit():
    """
    * Тест на негативычах
    """
    with pytest.raises(ValueError):
        normalize_city("Псков1")



@pytest.mark.parametrize("city1, city2, expected", [
    ("Псков", "Владимир", True),
    ("Псков", "Вологда", True),
    ("Псков", "Москва", False),
    ("Псков", "Остров", False)
])
def test_rule_check_parametrize(city1, city2, expected):
    """
    *Параметризация
    """
    assert rule_check(city1, city2) == expected


