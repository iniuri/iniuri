def plus(one, two):
  return one + two
def minus(three, four):
    return three - four

def divide(five, six):
  return five / six
def multiply(seven, eight):
    return seven * eight

while True:
 idf = input("What would you like? [plus/minus/divide/multiply]\n")
 if idf in ("plus", "minus", "divide", "multiply"):
     calc1 = float(input("Please enter calculation 1:\n"))
     calc2 = float(input("Please enter calculation 2:\n"))
 if idf == "plus":
    print(plus(calc1, calc2))
 if idf == "minus":
    print(minus(calc1, calc2))
 if idf == "divide":
    print(divide(calc1, calc2))
 if idf == "multiply":
    print(multiply(calc1, calc2))