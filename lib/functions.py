#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")


def greet(name):
    print(f"hello, {name}!")

def greet_with_default(name="programmer"):
     print(f"hello, {name}!")
greet_with_default("Herman")

def add(num1, num2):
    return num1 + num2
result=add(1, 3)
print(result)

def halve(number):
    if not isinstance(number, (int, float)):
        return None

    return number / 2
result = halve(10)      
print(result)

result = halve("text") 
print(result)