import numpy as np
from scipy.integrate import trapezoid as sint
from sympy import *

from IntegrationError import IntegrationError


class Integrate:
    def __init__(self, function, expression):
        self.function = function
        self.expression = expression
        self.error = 0

    def single_integral(self, lower, upper, precision):
        xs = np.linspace(lower, upper, int(precision))
        y = self.function(xs)
        xx = symbols('x')

        # Use trapezoidal rule to approximate a single integral.
        try:
            approximation = sint(y, xs)
        except ValueError:
            print("\nNumerical integration did not succeed. Proceeding with symbolic integration:")
            integral = integrate(self.expression, (xx, lower, upper))
            if integral != nan:
                return integral
            else:
                print("\nSymbolic integration did not succeed.")
                self.error = None
                return None

        # Use symbolic integration to try to calculate error
        integral = integrate(self.expression, (xx, lower, upper))
        if integral == nan:
            self.error = None
        else:
            self.error = integral.evalf() - approximation

        # Return the approximation
        return approximation

    def double_integral(self, limit_list, precision):
        if type(limit_list) != list:
            raise IntegrationError("The bounds must be given as a list of lists")
        x_list, y_list = limit_list
        (a, b), (c, d) = x_list, y_list
        xs, ys = np.linspace(a, b, precision), np.linspace(c, d, precision)
        zs = self.function(xs[:, None], ys)
        xx, yy = symbols('x y')

        # Attempt trapezoidal rule to approximate a double integral.
        try:
            approximation = sint(sint(zs, ys), xs)
        except ValueError:
            print("\nNumerical integration did not succeed. Proceeding with symbolic integration:")
            integral = integrate(self.expression, (xx, a, b), (yy, c, d))
            if integral != nan:
                return integral
            else:
                print("\nSymbolic integration did not succeed.")
                self.error = None
                return None

        # Attempt symbolic integration to calculate error
        integral = integrate(self.expression, (xx, a, b), (yy, c, d))
        if integral == nan:
            self.error = None
        else:
            self.error = integral.evalf() - approximation

        # Return the approximation
        return approximation
