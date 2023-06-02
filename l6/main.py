'''
try:
    your_code
except type_of_the_error:
    your_code
'''
from buildingerror import BuildingError
from validation import Validation
checker = Validation()
try:
    amount=int(input("Enter amount: "))
    limit=int(input("Enter limit: "))
    checker.Check(amount, limit)
    print(10/0)
except BuildingError as be:
    print(f"Custom exception: {be}")
except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as ex:
    print(f"Standart exception: {ex}")