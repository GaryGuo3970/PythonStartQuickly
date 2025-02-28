import logging
#raise Exception("custom error")

for sym ,w,h in(('*',4,4),('0',20,5),('x',1,3),('ZZ',3,3)):
    for i in range(h-2):
        print(sym+(' '*(w-2)+sym))

ages = [123,4,45,41,23,23,54,43,444]
ages.sort()
assert 1 > 0

logging.basicConfig(level=logging.DEBUG,format= '%(asctime)s %(levelname)s %(message)s')
logging.debug('start debug')


def factorial(n):
    logging.debug(f"start factorial {n}")
    total=0
    for i in range(n):
        total+=i
        logging.debug(f'i is {i} ,total is {total}')
    logging.debug(f"end factorial {n}")
    return total

factorial(10)

logging.debug('end debug')