import pytest
import re
import inspect
import random
import os
import math
from decimal import *

import session6
from session6 import *


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"   
    
def test_minlength_docstring_check_if_function_exist():
    assert hasattr(session6, "check_function_min_length_docstring"), "check_function_min_length_docstring function missing!"
    
def test_minlength_docstring_check_working():
    def func1():
        '''
        docstring not sufficient
        '''
        pass
    def func2():
        '''
        this function accepts 'x' as input and gives 'y' as an input, this docstring is sufficiently long as it explains the function quite well.
        '''
        pass
    check_func, ___= check_function_min_length_docstring()
    assert check_func(func1) == False, "Function is not correctly working for docstring less than required length"
    assert check_func(func2) == True, "Function is not working correctly when length of docstring is more than required"
    
def test_minlength_docstring_changing_minlength1():
    check_func, change_minLength = check_function_min_length_docstring()
    change_minLength(5)
    def func1():
        '''
        docstring not sufficient
        '''
        pass
    assert check_func(func1) == True, "changing the minimum length using a separate closure function not working" 
    change_minLength(30)
    def func2():
        '''
        this function accepts 'x' as input and gives 'y' as an input, this docstring is sufficiently long
        '''
        pass
    assert check_func(func2) == True, "changing the minimum length using a separate closure function not working" 
    assert check_func(func1) == True, "changing the minimum length using a separate closure function not working" 
    change_minLength(200)
    assert check_func(func2) == False, "hanging the minimum length using a separate closure function not working"
    assert check_func(func1) == False, "changing the minimum length using a separate closure function not working"  

def test_minlength_docstring_changing_minlength2():
    check_func1, ___ = check_function_min_length_docstring(5)
    def func1():
        '''
        docstring not sufficient
        '''
        pass
    def func2():
        '''
        this function accepts 'x' as input and gives 'y' as an input, this docstring is sufficiently long
        '''
        pass
    assert check_func1(func1) == True,"changing the minimum length using the decorator function not working" 
    assert check_func1(func2) == True,"changing the minimum length using the decorator function not working"
    check_func2, ___ = check_function_min_length_docstring(50)
    assert check_func2(func1) == False,"changing the minimum length using the decorator function not working" 
    assert check_func2(func2) == True,"changing the minimum length using the decorator function not working"
    check_func3, ___ = check_function_min_length_docstring(200)
    assert check_func3(func1) == False,"changing the minimum length using the decorator function not working" 
    assert check_func3(func2) == False,"changing the minimum length using the decorator function not working"
    
def test_minlength_docstring_function_param_types():
    with pytest.raises(TypeError):
        check_func, ___ = check_function_min_length_docstring(50, 'aabc')
    with pytest.raises(TypeError):
        check_func, ___ = check_function_min_length_docstring(50, 74,'34', hub = 90)
    with pytest.raises(TypeError):
        check_func, ___ = check_function_min_length_docstring('hojlfds')
    with pytest.raises(TypeError):
        check_func, ___ = check_function_min_length_docstring([1,2,3])   
        
def test_minlength_docstring_closure_function_params():
    check_func, change_min_length = check_function_min_length_docstring()
    def func2():
        '''
        this function accepts 'x' as input and gives 'y' as an input, this docstring is sufficiently long
        '''
        pass
    with pytest.raises(TypeError):
        check_func(123)
    with pytest.raises(TypeError):
        check_func(func2, 1345,bun = 'yes')
    with pytest.raises(TypeError):
        change_min_length('ada')
    with pytest.raises(ValueError):
        change_min_length(-8)
    with pytest.raises(TypeError):
        change_min_length(32,'aga', foo = 'bar')
        
    
def test_fibonacci_function_exist():
    assert hasattr(session6, "fibonacci"), "check_function_min_length_docstring function missing!"
    
def test_fibonacci_input_params():
    with pytest.raises(TypeError):
        fib = fibonacci(1234, foo='bar')
    with pytest.raises(TypeError):
        fib = fibonacci(1234)
    with pytest.raises(TypeError):
        fib = fibonacci()
        fib('adga')
    with pytest.raises(ValueError):
        fib = fibonacci()
        fib(-7)

def test_fibonacci_final_output():
    fib = fibonacci()
    assert fib(1) == 0 , 'output is not correct'
    assert fib(2) == 1, 'output is not correct'
    assert fib(3) == 1, 'output is not correct'
    assert fib(10) == 34, 'output is not correct'
    assert fib(15) == 377, 'output is not correct'
    
