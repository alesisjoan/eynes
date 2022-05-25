from math import pi as PI_NUMBER


class Shape(object):

    def get_area(self):
        "This will be defined in the subclass"
        pass

    def get_perimeter(self):
        "This will be defined in the subclass"
        pass


class Circle(Shape):

    def __str__(self):
        return 'Circle with a radio of %.4f' % float(self.radio)

    def __init__(self, radio):
        self.radio = radio

    def _check_radio(self, radio):
        if type(radio) not in [int, float] or radio <= 0:
            raise Exception("Please, set a radio greater than 0.")

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, value):
        self._check_radio(value)
        self._radio = value

    def multiply(self, multiplier):
        if type(multiplier) not in [int, float] or multiplier <= 0:
            raise Exception("Please, set a multiplier greater than 0.")
        return Circle(self.radio * multiplier)

    def get_area(self):
        return PI_NUMBER * (self.radio * self.radio)

    def get_perimeter(self):
        return PI_NUMBER * (self.radio * 2)


if __name__ == '__main__':
    circle = Circle(1)
    print(circle)
    print('Perimeter %.2f ' % circle.get_perimeter())
    print('Area %.2f ' % circle.get_area())
    new_circle = circle.multiply(2)
    print('Multiply by 2:')
    print(new_circle)
