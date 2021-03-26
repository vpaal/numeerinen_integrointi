from numpy import sin, exp
import math
from sympy import var
from sympy import sympify
from sympy.utilities.lambdify import lambdify

from Integrate import Integrate


def single_integral():
    x = var('x')
    print("\nThis program uses cartesian coordinates. Please only use 'x' as the variable.")
    user_input = str(input("Enter the integrand using arithmetic Python expressions (ex. 'x ** -1'): "))
    expr = sympify(user_input)
    f = lambdify(x, expr)
    return f


def double_integral():
    x = var('x')
    y = var('y')
    print("\nThis program uses cartesian coordinates. Please only use 'x' and 'y' as variables.")
    user_input = str(input("Enter the integrand using arithmetic Python expressions (ex. 'exp(-(x ** 2 + y ** 2))'): "))
    expr = sympify(user_input)
    f = lambdify([x, y], expr)
    return f


if __name__ == '__main__':
    print("This program can be used to approximate integrals numerically in one and two dimensions.")
    print()
    while True:
        try:
            choice = str(input("Would you like to compute a single or double integral? Enter 'single' or 'double': "))
            choice = choice.strip()
            if choice != "single" and choice != "double":
                print("Enter a valid command.")
                continue
            elif choice == "single":
                single_integral = single_integral()
                string = str(input(
                    "\nEnter the lower limit, upper limit, and the required degree of precision separated by commas (ex. '0,math.pi,1'): "))
                split = string.split(",")
                lower_limit = split[0]
                upper_limit = split[1]
                precision = split[2]
                break
            elif choice == "double":
                double_integral = double_integral()
                limits_list = []
                string = str(input("\nEnter the first set of limits separated by a comma (ex. lower,upper): "))
                split = string.split(",")
                while len(split) != 2:
                    print("Incorrect amount of variables entered, returning")
                    string = str(input("\nEnter the first set of limits separated by a comma (ex. lower,upper): "))
                    split = string.split(",")
                split[0] = eval(split[0])
                split[1] = eval(split[1])
                limits_list.append(split)
                string = str(input("\nEnter the second set of limits separated by a comma (ex. lower,upper): "))
                split = string.split(",")
                while len(split) != 2:
                    print("Incorrect amount of variables entered, returning")
                    string = str(input("\nEnter the second set of limits separated by a comma (ex. lower,upper): "))
                    split = string.split(",")
                split[0] = eval(split[0])
                split[1] = eval(split[1])
                limits_list.append(split)
                precision = int(input("\nEnter the required degree of precision (integer): "))
                break
        except TypeError:
            print("Enter a valid command.")
            continue
    if choice == "single":
        integral = Integrate(single_integral)
        result = integral.single_integral(eval(lower_limit), eval(upper_limit), precision=eval(precision))
        print("\nThe result is", result)
        print("\nThe accuracy of this result is", integral.error)
    elif choice == "double":
        integral = Integrate(double_integral)
        result = integral.double_integral(limits_list, precision=precision)
        print("\nThe result is", result)
        print("\nThe accuracy of this result is", integral.error)





