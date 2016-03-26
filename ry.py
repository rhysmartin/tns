import uuid
import random

def rollDice(sides):
    result = random.randint(1,sides)
    return result

class  Employee(object):
    def __init__(self, name):
        self.name = name
        self.interviewScore = None
        self.payRate = None
        self.performanceScore = None
        genderRoll = rollDice(2)
        if genderRoll == 1:
            self.gender = 'male'
        elif genderRoll == 2:
            self.gender = 'female'
        else:
            self.gender = 'trans'

        raceRoll = rollDice(3)
        if raceRoll == 3:
            #under-represented minority
            self.race = 'URM'
        elif raceRoll == 2:
            #well-represented minority
            self.race = 'WRM'
        else:
            #over-represented majority
            self.race = 'ORM'


class Employer(object):
    def __init__(self, name):
        self.fairnessScore = None
        self.name = name
        self.industry = raw_input("With what industry is your company associated?")
        self.interviewees = []
        self.employees = []
    def interview(self, employee, score, decision=0):
        employee.interviewScore = score
        self.interviewees.append(employee)
        if decision == 1:
            self.employees.append(employee)

    def batch_interview(self, employees):
        for i in employees:
            ##this is hard-coded for now!
            self.interview(i, 100)

    def setPay(self, employee, rate):
        employee.payRate = rate

    def setPerformanceScore(self, employee, score):
        employee.payRate = score



"""class Account(object):
    def __init__(self, initial_balance=0):
        ##self.number = uuid.uuid()
        self.Employee= input("Name on the account?")
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount"""

