# -*- coding: utf-8 -*-
# @Author   :Solana0x
# @File     :main.py
# @Software :PyCharm
import asyncio
import random
import ssl
import json
import time
import uuid
from loguru import logger
from websockets_proxy import Proxy, proxy_connect
from multiprocessing import Pool

def remove_proxy_from_list(proxy):
    with open("proxy.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line.strip() != proxy:
                file.write(line)
        file.truncate()




async def connect_to_wss(socks5_proxy, user_id):
    device_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, socks5_proxy))
    logger.info(device_id)
    while True:
        try:
            await asyncio.sleep(random.uniform(0.1, 1.0))  # Reduced frequency
            custom_headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
            }
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            uri = "wss://proxy2.wynd.network:4444/"     # wss://proxy2.wynd.network:4650/
            server_hostname = "proxy.wynd.network"
            proxy = Proxy.from_url(socks5_proxy)
            async with proxy_connect(uri, proxy=proxy, ssl=ssl_context, extra_headers={
                "Origin": "chrome-extension://lkbnfiajjmbhnfledhphioinpickokdi",
                "User-Agent": custom_headers["User-Agent"]
            }) as websocket:
                async def send_ping():
                    while True:
                        send_message = json.dumps(
                            {"id": str(uuid.uuid4()), "version": "1.0.0", "action": "PING", "data": {}})
                        logger.debug(send_message)
                        await websocket.send(send_message)
                        await asyncio.sleep(110)  # Increased interval to reduce bandwidth usage

                send_ping_task = asyncio.create_task(send_ping())
                try:
                    while True:
                        response = await websocket.recv()
                        message = json.loads(response)
                        logger.info(message)
                        if message.get("action") == "AUTH":
                            auth_response = {
                                "id": message["id"],
                                "origin_action": "AUTH",
                                "result": {
                                    "browser_id": device_id,
                                    "user_id": user_id,
                                    "user_agent": custom_headers['User-Agent'],
                                    "timestamp": int(time.time()),
                                    "device_type": "extension",
                                    "version": "4.26.2",
                                    "extension_id": "lkbnfiajjmbhnfledhphioinpickokdi"
                                }
                            }
                            logger.debug(auth_response)
                            await websocket.send(json.dumps(auth_response))

                        elif message.get("action") == "PONG":
                            pong_response = {"id": message["id"], "origin_action": "PONG"}
                            logger.debug(pong_response)
                            await websocket.send(json.dumps(pong_response))
                finally:
                    send_ping_task.cancel()

        except Exception as e:
            logger.error(f"Error with proxy {socks5_proxy}: {str(e)}")
            if any(error_msg in str(e) for error_msg in ["Host unreachable", "[SSL: WRONG_VERSION_NUMBER]", "invalid length of packed IP address string", "Empty connect reply", "Device creation limit exceeded", "sent 1011 (internal error) keepalive ping timeout; no close frame received"]):
                logger.info(f"Removing error proxy from the list: {socks5_proxy}")
                remove_proxy_from_list(socks5_proxy)
                return None  # Signal to the main loop to replace this proxy
            else:
                continue  # Continue to try to reconnect or handle other errors




async def process_proxies(proxies, user_id):
    tasks = {asyncio.create_task(connect_to_wss(proxy, user_id)): proxy for proxy in proxies}

    while True:
        done, _ = await asyncio.wait(tasks.keys(), return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            if task.result() is None:  # Если задача завершилась с ошибкой
                failed_proxy = tasks.pop(task)
                logger.info(f"Removing and replacing failed proxy: {failed_proxy}")
                proxies.remove(failed_proxy)  # Убираем прокси из пула
        # Перезапускаем недостающие задачи
        while len(tasks) < len(proxies):
            proxy = random.choice(proxies)
            tasks[asyncio.create_task(connect_to_wss(proxy, user_id))] = proxy


def run_proxy_group(proxy_group, user_id):
    # Запуск asyncio-цикла в отдельном процессе
    asyncio.run(process_proxies(proxy_group, user_id))


def split_into_groups(items, group_size):
    """Разделить список на группы по `group_size`"""
    for i in range(0, len(items), group_size):
        yield items[i:i + group_size]


if __name__ == "__main__":
    _user_id = "2pIZxuyEylPFlRXX8D8sDyyeMw6"  # Замените на ваш ID пользователя
    proxy_file = "proxy.txt"

    with open(proxy_file, "r") as file:
        all_proxies = file.read().splitlines()

    group_size = 1000  # Размер группы
    proxy_groups = list(split_into_groups(all_proxies, group_size))

    with Pool(len(proxy_groups)) as pool:
        pool.starmap(run_proxy_group, [(group, _user_id) for group in proxy_groups])



