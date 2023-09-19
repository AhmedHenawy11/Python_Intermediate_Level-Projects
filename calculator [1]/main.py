import art
from replit import clear

# OPERATION FUNCTIONS

def plus (num1, num2):
  result = num1 + num2
  print(f"{float(num1)} + {float(num2)} = {float(result)}")
  num1 = result
  return num1
def minus (num1, num2):
  result = num1 - num2
  print(f"{float(num1)} - {float(num2)} = {float(result)}")
  num1 = result
  return num1
def multiply (num1, num2):
  result = num1 * num2
  print(f"{float(num1)} * {float(num2)} = {float(result)}")
  num1 = result
  return num1
def divide (num1, num2):
  result = num1 / num2
  print(f"{float(num1)} - {float(num2)} = {float(result)}")
  num1 = result
  return num1

# The main function : choose the right function for operation 

recursive = True
again = ""
while recursive == True:
  clear()
  print(art.logo)
  num1 = int(input("What's the first number?: "))
  operation = input("+\n-\n*\n/\nPick an operation: ")
  num2 = int(input("What's the next number?: "))
  if operation == "+":
    outcome = plus(num1, num2)
  elif operation == "-":
    outcome = minus(num1, num2)
  elif operation == "*":
    outcome = multiply(num1, num2)
  elif operation == "/":
    outcome = divide(num1, num2)
    
# Make loop for continuis
  
  again = input(f"Type 'y' to continue calculating with {float(outcome)}, or type 'n' to start a new calculation:")
  while again == "y":
    num1 = outcome
    operation = input("+\n-\n*\n/\nPick an operation: ")
    num2 = int(input("What's the next number?: "))
    if operation == "+":
      outcome = plus(num1, num2)
    elif operation == "-":
      minus(num1, num2)
    elif operation == "*":
      outcome = multiply(num1, num2)
    elif operation == "/":
      outcome = divide(num1, num2)
    again = input(f"Type 'y' to continue calculating with {float(outcome)}, or type 'n' to start a new calculation:")