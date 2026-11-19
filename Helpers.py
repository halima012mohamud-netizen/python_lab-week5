import math

def welcome(name):
    return "Welcome to PLP, " + name + "!"

def tables_needed(students, seats):
    return math.ceil(students / seats)

if __name__== "_main_":
    print(tables_needed(9, 3))