def test_function_counter_exist():
    assert hasattr(session6, "counter"), "counter function missing in the file"
    
def test_function_counter_input_params():
    def x():
        pass
    with pytest.raises(TypeError):
        count = counter('asffa')
    with pytest.raises(TypeError):
        count = counter(x, 'agaqq', foo = 'bar')

def test_function_counter_final_output():
    def x():
        return 1
    x_counter = counter(x)
    result, count = x_counter()
    assert count == 1 , 'counter function not working correctly'
    result, count = x_counter()
    assert count == 2 , 'counter function not working correctly'
    
def test_count_add_mul_div_exist():
    assert hasattr(session6, "counter_add_mul_div"), "counter function for add, mul and div missing in the file"
    
def test_count_add_mul_div_params_init():
    with pytest.raises(TypeError):
        count_add, count_mul, count_div, count_dic = counter_add_mul_div('adga')
    with pytest.raises(TypeError):
        count_add, count_mul, count_div, count_dic = counter_add_mul_div(1234)
    with pytest.raises(TypeError):
        count_add, count_mul, count_div, count_dic = counter_add_mul_div('adga', foo = 'bar')
    count_add, count_mul, count_div, count_dic  = counter_add_mul_div()
    
def test_count_add_mul_div_func_param():
    count_add, count_mul, count_div, count_dic  = counter_add_mul_div() 
    with pytest.raises(TypeError):
        answer, count_dict = count_add('afa', 78)
    with pytest.raises(TypeError):
        answer, count_dict = count_add('afa', 'gagfs')
    with pytest.raises(TypeError):
        answer, count_dict = count_add(1, 2, 32)
    with pytest.raises(TypeError):
        answer, count_dict = count_add(1, 2, foo = 'bar')
    with pytest.raises(TypeError):
        answer, count_dict = count_mul('afa', 78)
    with pytest.raises(TypeError):
        answer, count_dict = count_mul('afa', 'gagfs')
    with pytest.raises(TypeError):
        answer, count_dict = count_mul(1, 2, 32)
    with pytest.raises(TypeError):
        answer, count_dict = count_mul(1, 2, foo = 'bar')
    with pytest.raises(TypeError):
        answer, count_dict = count_div('afa', 78)
    with pytest.raises(TypeError):
        answer, count_dict = count_div('afa', 'gagfs')
    with pytest.raises(TypeError):
        answer, count_dict = count_div(1, 2, 32)
    with pytest.raises(TypeError):
        answer, count_dict = count_div(1, 2, foo = 'bar')
        
def test_count_add_mul_div_functionality_add():
    count_add, count_mul, count_div, count_dic  = counter_add_mul_div() 
    answer, count_dic = count_add(9,6)
    assert answer == 15, 'function not working properly'
    assert count_dic['count_add'] == 1, 'count part of add function not working properly'
    answer, count_dic = count_add(-78,6)
    assert answer == -72, 'function not working properly'
    assert count_dic['count_add'] == 2, 'count part of add function not working properly'
    answer, count_dic = count_add(1000000000000,7000000000000)
    assert answer == 8000000000000, 'function not working properly'
    assert count_dic['count_add'] == 3, 'count part of add function not working properly'
    answer, count_dic = count_add(-1000000000000,-7000000000000)
    assert answer == -8000000000000, 'function not working properly'
    assert count_dic['count_add'] == 4, 'count part of add function not working properly'
    for i  in range(100000):
        answer, count_dic = count_add(9,6)
    assert count_dic['count_add'] == 100004, 'count part not working'
    

def test_count_add_mul_div_functionality_mul():
    count_add, count_mul, count_div, count_dic  = counter_add_mul_div()
    answer, count_dic = count_mul(9,6)
    assert answer == 54, 'mul function not working properly'
    assert count_dic['count_mul'] == 1, 'count part of mul function not working properly'
    answer, count_dic = count_mul(0,10000000000000)
    assert answer == 0, 'mul function not working properly'
    assert count_dic['count_mul'] == 2, 'count part of mul function not working properly'
    answer, count_dic = count_mul(200000000,200000000)
    assert answer == 40000000000000000, 'mul function not working properly'
    assert count_dic['count_mul'] == 3, 'count part of mul function not working properly'
    answer, count_dic = count_mul(-10000,67)
    assert answer == -670000, 'mul function not working properly'
    assert count_dic['count_mul'] == 4, 'count part of mul function not working properly'
    for i  in range(100000):
        answer, count_dic = count_mul(9,6)
    assert count_dic['count_mul'] == 100004, 'count part not working'
        
    

