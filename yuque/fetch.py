# coding: utf-8

import requests
from retrying import retry

from yuque.settings import GET_TIMEOUT


@retry(stop_max_attempt_number=3, retry_on_result=lambda x: x is None, wait_fixed=5000)
def fetch(url, **kwargs):
    try:
        kwargs.setdefault('timeout', GET_TIMEOUT)
        kwargs.setdefault('verify', False)
        resp = requests.get(url, **kwargs)
        if resp.status_code == 200:
            resp.encoding = 'utf-8'
            return resp.text
    except requests.ConnectionError:
        return


if __name__ == "__main__":
    pass
