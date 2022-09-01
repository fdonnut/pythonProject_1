# import fib
# import rects
# import logging
#
# logging.basicConfig(
#     format='%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s',
#     level=logging.INFO)
#
# # print(fib.fib_list(21))
# # print(fib.fib(7))
# # print('Rect 3 4', rects.perimeter(3, 4))
# # print()
#
#
# def fails(a, b):
#     logging.warning('entered fails')
#     a / b
#
#
# try:
#     fails(2, 0)
#     # 1 / 0
#     # print('zero')
#     # '42' + 10
#     # print('type')
#     # [1, 2][2]
#     # print('index')
#     # exc = Exception('spam', 'eggs')
#     # print(exc)
#     # raise exc
# except Exception:
#     # print('got exception', type(e), e.args)
#     # logging.error('got exception %s %s', type(e), e.args, exc_info=e)
#     logging.exception('got exception!')
#
# # print('i\'m working!')
# logging.error('working!')
import logging


class Human:
    pass


h = Human()
h.name = 'john'
h.age = 42


def print_human(human):
    print(Human)
    print(human.name, human.age)


print_human(h)


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, point):
        if not isinstance(point, Point):
            raise TypeError('please provide Point instance')
        return Point(self.x + point.x, self.y + point.y)

    def __iadd__(self, other):
        if not isinstance(other, Point):
            raise TypeError('please provide Point instance')
        self.x += other.x
        self.y += other.y
        return self

    __add__ = add
    # def __add__(self, other):
    #     return self.add(other)

    def __eq__(self, other):
        print('Called eq')
        if not isinstance(other, Point):
            logging.warning('Please provide Point instance for comparison')
            return False
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        print('Called gt')
        if not isinstance(other, Point):
            raise TypeError('Please provide Point instance')
        return self.x > other.x and self.y > other.y

    def __str__(self):
        return f'<Point {self.x}, {self.y}>'


p1 = Point(2, 3)
p2 = Point(5, -7)
print(isinstance(p1, Human))
p3 = p1 + p2
p3 = p1.__add__(p2)
print(p1.add(p2))
p3 += Point(1, 2)
p3 = p3.__iadd__(Point(1, 2))
print(p3)
print(p1 == p2)
print(p1 > p2)


class Vehicle:
    speed = 0
    age = 0

    def move(self):
        return f'Moving with speed {self.speed}'


class Car(Vehicle):
    def __init__(self):
        self.speed = 10

    def move(self):
        s = super().move()
        print('Previous:', s)
        # return f'Driving car with speed {self.speed}'
        s += ' [it is a car]'
        return s


class SportCar(Car):
    speed = 50

    def __init__(self):
        print('Current speed is', self.speed)
        super().__init__()
        print('And now current speed is', self.speed)
        self.speed = 70


class ECar(Car):
    charge = 50

    def state(self):
        return 'Needs charge' if self.charge < 10 else 'OK'


class PlaybackError(Exception):
    pass


class MorePlaybackErrors(PlaybackError):
    pass


class SportECar(SportCar, ECar):

    def play(self):
        print('Trying to play')
        raise PlaybackError

    def play2(self):
        raise MorePlaybackErrors


class Ship(Vehicle):

    def __init__(self):
        self.tubes = 3

    def sound(self):
        return f'Tu Tu from {self.tubes} tubes'


# v = Vehicle()
# car = Car()
# ship = Ship()
# s_car = SportCar()
e_car = ECar()
e_car.charge = 7
se_car = SportECar()
# print(Car, Car.__bases__, car, car.__class__)
# print(v.speed)
# print(car.speed)
# print(v.move())
# print(car.move())
# print(ship.sound())
# print(s_car.move())
print(e_car.state())
print(se_car.speed, se_car.charge, se_car.state())
print(se_car.__class__)
print(isinstance(se_car, (Car, SportECar, Vehicle)))
try:
    se_car.play()
except Exception:
    print('No play')

try:
    se_car.play2()
except MorePlaybackErrors:
    print('No play 2')
except PlaybackError:
    print('No play 1')
