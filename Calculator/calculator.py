
# input values validation check first , Enter correct inputs values:
def validatorFn():
  while True:
    operator = input("Enter an operator (+ - * /): ")
    if operator in ["+","-","*","/"]:
      break
    else:
      print("Put the Valid operators\n")
  while True:
    try:
      num1 = float(input("Enter the First number: "))
      break
    except ValueError:
      print("invalid input . Please Enter the Valid Number")
  while True:
    try: 
      num2 = float(input("Enter the second number: "))
      break
    except ValueError:
      print("invalid input . Please Enter the Valid Number")
  return operator, num1, num2
  


def Calculation(operator, num1, num2):
  if operator == "+":
    result = num1 + num2
    print(result)
  elif operator == "-":
    result = num1 - num2
    print(result)
  elif operator == "*":
    result = num1 * num2
    print(result)
  elif operator == "/":
    if num2 != 0:
      result = num1 / num2
      print(result)
    else:
      print("Error: Division by Zero")
      return None
  return result


def main():
  operator, num1, num2 = validatorFn()
  result = Calculation(operator, num1, num2)
  if result is not None:
    print("result: ",result)
    

if __name__ == "__main__":
  main()



