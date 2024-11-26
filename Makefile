read:
	python3 read.py



INPUT_FOLDER=input
OUTPUT_FOLDER=output
SERVER_USER=root
SERVER_HOST=93.183.81.30
SERVER_PATH=/home/grass-airdrop-farm/output
SSH_PASSWORD=v*n*-i#ZdV?2Ef

run-script:
	@echo "Запуск скрипта Python для обработки файлов..."
	python3 process_files.py

send-to-server:
	@echo "Отправка обработанных файлов на сервер..."
	scp $(OUTPUT_FOLDER)/* $(SERVER_USER)@$(SERVER_HOST):$(SERVER_PATH)
	@echo "Файлы отправлены на сервер."

# Цель по умолчанию
all: run-script send-to-server
