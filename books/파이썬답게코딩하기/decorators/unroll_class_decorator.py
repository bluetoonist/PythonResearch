import time
from functools import update_wrapper, wraps


class MeasureRuntime:
    def __init__(self, active_state):
        self.mesure_active = active_state

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.mesure_active is False:
                return func(*args, **kwargs)

            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} function running time: {end - start} ")

            return result

        return wrapper


@MeasureRuntime(True)
def active_worker(delay_time):
    time.sleep(delay_time)


@MeasureRuntime(False)
def non_active_worker(delay_time):
    time.sleep(delay_time)


if __name__ == '__main__':
    active_worker(5)
    non_active_worker(5)
