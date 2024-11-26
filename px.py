# Открытие файла и чтение строк
with open("proxies.txt", "r") as file:
    lines = file.readlines()

# Удаление лишних символов, добавление префикса и формирование списка
proxies = [f'socks5://{line.strip()}' for line in lines]

# Преобразование в строку формата списка
formatted_string = "[\n" + ",\n".join(f'    "{proxy}"' for proxy in proxies) + "\n]"

# Вывод результата
print(formatted_string)
