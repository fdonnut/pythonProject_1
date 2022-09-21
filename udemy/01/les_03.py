# oop
class Car:
    wheels = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print('car is created')

    def drive(self, city):
        print(f'{self.name} is driving to {city}')

    def change_color(self, new_color):
        self.color = new_color
        print('color is changed to ' + new_color)

    def load_cargo(self, weight):
        print('the cargo is loaded. weight is ' + str(weight) + ' kg.')


mazda_car = Car(name='mazda_cx7', color='red', year=2017, is_crashed=True)
bmw_car = Car('bmw', 'black', 2018, False)
opel_car = Car('opel tigra', 'grey', 1999, is_crashed=True)

print(mazda_car.name, mazda_car.color, mazda_car.year, mazda_car.is_crashed, mazda_car.wheels)
print(bmw_car.name, bmw_car.color, bmw_car.year, bmw_car.is_crashed)

wheels_of_3_cars = Car.wheels * 3
print(wheels_of_3_cars)
opel_car.drive('moscow')
bmw_car.drive('spb')
mazda_car.drive('tynda')
mazda_car.change_color('green')
print(mazda_car.name, mazda_car.color)


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.circumference = 2 * Circle.pi * self.radius

    def get_area(self):
        return Circle.pi * (self.radius ** 2)

    # def get_circumference(self):
    #     return 2 * self.pi * self.radius


circle = Circle(10)
print(circle.get_area())
# print(circle.get_circumference())
print(circle.circumference)


class Gamer:
    active_gamers = 0

    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers

    @classmethod
    def gamer_from_string(cls, data_string):
        name, age, level, points = data_string.split(',')
        return cls(name, int(age), int(level), int(points))

    def __init__(self, name, age, level, points):
        self.name = name
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def log_out(self):
        Gamer.active_gamers -= 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level_permission(self):
        if self.is_adult():
            print('you can go to adult level')
        else:
            print("you can't go to adult level")


gamer_1 = Gamer('hell_boy', 23, 5, 13)
gamer_2 = Gamer('harry_potter', 13, 7, 34)

print(gamer_1.name, gamer_1.age)
gamer_1.get_adult_level_permission()

print(gamer_2.name, gamer_2.age)
gamer_2.get_adult_level_permission()

print(Gamer.active_gamers)
# gamer_1.log_out()
# print(Gamer.get_active_gamers())

gamer_3 = Gamer.gamer_from_string('super_man, 34, 3, 12')
gamer_4 = Gamer.gamer_from_string('super_girl, 25, 4, 21')
print(gamer_3.name, gamer_3.age)
gamer_3.get_adult_level_permission()
print(gamer_4.name, gamer_4.age)
gamer_4.get_adult_level_permission()
print(Gamer.get_active_gamers())

my_dict = dict.fromkeys((1, 2, 3), 'any')
print(my_dict)


# inheritance
class Truck(Car):
    wheels = 6

    def __init__(self, name, color, year, is_crashed):
        Car.__init__(self, name, color, year, is_crashed)
        print('truck is created')

    def drive(self, city):
        print('truck ' + self.name + ' is driving to ' + city)


man_truck = Truck('man', 'white', 2015, False)
man_truck.drive('novgorod')
print(man_truck.wheels)
print(man_truck.color)
man_truck.change_color('red')
print(man_truck.color)
man_truck.load_cargo(2000)


# polymorphism
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('class successor must implement this method')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def speak(self):
        print(self.name + ' is saying woof')


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def speak(self):
        print(self.name + ' is saying meow')


class Mouse(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def speak(self):
        print(self.name + ' is saying pee-pee-pee')


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def speak(self):
        print(self.name + ' is saying nothing')


spike = Dog('spike')
tom = Cat('tom')
jerry = Mouse('jerry')
freddy = Fish('freddy')

pet_list = [spike, tom, jerry]

for pet in pet_list:
    pet.speak()


def pet_voice(pet):
    pet.speak()


pet_voice(spike)
pet_voice(tom)
pet_voice(jerry)
pet_voice(freddy)


# multi_inheritance
class Swimmable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'hello! my name is {self.name} and i can swim')

    def swim(self):
        print("i'm swimming")


class Walkable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'hello! my name is {self.name} and i can walk')

    def walk(self):
        print("i'm walking")


class Flyable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'hello! my name is {self.name} and i can fly')

    def fly(self):
        print("i'm flying")


class GameCharacter(Swimmable, Walkable, Flyable):
    def __init__(self, name):
        self.name = name
        Swimmable.__init__(self, name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)

    def greeting(self):
        print(f'hello! my name is {self.name}')


boy = GameCharacter('jack')
boy.greeting()
boy.swim()
boy.walk()
boy.fly()
print(isinstance(boy, Swimmable))
print(isinstance(boy, Walkable))
print(isinstance(boy, Flyable))
print(isinstance(boy, GameCharacter))


# mro
class A:
    def some_method(self):
        print('method of class A')


class B(A):
    def some_method(self):
        print('method of class B')


class C(A):
    def some_method(self):
        print('method of class C')


class D(B, C):
    def some_method(self):
        print('method of class D')


some_object = D()
some_object.some_method()
print(D.__mro__)
help(D)


# magic methods
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

    def __len__(self):
        return self.age

    def __del__(self):
        print('person object with name ' + self.first_name + ' is deleted from memory')

    def __add__(self, other):
        return self.age + other.age


jack = Person('jack', 'white', 45)
jane = Person('jane', 'kit', 23)

print(jack)
print(len(jack))
print(jack + jane)

del jack
