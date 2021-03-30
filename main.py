from sympy import var
from sympy import sympify
from sympy.utilities.lambdify import lambdify
import time
import math
import numpy as np

from VectorizationIntegrate import Integrate


def single_integral():
    # Ask for the integrand as input, and convert it into a processable lambda function
    x = var('x')
    print("\nThis program uses cartesian coordinates. Please only use 'x' as the variable.")
    user_input = str(input("Enter the integrand using arithmetic Python expressions (ex. 'x ** -1'): "))
    expr = sympify(user_input)
    f = lambdify(x, expr)
    return f, expr


def double_integral():
    # Ask for the integrand as input, and convert it into a processable lambda function
    x = var('x')
    y = var('y')
    print("\nThis program uses cartesian coordinates. Please only use 'x' and 'y' as variables.")
    user_input = str(input("Enter the integrand using arithmetic Python expressions (ex. 'exp(-(x ** 2 + y ** 2))'): "))
    expr = sympify(user_input)
    f = lambdify([x, y], expr)
    return f, expr


if __name__ == '__main__':
    print("This program can be used to approximate integrals numerically in one and two dimensions.")
    print()
    while True:
        choice = str(input("Would you like to compute a single or double integral? Enter 'single' or 'double': "))
        choice = choice.strip()
        if choice.lower() != "single" and choice.lower() != "double":
            print("\nEnter a valid command.")
            continue

        elif choice == "single":

            # Get the integrand, limits, and desired precision from user
            single_integral, expression = single_integral()
            string = str(input(
                "\nEnter the lower limit, upper limit, and the required degree of precision separated by commas (ex. '0,math.pi,1'): "))
            split = string.split(",")
            lower_limit = split[0]
            upper_limit = split[1]
            precision = split[2]

            # Approximate the integral and calculate error
            start_time = time.perf_counter()
            integral = Integrate(single_integral, expression)
            result = integral.single_integral(eval(lower_limit), eval(upper_limit), eval(precision))
            print("\nThe result is", result)
            if integral.error is None:
                print("\nThe accuracy could not be calculated. You have probably entered an unsupported integral type.")
            else:
                print("\nThe accuracy of this result is (at least) {:.2e}".format(integral.error))
            print("\nThe calculation ran for %s seconds" % (time.perf_counter() - start_time))
            break

        elif choice == "double":

            # Get the integrand, limits, and desired precision from user
            double_integral, expression = double_integral()
            limits_list = []
            string = str(input("\nEnter the inner set of limits separated by a comma (ex. lower,upper): "))
            split = string.split(",")
            while len(split) != 2:
                print("\nIncorrect amount of variables entered, returning")
                string = str(input("\nEnter the inner set of limits separated by a comma (ex. lower,upper): "))
                split = string.split(",")
            split[0] = eval(split[0])
            split[1] = eval(split[1])
            limits_list.append(split)
            string = str(input("\nEnter the outer set of limits separated by a comma (ex. lower,upper): "))
            split = string.split(",")
            while len(split) != 2:
                print("\nIncorrect amount of variables entered, returning")
                string = str(input("\nEnter the outer set of limits separated by a comma (ex. lower,upper): "))
                split = string.split(",")
            split[0] = eval(split[0])
            split[1] = eval(split[1])
            limits_list.append(split)
            precision = int(input("\nEnter the required degree of precision (integer): "))

            # Approximate the integral and calculate error
            start_time = time.perf_counter()
            integral = Integrate(double_integral, expression)
            result = integral.double_integral(limits_list, precision)
            print("\nThe result is", result)
            if integral.error is None:
                print("\nThe accuracy could not be calculated. You have probably entered an unsupported integral type.")
            else:
                print("\nThe accuracy of this result is (at least) {:.2e}".format(integral.error))
            print("\nThe calculation ran for %s seconds" % (time.perf_counter() - start_time))
            break
