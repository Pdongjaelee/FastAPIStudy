import requests

def io_bound_func():
    result = requests.get("https://google.com")
    return result


if __name__

