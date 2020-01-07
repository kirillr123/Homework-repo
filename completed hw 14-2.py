import pickle

f = open('tempdata', 'rb')
SomeEmployee = pickle.load(f)
print(SomeEmployee.salary)