def test_count_add_mul_div_functionality_div():
    count_add, count_mul, count_div, count_dic  = counter_add_mul_div()
    answer, count_dic = count_div(12,6)
    assert answer == 2, 'div function not working properly'
    assert count_dic['count_div'] == 1, 'count part of div function not working properly'
    answer, count_dic = count_div(10000000000,10000)
    assert answer == 1000000, 'div function not working properly'
    assert count_dic['count_div'] == 2, 'count part of div function not working properly'
    answer, count_dic = count_div(-10000000000,10000)
    assert answer == -1000000, 'div function not working properly'
    assert count_dic['count_div'] == 3, 'count part of div function not working properly'
    answer, count_dic = count_div(-5,2)
    assert answer == -2.5, 'div function not working properly'
    assert count_dic['count_div'] == 4, 'count part of div function not working properly'
    with pytest.raises(ZeroDivisionError):
        answer, count_dic = count_div(-5,0)
    

def test_count_add_mul_div_functionality_counter():
    count_add, count_mul, count_div, count_dic  = counter_add_mul_div()
    for i  in range(16843):
        answer, count_dic = count_add(9,6)
    for i  in range(41521):
        answer, count_dic = count_mul(9,6)
    for i  in range(51154):
        answer, count_dic = count_div(9,6)
    assert count_dic['count_add'] == 16843, 'count for add function not working properly'
    assert count_dic['count_mul'] == 41521 , 'count for mul function not working properly'
    assert count_dic['count_div'] == 51154 , 'count for div function not working properly'
    
# defining function for testing the counter for the 3 functions

def func1(a: int, *, foo, **kwargs):
    '''this is function 1'''
    return a

def func2(a: int, *, foo = 'bar', **kwargs):
    '''this is function 2'''
    return a

def func3(a: int, foo, *args,  **kwargs):
    '''this is function 3'''
    return a

def test_3_function_counter_exist():
    assert hasattr(session6, "counter_3_functions"), "counter function for add, mul and div missing in the file"
    
def test_3_function_counter_init():
    func1_test, func2_test, func3_test, count_dic = counter_3_functions(func1, func2, func3)
    with pytest.raises(TypeError):
        func1_test, func2_test, func3_test, count_dic = counter_3_functions(func1, func2)
    with pytest.raises(TypeError):
        func1_test, func2_test, func3_test, count_dic = counter_3_functions(func1, func2, '78987')
    with pytest.raises(TypeError):
        func1_test, func2_test, func3_test, count_dic = counter_3_functions(6789, func2, '78987')
    with pytest.raises(TypeError):
         func1_test, func2_test, func3_test, count_dic = counter_3_functions(func1, func2, func3, 'func1_name', 6787)

def test_3_function_counter_func1_init():
    func1_test, func2_test, func3_test, count_dic = counter_3_functions(func1, func2, func3)
    assert str(func1_test.__doc__).__contains__('function 1'), ' information of the original function is not passed to the closure function'
    assert func1_test.__name__.__contains__('func1'), ' information of the original function is not passed to the closure function'

def test_3_function_counter_func2_init():
    func1_test, func2_test, func3_test, count_dic = counter_3_functions(func1, func2, func3)
    assert str(func2_test.__doc__).__contains__('function 2'), ' information of the original function is not passed to the closure function'
    assert func2_test.__name__.__contains__('func2'), ' information of the original function is not passed to the closure function'

def test_3_function_counter_func3_init(): ##check both the presence fo doctring as well the input required
    func1_test, func2_test, func3_test, count_dic = counter_3_functions(func1, func2, func3)
    assert str(func3_test.__doc__).__contains__('function 3'), ' information of the original function is not passed to the closure function'
    assert func3_test.__name__.__contains__('func3'), ' information of the original function is not passed to the closure function'

def test_3_function_counter_working():
    func1_test, func2_test, func3_test, count_dic = counter_3_functions(func1, func2, func3)
    for i in range(10000):
        func1_test(1, foo = 'bar')
    assert count_dic['func1'] == 10000, 'function1 counter not working'
    for i in range(12343):
        func2_test(1, xyz = 'abc')
    assert count_dic['func1'] == 10000, 'function1 counter not working'
    assert count_dic['func2'] == 12343, 'function2 counter not working'
    for i in range(87678):
        func3_test(1, foo = 'gasf', xyz = 'abc')
    assert count_dic['func1'] == 10000, 'function1 counter not working'
    assert count_dic['func2'] == 12343, 'function2 counter not working'
    assert count_dic['func3'] == 87678, 'function1 counter not working'
    