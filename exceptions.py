import logging


def isdigit_test(x):
    if x.replace(".","").strip("-").isdigit():
        return True
    else:
        print("Error. Invalid value of operand entered")
        logging.warning("Wrong value of operand entered")
        return False


def negative_test(x):
    if x < 0:
        print("Error. Invalid value of operand entered/ It cannot be negative")
        logging.warning("Wrong value of operand entered")
        return False
    else:
        return True


def zero_test(x):
    if x == 0:
        print("Error. Invalid value of operand entered. It cannot be divided on 0")
        logging.warning("Wrong value of operand entered")
        return False
    else:
        return True

