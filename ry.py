import uuid
import random

def rollDice(sides):
    result = random.randint(1,sides)
    return result

class  Employee(object):
    def __init__(self):
        ##self.payRate

        genderRoll = rollDice(2)
        if genderRoll == 1:
            self.gender = 'male'
        else:
            self.gender = 'female'

        raceRoll = rollDice(3)
        if raceRoll == 3:
            #under-represented minority
            self.race = 'URM'
        elif raceRoll == 2:
            #well-represented minority
            self.race == 'WRM'
        else:
            #over-represented majority
            self.race == 'ORM'


class Company(object):
    def __init__(self):
        self.industry = raw_input("With what industry is your company associated?")
        self.name = raw_input("What is your company's name?")
        self.employees = {}
    def interview(employee):
        Employee.interScire
    def hire(self, Employee):
        self.employees.append(Employee)



class Account(object):
    def __init__(self, initial_balance=0):
        ##self.number = uuid.uuid()
        self.Employee= input("Name on the account?")
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

