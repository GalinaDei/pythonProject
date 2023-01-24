import logging

import exceptions
import get_value


def convert_toComplex(real, imag):
    return complex(real, imag)


def sum():
    x = get_value.get_rational_value(input("Enter operand 1 "))
    if x is not None:
        y = get_value.get_rational_value(input("Enter operand 2 "))
        if y is not None:
            logging.info(f" {x} + {y} = {x + y}")
            print(f"Sum = {x + y}")
    else:
        return
    print(x)


def integer_division():
    global y
    x = get_value.get_rational_value(input("Enter operand 1 "))
    if x is not None:
        y = get_value.get_rational_value(input("Enter operand 2 "))
        result = exceptions.zero_test(y)
        if y is not None and result:
            logging.info(f" {x} // {y} = {round(x // y)}")
            print(f"Integer division result {round(x // y)}")
    else:
        return


def division_with_remainder():
    x = get_value.get_rational_value(input("Enter operand 1 "))
    if x is not None:
        y = get_value.get_rational_value(input("Enter operand 2 "))
        result = exceptions.zero_test(y)
        if y is not None and result:
            logging.info(f" {x} / {y} = {(x / y)}")
            print(f"Division with remainder result {(x / y)}")
    else:
        return


def remainder_of_division():
    x = get_value.get_rational_value(input("Enter operand 1 "))
    if x is not None:
        y = get_value.get_rational_value(input("Enter operand 2 "))
        result = exceptions.zero_test(y)
        if y is not None and result:
            logging.info(f" {x} % {y} = {x % y}")
            print(f"Division with remainder result {x % y}")
    else:
        return


def multiplication():
    x = get_value.get_rational_value(input("Enter operand 1 "))
    if x is not None:
        y = get_value.get_rational_value(input("Enter operand 2 "))
        if y is not None:
            logging.info(f" {x} * {y} = {x * y}")
            print(f"Multiplication result {x * y}")
    else:
        return


def subtraction():
    x = get_value.get_rational_value(input("Enter operand 1 "))
    if x is not None:
        y = get_value.get_rational_value(input("Enter operand 2 "))
        if y is not None:
            logging.info(f" {x} - {y} = {round(x - y)}")
            print(f"Subtraction result {round(x - y)}")
    else:
        return


def exponential():
    x = get_value.get_rational_value(input("Enter the basis "))
    if x is not None:
        y = get_value.get_rational_value(input("Enter degree indicator "))
        if y is not None:
            if x == 0 and y == 0:
                logging.info(f" {x} ^ {y} = {0}")
                print(f"Exponential result {0}")
            elif x != 0 and y == 0:
                logging.info(f" {x} ^ {y} = {1}")
                print(f"Exponential result 1")
            elif x != 0 and y < 0:
                logging.info(f" {x} ^ {y} = {1 / (x ** (-1 * y))}")
                print(f"Exponential result {1 / (x ** (-1 * y))}")
            else:
                logging.info(f" {x} ^ {y} = {x ** y}")
                print(f"Exponential result {x ** y}")
    else:
        return


def square_root():
    from math import sqrt
    x = get_value.get_rational_value(input("Enter the basis "))
    if x is not None:
        result = exceptions.negative_test(x)
        if result:
            logging.info(f"sqrt from {x}  = {sqrt(x)}")
            print(f"square root result {sqrt(x)}")
    else:
        return


def complex_sum():
    x = get_value.get_complex_value(input("Enter real 1 "), input("Enter imag 2 "))
    if x is not None:
        y = get_value.get_complex_value(input("Enter real 2 "), input("Enter imag 2 "))
        if y is not None:
            logging.info(f" {x} + {y} = {x + y}")
            print(f"Sum = {x + y}")
    else:
        return
    print(x)


def complex_division():
    global y
    x = get_value.get_complex_value(input("Enter real 1 "), input("Enter imag 2 "))
    if x is not None:
        y = get_value.get_complex_value(input("Enter real 2 "), input("Enter imag 2 "))
        if y is not None:
            result = exceptions.zero_test(y)
            if y is not None and result:
                logging.info(f" {x} / {y} = {x / y}")
                print(f"Integer division result {x / y}")
    else:
        return


def complex_multiplication():
    x = get_value.get_complex_value(input("Enter real 1 "), input("Enter imag 2 "))
    if x is not None:
        y = get_value.get_complex_value(input("Enter real 2 "), input("Enter imag 2 "))
        if y is not None:
            logging.info(f" {x} * {y} = {x * y}")
            print(f"Multiplication result {x * y}")
    else:
        return


def complex_subtraction():
    x = get_value.get_complex_value(input("Enter real 1 "), input("Enter imag 2 "))
    if x is not None:
        y = get_value.get_complex_value(input("Enter real 2 "), input("Enter imag 2 "))
        if y is not None:
            logging.info(f" {x} - {y} = {x - y}")
            print(f"Subtraction result {x - y}")
    else:
        return


def complex_exponential():
    x = get_value.get_complex_value(input("Enter real 1 "), input("Enter imag 2 "))
    if x is not None:
        y = get_value.get_complex_value(input("Enter real 2 "), input("Enter imag 2 "))
        if y is not None:
            logging.info(f" {x} ^ {y} = {x ** y}")
            print(f"Exponential result {x ** y}")
    else:
        return


def complex_square_root():
    x = get_value.get_complex_value(input("Enter real 1 "), input("Enter imag 2 "))
    if x is not None:
        logging.info(f"sqrt from {x}  = {x**0.5}")
        print(f"square root result {x**0.5}")
    else:
        return
