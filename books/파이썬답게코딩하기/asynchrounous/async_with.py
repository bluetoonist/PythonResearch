import asyncio


class AsynchronousReader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None

    async def __aenter__(self):
        try:
            self.file = open(self.file_name, "rb")
        except:
            print("File Open Error")
            raise Exception
        else:
            return self.file

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


async def read_file(file_name):
    async with AsynchronousReader(file_name) as af:
        for line in af.readlines():
            print(line.decode("utf-8").strip())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(read_file("./test.txt"))
    finally:
        loop.close()
