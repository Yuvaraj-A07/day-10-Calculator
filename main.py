from art import logo
def add(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  return x/y

def calculator():
  print(logo)
  num1 = float(input("Enter the first number : "))
  operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide}
  
  for i in operations:
    print(i)
  operator = input("pick an operation : ")
  num2 = float(input("Enter the second number : "))
  
  
  function = operations[operator]
  answer = function(num1,num2)
  print(f"{num1} {operator} {num2} = {answer}")
  follow = True
  while follow:
    again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation : ")
    if (again == 'y'):
        operator = input("Pick an operation : ")
        num3 = float(input("Enter the next number : "))
        function = operations[operator]
        answer = function(answer,num3)
        print(f"{num1} {operator} {num2} = {answer}")
    else:
      follow = False
      calculator()

calculator()
