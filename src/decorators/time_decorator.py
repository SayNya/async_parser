import asyncio
import time


def timeit(func):
    async def process(func, *args, **params):
        if asyncio.iscoroutinefunction(func):
            print(f'this function is a coroutine: {func.__name__}')
            return await func(*args, **params)
        else:
            print('this is not a coroutine')
            return func(*args, **params)

    async def helper(*args, **params):
        print(f'{func.__name__}.time')
        start = time.time()
        result = await process(func, *args, **params)
        print('>>>', time.time() - start)
        return result

    return helper
