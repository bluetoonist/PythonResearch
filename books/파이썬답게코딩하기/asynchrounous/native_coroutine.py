import asyncio
import random
import datetime


async def print_time(idx):
    sleep_time = random.randrange(1, 10)

    await asyncio.sleep(sleep_time)
    print("[%s] Sleep time: %s, Complete Time: %s" % (idx, sleep_time, datetime.datetime.now()))


def main():
    futures = [print_time(i) for i in range(10)]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    loop.close()


if __name__ == '__main__':
    main()
