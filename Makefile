read:
	python3 read.py

INPUT_FOLDER=input
OUTPUT_FOLDER=output
SERVER_USER=root
SERVER_HOST=
SERVER_PATH=/home/grass-airdrop-farm/output
SSH_PASSWORD=

run-script:
	@echo "Запуск скрипта Python для обработки файлов..."
	python3 process_files.py

send-to-server:
	@echo "Отправка обработанных файлов на сервер..."
	scp $(OUTPUT_FOLDER)/* $(SERVER_USER)@$(SERVER_HOST):$(SERVER_PATH)
	@echo "Файлы отправлены на сервер."

all: run-script send-to-server


install-repo:
	git clone git@github.com:artyom-gaibovich/grass-airdrop-farm.git

install:
	sudo apt update &&
	sudo apt install git screen python3 python3-pip &&


install-deps:
	pip3 install websockets_proxy
	pip3 install loguru

proxy:
	python new_read.py

run:
	  python main.py [grass_user_id] output/output_1.txt & \
	  python main.py [grass_user_id] output/output_2.txt & \
	  python main.py [grass_user_id] output/output_N.txt & \
	  wait