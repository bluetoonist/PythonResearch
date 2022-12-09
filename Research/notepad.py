import hashlib
import os

import requests


def get_url_data(url):
    data = requests.get(url).text

    filename = hashlib.md5(url.encode()).hexdigest()
    f = open(filename, "w")
    f.write(data)
    f.close()

    return data


def get_url_data_stub(url):
    filename = hashlib.md5(url.encode()).hexdigest()
    print(filename)
    if os.path.isfile(filename):
        return open(filename).read()


def get_url_data_v2(url):
    filename = hashlib.md5(url.encode()).hexdigest()
    if os.path.isfile(filename):
        return open(filename).read()

    data = requests.get(url).text
    open(filename, "w").write(data)
    return data


if __name__ == '__main__':
    sample_api = "https://api.sampleapis.com/fakebank/accounts"

    # print(get_url_data(url=sample_api))
    # print(get_url_data_stub(url=sample_api))
    print(get_url_data_v2(url=sample_api))
