import random


def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
            print(err)

age = get_int("enter your age: ")

print("age = ", age)

x = random.randint(1,6)
print(x)