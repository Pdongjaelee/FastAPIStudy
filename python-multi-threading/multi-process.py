import requests
import time
import os
import threading
from concurrent.futures import ProcessPoolExecutor

# multi-proces를 사용하려면 위의 ProcessPoolExecutor 를 import 한다.

def fetcher(params):
    seesion = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text
# os.getpid() 는 현재 process id를 return 해준다. pid는 프로세스 각각의 id

def main():
    urls = ["https://google.com", "https://apple.com"] * 50

    executor = ProcessPoolExecutor(max_workers=10)

    with requests.Session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        params = [(session, url)for url in urls]
        executor.map(fetcher, urls)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 19



