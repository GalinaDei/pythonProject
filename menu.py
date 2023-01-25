import logging
import calc_lib
import logger


def greeting():
    print("Hello! Calculator is ready to work.")
    logging.info("Start program")


def mode_menu():
    while True:
        mode = input("Enter\n"
                     "1 - rational\n"
                     "2 - complex\n"
                     "3 = exit\n")
        match mode:
            case "1":
                rational_operations_menu()
            case "2":
                complex_operations_menu()
            case "3":
                break
            case _:
                logging.warning("Wrong item selected")
                print("Error")


def rational_operations_menu():
    while True:
        operation = input("Enter\n"
                          "1 - summ\n"
                          "2 - division\n"
                          "3 - multiplication\n"
                          "4 - subtraction\n"
                          "5 - exponentiation\n"
                          "6 - square root\n"
                          "7 - previous menu\n")
        match operation:
            case "1":
                calc_lib.sum()
            case "2":
                menu_division()
            case "3":
                calc_lib.multiplication()
            case "4":
                calc_lib.subtraction()
            case "5":
                calc_lib.exponential()
            case "6":
                calc_lib.square_root()
            case "7":
                break
            case _:
                logging.warning("Wrong item selected")
                print("Error")


def complex_operations_menu():
    global y
    while True:
        operation = input("Enter\n"
                          "1 - summ\n"
                          "2 - division\n"
                          "3 - multiplication\n"
                          "4 - subtraction\n"
                          "5 - exponentiation\n"
                          "6 - square root\n"
                          "7 - previous menu\n")
        match operation:
            case "1":
                calc_lib.complex_sum()
            case "2":
                calc_lib.complex_division()
            case "3":
                calc_lib.complex_multiplication()
            case "4":
                calc_lib.complex_subtraction()
            case "5":
                calc_lib.complex_exponential()
            case "6":
                calc_lib.complex_square_root()
            case "7":
                break
            case _:
                logging.warning("Wrong item selected")
                print("Error")

def menu_division():
    while True:
        operation = input("Enter\n"
                          "1 - integer division\n"
                          "2 - division with reminder\n"
                          "3 - reminder of division\n"
                          "4 - previous menu\n")
        match operation:
            case "1":
                calc_lib.integer_division()
            case "2":
                calc_lib.division_with_remainder()
            case "3":
                calc_lib.remainder_of_division()
            case "4":
                break
            case _:
                logging.warning("Wrong item selected")
                print("Error")