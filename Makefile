read:
	python3 read.py

INPUT_FOLDER=input
OUTPUT_FOLDER=output
SERVER_USER=root
SERVER_HOST=89.223.122.215
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
	  python main.py 2pBIJW72ZEYmUyTSjQkZV2bR6LD output/output_1.txt & \
	  python main.py 2pAI2Q6KBRt5K6tZ61qdaKyGgFm output/output_2.txt & \
	  wait



//run:
	  python main.py 2p9mtXal4k5Q5Vav1lU2pvoEhup output/output_1.txt
	python main.py 2pAIMZjHFiGpdtaOYvsEr5ZTzDu output/output_2.txt
	  python main.py 2p9nbc2RB7rbOBu9yACR1D84FZ1 output/output_3.txt
	  python main.py 2pAIAxqG0ZRV4e7A9SZBJxPaapV output/output_4.txt
	  python main.py 2p9nEB5xhXbYrCdobE7cWfydfq1 output/output_5.txt

	  python main.py 2pAIS1wQLkHccgdR22s07UKfS0J output/output_6.txt














