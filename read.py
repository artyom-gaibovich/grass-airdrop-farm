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

input_filename = "input_proxy.txt"
output_filename = "output_proxy.txt"

add_prefix_to_lines(input_filename, output_filename)
