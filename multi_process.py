import logging
import multiprocessing
import subprocess
import sys

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат вывода
    handlers=[
        logging.StreamHandler(sys.stdout),  # Вывод в консоль
        logging.FileHandler('process_log.log')  # Запись в файл
    ]
)


# Функция для запуска процесса с логированием
def run_process(user_id, path):
    logging.info(f"Starting process for user_id={user_id}, path={path}")
    try:
        # Запускаем команду и передаем параметры в subprocess
        result = subprocess.run(
            ['python', 'main.py', user_id, path],
            check=True,  # Проверка на ошибки
            text=True,  # Возвращать текстовый вывод
            capture_output=True  # Сохраняем вывод
        )
        # Логируем стандартный вывод процесса
        logging.info(f"Output for {user_id}: {result.stdout}")
    except subprocess.CalledProcessError as e:
        # Логируем ошибку, если процесс завершился с ошибкой
        logging.error(f"Error occurred while processing {user_id}: {e.stderr}")


def process_file(file_path):
    # Читаем строки из файла
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Создаем список из пар (userId, path)
    tasks = []
    for line in lines:
        # Разделяем строку на два компонента
        parts = line.strip().split(',')
        if len(parts) == 2:
            user_id, path = parts
            tasks.append((user_id, path))
        else:
            logging.warning(f"Skipping invalid line: {line.strip()}")

    # Создаем пул процессов
    with multiprocessing.Pool(processes=10) as pool:
        pool.starmap(run_process, tasks)


if __name__ == "__main__":
    file_path = 'your_file.txt'  # Укажите путь к вашему файлу
    logging.info(f"Starting to process the file: {file_path}")
    process_file(file_path)
    logging.info("Processing finished.")
