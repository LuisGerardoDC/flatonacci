"""
Flatonacci secuence is a secuence which is result from the same given secuence 
plus the sum of the last 3 numbers of the secuence. 

The challenge is to create a flatonacci function that given a signature returns the first 
n elements - signature included of the so seeded sequence. So, if we are to 
start our Flatonacci sequence with [1, 1, 1] as a starting input (AKA signature) and n = 8,
we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31]

Another example; if signature is the secuence [0, 0, 1] we should get some thing
like:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

- Signature will always contain 3 numbers 
- n will always be a non-negative number
- if n == 0, then return an empty list and be ready for anything else which is not
clearly specified ;)

Note. Please note that we are gonna test the funcion against a lot of different signatures and n's
"""

from functools import reduce


def check_type(value, check_non_negative=False):
    int_value=value 
    if int_value is not int:
        if type(int_value) == str:
            int_value = int(int_value)
    else:
        raise ValueError(f'value must be int or string but got {type(value)}')
    if(check_non_negative and int_value < 0):
        raise ValueError(f'value must be non negative but got {int_value}')
    return int_value


def flatonacci(signature: list, n: int) -> list:
    result = []
    try:
        n = check_type(n,check_non_negative=True)
        for value in signature:
            result.append(check_type(value))
        
        # genera faltonacci
        for i in range(n-3):
            result.append( reduce(lambda a,b: a+b , result[:-4:-1] ))
        return result

    except ValueError as ve:
        print(ve)
        return []