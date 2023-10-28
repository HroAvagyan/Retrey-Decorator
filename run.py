from decorator import retry
import random

@retry(Exception, tries=3,delay=3,backoff=1)
def random_numbers_interval(p, q):
    """Function generates rundom number in interval [0,1], p, q are from [0,1] interval"""

    random_number = random.uniform(0,1)
    if random_number < p:
        raise Exception('less than lower bound')
    if random_number > q:
        raise Exception('grader than upper bound')
    print(random_number)
    return random_number
random_numbers_interval(0.2,0.5)