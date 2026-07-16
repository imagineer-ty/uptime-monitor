import requests
import time


def check_website(url):
    try:
        start = time.time()

        response = requests.get(
            url,
            timeout=5
        )

        response_time = round(
            (time.time() - start) * 1000,
            2
        )

        return {
            "status": "UP",
            "status_code": response.status_code,
            "response_time_ms": response_time
        }

    except requests.exceptions.RequestException:
        return {
            "status": "DOWN",
            "status_code": None,
            "response_time_ms": None
        }
