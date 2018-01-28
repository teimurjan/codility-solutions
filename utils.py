from time import time


def check_time(f):
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        print('It took {} seconds'.format(time() - start))
        return result

    return wrapper
