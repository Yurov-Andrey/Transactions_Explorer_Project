import logging
import os
import time
import pandas

from src.settings import REPORTS_PATH

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(f"{REPORTS_PATH}/transaction_processing.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)d: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def current_time() -> str:
    """Функция определяет текущую дату и время"""

    current_time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return current_time_now


def greating_user(relevant_time: str) -> str:
    """Функция приветствует пользователя в зависимости от текущего времени суток (Добрый день/вечер/ночь/утро)."""

    act_time = int(relevant_time[11:13])
    greating_text = ""

    if 0 <= act_time < 6:
        greating_text = "Доброй ночи!"

    elif 6 <= act_time < 12:
        greating_text = "Доброе утро!"

    elif 12 <= act_time < 17:
        greating_text = "Добрый день!"

    elif 17 <= act_time < 24:
        greating_text = "Добрый вечер!"

    return greating_text


def processing_excel(file_path: str) -> list[dict] | str:
    """Функция для считывания финансовых операций из xlsx. Принимает путь к файлу xlsx в качестве аргумента и
    считывает финансовые операции из xlsx, после чего выдает список словарей с транзакциями."""

    logger.info(f"Старт работы функции {processing_excel}, принят файл по пути {file_path}")

    if os.path.splitext(file_path)[1].lower() != ".xlsx":
        return "Файл по указанному пути не является xlsx файлом"

    try:
        xlsx = pd.read_excel(file_path)
        result_list_excel = xlsx.to_dict(orient="records")
        logger.info(f"Функция {processing_excel} завершила работу и вернула результат.")
        return result_list_excel

    except FileNotFoundError:
        logger.error(f"Запрашиваемый файл не найден или указан некорректный путь ({file_path}) к файлу")
        return f"Запрашиваемый файл не найден или указан некорректный путь ({file_path}) к файлу"

    except ValueError:
        logger.error("Файл по указанному пути не является xlsx файлом")
        return "Файл по указанному пути не является xlsx файлом"


if __name__ == "__main__":
    time_mow = current_time()
    gr = greating_user(time_mow)
    print(time_mow)
    print(gr)
