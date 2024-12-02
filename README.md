### Grass farm bot



1. Установка зависимостей для работы на серваке
```bash
make install
```

2. Установказ зависимостей для питоновского скрипта
```bash
make install-deps
```

3. Создай папку input, и в нее добавь прокси(в виде .txt файлов), прокси должны быть в формате:
````
LOGIN:PASSWORD@IP:PORT
Пример:
109426211478ce42:RNW78Fm5@res.proxy-seller.com:10018
````

4. Как только все установлено, теперь ты можешь запустить скрипт:
````
make proxy
````
5. У тебя создатся папка ouput, в ней будут прокси в нужном формате для запуска скрипта
````
socks5://LOGIN:PASSWORD@IP:PORT
Пример:
socks5://109426211478ce42:RNW78Fm5@res.proxy-seller.com:10018 [верный формат]
````

6. Теперь можешь запускать один из проксей
````bash
python main.py [grass_user_id] output/output_[N].txt & \
````

Либо ты можешь в мейкфайле задать:
````
run:
	  python main.py [grass_user_id] output/output_1.txt & \
	  python main.py [grass_user_id] output/output_2.txt & \
	  python main.py [grass_user_id] output/output_N.txt & \
	  wait
````


- Примечание:
- В мейкфайле можно задать переменные:
````
INPUT_FOLDER=input
OUTPUT_FOLDER=output
SERVER_USER=root
SERVER_HOST=[ХОСТ СЕРВЕРА]
SERVER_PATH=/home/grass-airdrop-farm/output [это путь до папки output]
````

- Как только все задал и ывыполнил команду make proxy(создатся папка output и отформатируеются прокси)
- Далее ты можешь отправить папку outout на сервер командой:
````
make send-to-server
````
- Там на серваке уже 1-ый пункт, 2-ой пункт, ...  и уже можешь прокси запускать
- Удачи !