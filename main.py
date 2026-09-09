from cities import cities_list


def get_cities(cities_data: list[dict]) -> set[str]:
    """
    Подготавливает множество городов, извелкает названия городов из списка словарей.

    Принимает один параметр cities_data: list[dict]

    Возвращает множество городов set[str]
    """
    cities = set()
    for city in cities_data:
        cities.add(city["name"].lower())
    return cities


def rule_check(city1: str, city2: str) -> bool:
    """
    Функция проверяет правило игры: "Последняя буква city1 должна совпадать с первой буквой city2"

    Args:
        city1 (str): предыдущий названный город.
        city2 (str): город, который хочет назвать игрок.

    Возвращает True, есмли правило соблюдено, иначе False

    """
    if not city1 or not city2:
        return False
    return city1[-1].lower() == city2[0].lower()


def city_check(available: set[str], letter: str) -> str | None:
    """
    Функция ищет город, на нужную букву

    Args:
        available: set[str]: не использованные города
        letter: str: буква, с который должен начинаться город

        Возвращает найденный город или None (если такого нету)
    """
    for city in available:
        if city[0] == letter.lower():
            return city
    else:
        return None


def main() -> None:
    available_cities = get_cities(cities_list)
    last_city = ""

    while True:
        user_input = input("Введите город или 'стоп' для выхода: ").strip().lower()
        if user_input == "стоп":
            print("Вы завершили игру")
            break

        if user_input not in available_cities:
            print(
                f"Города {user_input} не существует или вы его уже использовали. Ты проиграл, чилавэк!"
            )
            break

        if last_city and not rule_check(last_city, user_input):
            print(
                f"Город должен начинаться на букву '{last_city[-1]}'. Чилавэк проиграл!"
            )
            break

        available_cities.remove(user_input)
        last_city = user_input

        letter = last_city[-1]
        computer_city = city_check(available_cities, letter)

        if computer_city is None:
            print(f"Я нимагу найти город на букву {letter}. Ты победил чилавэк!")
            break

        print(f"Компьютер назвал: {computer_city}")
        available_cities.remove(computer_city)
        last_city = computer_city


main()
