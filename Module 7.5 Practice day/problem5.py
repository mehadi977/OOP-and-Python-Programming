# Explain the difference between inheritance and composition with proper examples.
""" 
Inheritance ও Composition-এর মধ্যে পার্থক্য
পাইথনে Inheritance (উত্তরাধিকার) এবং Composition (সমন্বয়) হলো কোড পুনরায় ব্যবহার করার দুটি পদ্ধতি।
১. Inheritance কী?
Inheritance হলো এমন একটি পদ্ধতি, যেখানে একটি ক্লাস অন্য একটি ক্লাসের অ্যাট্রিবিউট ও মেথড গ্রহণ করতে পারে।

এটি “is-a” সম্পর্ক বোঝায়।

উদাহরণ: একটি Dog হলো একটি Animal।
"""

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


d = Dog()
d.eat()
d.bark()

""" 
২. Composition কী?
Composition হলো এমন একটি পদ্ধতি, যেখানে একটি ক্লাসের ভেতরে অন্য একটি ক্লাসের অবজেক্ট ব্যবহার করা হয়।

এটি “has-a” সম্পর্ক বোঝায়।

উদাহরণ: একটি Car-এর একটি Engine আছে।
"""
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")


c = Car()
c.start_car()