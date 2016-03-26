class  Employee(object):
    def __init__(self, name, gender, race, interviewScore = None):
        self.name = name
        self.interviewScore = interviewScore

class Employer(object):
    def __init__(self, name):
        self.name = name
        self.fairScore_race = None
        self.fairScore_gender = None
        #self.industry = raw_input("With what industry is your company associated?")
        self.interviewees = []
        self.employees = []

    #methods to be called on employee(s)
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

    def setPerformance(self, employee, score):
        employee.payRate = score

    #methods to be called on the Employer
    def fairCheck(self):
        unfair = []
        for e in self.employees:
            if e.race != 'URM':
                for i in self.interviewees:
                    if i.interviewScore > e.interviewScore:
                        unfair.append(i)
                        print unfair
        fairPenalty = len(self.interviewees) - len(unfair)
        print fairPenalty
        self.fairScore_race = len(self.interviewees) // fairPenalty * 100
        self.overallScore['race'] = self.fairScore_race
        print 'race: ' + self.fairScore_race

        unfair = []
        for e in self.employees:
            if e.race != 'trans':
                for i in self.interviewees:
                    if i.interviewScore > e.interviewScore:
                        unfair.append(i)
                        print unfair
        fairPenalty = len(self.interviewees) - len(unfair)
        print fairPenalty
        self.fairScore_trans = len(self.interviewees) // fairPenalty * 100
        self.overallScore['trans'] = self.fairScore_trans
        print 'race: ' + self.fairScore_trans

        unfair = []
        for e in self.employees:
            if e.race != 'female':
                for i in self.interviewees:
                    if i.interviewScore > e.interviewScore:
                        unfair.append(i)
                        print unfair
        fairPenalty = len(self.interviewees) - len(unfair)
        print fairPenalty
        self.fairScore_female = len(self.interviewees) // fairPenalty * 100
        self.overallScore['female'] = self.fairScore_female
        print 'race: ' + self.fairScore_female