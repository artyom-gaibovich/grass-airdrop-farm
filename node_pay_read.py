# Открытие исходного файла
with open("input_proxy.txt", "r") as file:
    # Чтение строк из файла
    lines = file.readlines()

# Список для преобразованных строк
formatted_lines = []

# Обработка каждой строки
for line in lines:
    line = line.strip()  # Удаление пробелов и символов перевода строки
    if line:  # Проверяем, что строка не пустая
        # Разделяем строку на части
        try:
            username, password_host, port = line.split(":")
            password, host = password_host.split("@")
            formatted_lines.append(f"{host}:{port}:{username}:{password}")
        except ValueError as e:
            print(f"Ошибка обработки строки: {line}. Проверьте формат. {e}")

# Запись в новый файл
with open("node_pay_proxy.txt", "w") as output_file:
    output_file.write("\n".join(formatted_lines))

print("Преобразование завершено. Результат сохранен в node_pay_proxy.txt.")
