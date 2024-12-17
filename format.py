import os
import shutil

input_dir = "input"  # Папка с исходными файлами прокси
output_dir = "output"  # Папка для записи отформатированных прокси

# Удаление старой папки output и создание новой
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

# Обработка всех файлов в папке input
output_counter = 1
for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, f"output_{output_counter}.txt")

        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                ip, port, username, password = line.strip().split(":")
                formatted_proxy = f"socks5://{username}:{password}@{ip}:{port}"
                outfile.write(formatted_proxy + "\n")

        output_counter += 1

print(f"Прокси успешно сконвертированы и сохранены в папке {output_dir}")