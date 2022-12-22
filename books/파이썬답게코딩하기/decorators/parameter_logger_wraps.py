import datetime
import time
from functools import wraps


def measure_run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} function running time {end - start}")

        return result

    return wrapper


def parameter_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print("[%s] args: %s, kwargs: %s" % (timestamp, args, kwargs))
        return func(*args, **kwargs)

    return wrapper


@measure_run_time
@parameter_logger
def worker(delay_time):
    time.sleep(delay_time)


if __name__ == '__main__':
    worker(5)
