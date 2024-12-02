import os


def add_prefix_to_lines(input_file, output_file):
    prefix = "socks5://"
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            line = line.strip()
            if line:
                outfile.write(f"{prefix}{line}\n")
    print(f"Обработка завершена. Результат сохранён в '{output_file}'.")


def clear_output_folder(output_folder):
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print(f"Папка '{output_folder}' очищена от старых файлов.")


def process_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    clear_output_folder(output_folder)
    input_files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]
    input_files.sort()
    for index, filename in enumerate(input_files, start=1):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, f"output_{index}.txt")

        add_prefix_to_lines(input_file, output_file)



input_folder = "input"
output_folder = "output"

process_files(input_folder, output_folder)
