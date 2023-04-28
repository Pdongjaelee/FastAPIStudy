import requests
import time

def fetcher(session, url):
    with session.get(url) as response:      #fetcher는 session에 해당하는 url을 보내서 해당하는 url의 데이터를 가져온다.
        return response.text
def main():
    url = "https://naver.com"

    with requests.Session() as session:
        result = fetcher(session, url)
        print(result)


if __name__ =="__main__":
    main()