import multiprocessing
import subprocess


# Функция для запуска процесса
def run_process(user_id, path):
    try:
        result = subprocess.run(
            ['python', 'main.py', user_id, path],
            check=True,  # Проверка на ошибки
            text=True,  # Возвращать текстовый вывод
            capture_output=True  # Сохраняем вывод
        )
        print(f"Output for {user_id}: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while processing {user_id}: {e.stderr}")

def process_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    tasks = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 2:
            user_id, path = parts
            tasks.append((user_id, path))
        else:
            print(f"Skipping invalid line: {line.strip()}")

    with multiprocessing.Pool(processes=10) as pool:
        pool.starmap(run_process, tasks)


if __name__ == "__main__":
    file_path = 'your_file.txt'  # Укажите путь к вашему файлу
    process_file(file_path)
