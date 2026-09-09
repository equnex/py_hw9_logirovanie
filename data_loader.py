import logging
import json
logger = logging.getLogger(__name__)


def load_cities(filename: str = "cities.json") -> list[dict] | None:
    """
    *Загружает список городов из JSON-файла.
    *Возвращает список словарей при успехе, иначе None.
    """
    try:
        with open(filename, encoding="utf-8") as f:
            data = json.load(f)
        logger.debug(f"Загружено {len(data)} записей из {filename}")
        return data
    except FileNotFoundError:
        logger.critical(f"Файл {filename} не найден")
        return None
    except json.JSONDecodeError as e:
        logger.critical(f"Ошибка JSON: {e}")
        return None