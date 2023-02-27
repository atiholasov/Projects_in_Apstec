"""
2.X - 1 """















"""
2.3 - 5

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')


class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')


class Employee:
    def __init__(self, name, age, company_name, location):
        a = Person(name, age)
        self.personal_data = a
        b = Company(company_name, location)
        self.work = b
"""
"""
2.3 - 4

class CustomLabel:
    def __init__(self, text, **kwargs):
        self.text = text
        for kay,value in kwargs.items():
            #setattr(CustomLabel, kay, value)
            self.__dict__[kay] = value

    def config(self, **kwargs):
        for kay,value in kwargs.items():
            #setattr(CustomLabel, kay, value)
            self.__dict__[kay] = value
"""
"""
2.3 - 3 

persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]

class Worker:
    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        print(f'Worker {self.name}; passport-{self.passport}')

worker_objects = []

for i in range(len(persons)):
    men = Worker(persons[i][0], persons[i][1], persons[i][2], persons[i][3])
    worker_objects.append(men)
    men.get_info()

print(worker_objects)

"""
"""
2.3 - 2 
class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def peek(self):
        if self.is_empty():
            print("Empty Stack")
            return None
        else:
            return self.values[-1]

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.values)

    def pop(self):
        last_item = self.peek()
        if self.size() != 0:
            self.values.remove(last_item)
            return last_item

"""
"""
2.3 - 1
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        text = f'{self.name} is {self.age} years old'
        return text

    def speak(self, sound):
        return f'{self.name} says {sound}'
"""
"""
2.2 - 5
class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return self.last_name + ' ' + self.first_name

    def is_adult(self):
        return True if self.age >= 18 else False

"""
"""
2.2 - 4
class Zebra:
    color = 'белая'
    def which_stripe(self):
        print(f"Полоска {self.color}")
        if self.color == 'черная':
            self.color = 'белая'
        else:
            self.color = 'черная'

"""
"""
2.2 - 3
class SoccerPlayer:
    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assist=1):
        self.assists += assist

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')
"""
"""
2.2 - 2
class Laptop:
    def __init__(self, brand = "hp", model = ' ', price = 12000):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + " " + model

laptop1 = Laptop()
laptop2 = Laptop()
"""
"""
2.2 - 1 
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
"""
"""
2.1 - 6
class Point:

    def set_coordinates(self,x ,y ):
        self.x, self.y = x, y

    def get_distance(self, point_2):
        if type(self) != type(point_2):
            print("Передана не точка")
        else:
            dist = ((point_2.x-self.x)**2 + (point_2.y-self.y)**2)**(1/2)
            return dist

"""
"""
2.1 - 5
class Constructor:

    def add_atribute(self, name, eq_attr):
        setattr(self, name, eq_attr)

    def display(self):
        print(self.__dict__)

"""
"""
2.1 - 4
class Counter:

    def start_from(self, first_num = 0):
        self.sum = first_num

    def increment(self):
        self.sum += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.sum}')

    def reset(self):
        self.sum = 0

c1 = Counter()
c1.start_from()
c1.increment()
c1.display()
c1.reset()

"""
"""
2.1 - 3
class Robot:

    def set_name(self, name):
        self.name = name

    def say_hello(self):
        if hasattr(self, "name"):
            print(f"Hello, human! My name is {self.name}")
        else:
            print("У робота нет имени")
    def say_bye(self):
        print("See u later alligator")

r2d2 = Robot()
r2d2.set_name("r2d2")

"""
