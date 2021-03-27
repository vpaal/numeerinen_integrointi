import numpy as np
from IntegrationError import IntegrationError


class Integrate:
    def __init__(self, function):
        self.function = function
        self.error = 0
        self.sign = 1

    def single_integral(self, lower, upper, precision):

        # Use trapezoidal rule to approximate a single integral.
        if lower > upper:
            lower, upper = upper, lower
            self.sign = -1
        number_of_points = (upper - lower) * precision
        xs = np.linspace(lower, upper, int(number_of_points))
        integral = 0
        super_sum = 0
        sub_sum = 0
        for index in range(len(xs) - 1):
            delta = xs[index + 1] - xs[index]
            try:
                y1 = self.function(xs[index])
                sub_area = y1 * delta
                y2 = self.function(xs[index + 1])
                super_area = y2 * delta

                area = (y2 + y1) / 2 * delta
                integral += area
                sub_sum += sub_area
                super_sum += super_area
            except ZeroDivisionError:
                print("\nAvoided pole")

        self.error = super_sum - sub_sum
        return self.sign * integral

    def double_integral(self, limit_list, precision):

        # Use trapezoidal rule to approximate a double integral.
        if type(limit_list) != list:
            raise IntegrationError("The bounds must be given as a list of lists")
        x_list, y_list = limit_list
        (a, b), (c, d) = x_list, y_list
        x_points, y_points = (b - a) * precision, (d - c) * precision
        xs, ys = np.linspace(a, b, int(x_points)), np.linspace(c, d, int(y_points))
        integral = 0
        sub_sum = 0
        super_sum = 0
        for i in range(len(xs) - 1):
            delta_x = xs[i + 1] - xs[i]
            for j in range(len(ys) - 1):
                delta_y = ys[j + 1] - ys[j]
                delta = delta_x * delta_y
                try:
                    f1 = self.function(xs[i], ys[j])
                    sub_area = f1 * delta
                    f2 = self.function(xs[i + 1], ys[j + 1])
                    super_area = f2 * delta

                    area = (f2 + f1) / 2 * delta
                    integral += area
                    sub_sum += sub_area
                    super_sum += super_area
                except ZeroDivisionError:
                    print("\nAvoided pole\n")

        self.error = super_sum - sub_sum
        return integral
