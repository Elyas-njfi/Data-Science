import numpy as np
from .make_array import make_array

COUNTER = 0

def generate_random_number(input, window):
    global COUNTER
    COUNTER += 1
    random_number = np.random.randint(0, 101)
    make_array(random_number, input, window)
    if COUNTER != input:
        generate_random_number(input, window)
    COUNTER = 0







