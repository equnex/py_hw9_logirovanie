import logging
from colorlog import ColoredFormatter
from logging.handlers import RotatingFileHandler
from data_loader import load_cities
from game import get_cities, play_game


console_handler = logging.StreamHandler()
console_formatter = ColoredFormatter(
    fmt=(
        """
        * Покраска логов для консоли
        """
        "%(asctime)s | "
        "%(log_color)s%(levelname)-8s%(reset)s | "
        "%(name)s | %(message)s"
    ),
    datefmt="%H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_white,bg_red",
    },
)
console_handler.setFormatter(console_formatter)

def setup_logging():
    """Настройка логирования: вывод в консоль и в файл game.log."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            console_handler,
            logging.StreamHandler(),
            RotatingFileHandler(
                "game.log", maxBytes=1_000_000, backupCount=3, encoding="utf-8",
            )
        ]
    )

def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    cities_data = load_cities()
    if cities_data is None:
        logger.critical("Невозможно запустить игру из-за ошибки загрузки данных")
        print("Не удалось загрузить данные городов. Проверьте файл cities.json.")
        return

    cities_set = get_cities(cities_data)
    logger.info(f"Загружено {len(cities_set)} уникальных городов")
    logger.info("Игра успешно запущена")
    play_game(cities_set)

if __name__ == "__main__":
    main()