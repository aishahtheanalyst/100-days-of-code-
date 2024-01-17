from calculator_art import logo

#Calculator

#Add
def add(n1, n2):
  return n1 + n2 

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

#Dictionary
  
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
for symbol in operations:
  print(symbol)

#select "*"
operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {first_answer}")

#select "*" which overrides the "+" we selected on line 32.
operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))

#calculation_function selected will be the multiply() function
calculation_function = operations[operation_symbol]

#second_answer = multiply(multiply(num1, num2), num3)
second_answer = calculation_function(calculation_function(num1, num2), num3)

#second_answer = 2 * 3 * 3 * 3 = 18
#fix the bug - need to change line 49 to:
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")