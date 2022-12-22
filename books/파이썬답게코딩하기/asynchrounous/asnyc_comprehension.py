import asyncio


async def delay_range(to, delay=1):
    for i in range(10):
        yield i
        await asyncio.sleep(delay=delay)


async def run():
    print("Async Await Comprehension")
    return [i async for i in delay_range(3)]


async def run_multiple():
    print("Async Await Comprehension")
    func_list = [run, run]

    result = [await func() for func in func_list]
    print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run_multiple())
    finally:
        loop.close()
