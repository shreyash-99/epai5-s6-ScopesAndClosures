from functools import wraps


def check_function_min_length_docstring(min_length = 50, *args, **kwargs):
    '''
    this function returns a closure which accepts a function as an input
    It has a free variable length, and checks if the docstring of the input function is more than the length or not
    '''
    if len(args) > 0 or len(kwargs):
        raise TypeError('received more number of parameters than required')
    if type(min_length) not in [int]:
        raise TypeError('type of the minimum length passed is wrong, it only accepts integer')
    
    length = min_length
    def inner(func, *args, **kwargs):
        '''
        accepts a function and returns true if length of the docstring is more than the min_length 
        '''
        if not callable(func):
            raise TypeError('input to this should be a function')
        if len(args) > 0  or len(kwargs) > 0:
            raise TypeError("only one function is to be given as input")
        if len(func.__doc__) >= length:
            return True
        else:
            return False
    def change_min_length(new_min_length, *args, **kwargs):
        if type(new_min_length) not in [int]:
            raise TypeError('input should be a number')
        if len(args) > 0 or len(kwargs) > 0 :
            raise TypeError('received more inputs than required')
        if new_min_length < 0:
            raise ValueError('value should be more than or equal to 0')
        nonlocal length
        length = new_min_length
    return inner, change_min_length

def fibonacci(*args, **kwargs):
    '''
    returns a closure which generates the next number in the fibonacci series
    '''
    cache = {1: 0, 2: 1}
    if len(args)> 0 or len(kwargs) > 0:
        raise TypeError('received more inputs than required')
    def calc_fib(n, *args, **kwargs):
        '''
        returns the next number in the fibonacci sequence
        '''
        if len(args) > 0  or len(kwargs) > 0:
            raise TypeError('only one input is allowed')
        if type(n) not in [int]:
            raise TypeError('input should be an integer')
        if n < 1:
            raise ValueError(' value should be more than 1')
        if n not in cache:
            print('Calculating fib({0})'.format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib


def counter(func,*args, **kwargs):
    '''
    accepts a function and returns a closure(or a decorator) which can then be used to called. 
    This will store the number of times function is called
    '''
    count = 0
    if len(args) > 0 or len(kwargs) > 0:
        raise TypeError('more inputs than required were provided')
    if not callable(func):
            raise TypeError('input to this should be a function')
    def inner(*args, **kwargs):
        '''
        When called, it calls the func stored as a local variable with the arguments given as well increases the count which tracks how many times a function is called.
        '''
        nonlocal count 
        count = count + 1
        return func(*args, **kwargs), count
    return inner




def add(a: int, b: int, *args, **kwargs):
    '''
    accepts two number(integer or float) as input and returns sum
    '''
    if len(args) > 0 or len(kwargs) > 0:
        raise TypeError('more inputs than required were provided')
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError('input was not in required type')
    return a + b

def div(a: int, b: int, *args, **kwargs):
    '''
    accepts two number(integer or float) as input and returns sum
    '''
    if len(args) > 0 or len(kwargs) > 0:
        raise TypeError('more inputs than required were provided')
    if b ==0 :
        raise ZeroDivisionError('division by zero not possible')
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError('input was not in required type')
    return a / b

def mul(a: int, b: int, *args, **kwargs):
    '''
    accepts two number(integer or float) as input and returns their multiplied value
    '''
    if len(args) > 0 or len(kwargs) > 0:
        raise TypeError('more inputs than required were provided')
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError('input was not in required type')
    return a * b


def counter_add_mul_div(*args, **kwargs):
    '''
    returns 3 closure function which can be called for add, mul and div
    each of closure function returns 2 things
    first is the answer, 2 is the dictionary which returns the count of times all three function has been called
    ''' 
    count_dict_add_mul_div = {'count_add' : 0 , 'count_mul' : 0, 'count_div' : 0}
    if len(args) > 0 or len(kwargs) > 0:
        raise TypeError('more inputs than required were provided')
    # print(count_dict_add_mul_div)
    
    @wraps(add)
    def add_inner(*args, **kwargs):
        nonlocal count_dict_add_mul_div
        count_dict_add_mul_div['count_add'] += 1
        result = add(*args, **kwargs)
        return result, count_dict_add_mul_div
    
    @wraps(mul)
    def mul_inner(*args, **kwargs):
        nonlocal count_dict_add_mul_div
        count_dict_add_mul_div['count_mul'] += 1
        return mul(*args, **kwargs), count_dict_add_mul_div
    
    @wraps(div)
    def div_inner(*args, **kwargs):
        nonlocal count_dict_add_mul_div
        count_dict_add_mul_div['count_div'] += 1
        return div(*args, **kwargs), count_dict_add_mul_div
    return add_inner, mul_inner, div_inner, count_dict_add_mul_div


def counter_3_functions(func1, func2, func3, func1_name = 'func1', func2_name = 'func2', func3_name = 'func3' , *args, **kwargs):
    '''
        gets 3 functions as input and is required to keep a log of many times each of the function are called 
    '''
    if len(args) > 0 or len(kwargs) > 0:
        raise TypeError('more inputs than required were provided')
    if not callable(func1) or not callable(func2) or not callable(func3):
        raise TypeError('input to this should be function')
    if type(func1_name) not in [str] or type(func2_name) not in [str] or type(func3_name) not in [str]:
        raise TypeError('inputs of function names should be a string')
    counter = {func1_name : 0, func2_name: 0, func3_name: 0}
    @wraps(func1)
    def func1_inner(*args, **kwargs):
        nonlocal counter
        counter[func1_name] += 1
        func1(*args, **kwargs) 
    
    @wraps(func2)
    def func2_inner(*args, **kwargs): 
        nonlocal counter
        counter[func2_name] += 1
        func2(*args, **kwargs) 
    
    @wraps(func3)
    def func3_inner(*args, **kwargs): 
        nonlocal counter
        counter[func3_name] += 1
        func3(*args, **kwargs) 
    
    return func1_inner, func2_inner, func3_inner, counter
    
    