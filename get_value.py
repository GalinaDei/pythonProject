import exceptions
import calc_lib


def get_rational_value(val=input()):

    result = exceptions.isdigit_test(val)
    if result:
        return float(val)
    else:
        return


def get_complex_value(val=input(), val1=input()):
    global real, imag
    result = exceptions.isdigit_test(val)
    result1 = exceptions.isdigit_test(val1)
    if result and result1:
        return calc_lib.convert_toComplex(float(val), float(val1))
    else:
        return

