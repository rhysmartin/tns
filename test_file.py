from ry import *

ruona = Employee('Rouna')

rhys = Employee('Rhys')

john = Employee('John')

google = Employer('Google')

hooli = Employer('Hooli')

batch = [rouna, rhys]

google.batch_interview(batch)

google.interview(john, 100, 1)
