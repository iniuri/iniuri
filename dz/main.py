#
# import random
# import time
# lives = 3
# number = random.randint(1, 3)
# streak = 0
# if number == 1:
#         print("------------------------------------")
#         print("welcome to [insert gameshow here]")
#         print("mode: [easy]")
#         print("the rules are simple\n you must answer correctly the math problems, if you answer 1 incorrectly, you lose a life")
#         print("------------------------------------")
#         print("[ ] loading...")
#         time.sleep(5)
#         print("[ | ] loading...")
#         time.sleep(5)
#         print("[ || ] loading...")
#         time.sleep(5)
#         print("[ ||| ] loading...")
#         time.sleep(5)
#         print("[ |||| ] loading...")
#         time.sleep(5)
#         print("[ ||||| ] loading...")
#         print("------------------------------------")
#         print(f"current lives: {lives}")
#         q1 = input("5 x 10 = ?\n")
#         if q1 == "50":
#             print('correct!')
#             streak += 1
#             print(f'current status: life(s): {lives} streak: {streak}')
#         else:
#           lives -= 1
#           streak -= 1
#           print("Wrong! - 1 life(s)")
#           print(f'current status: life(s): {lives} streak: {streak}')
#         q2 = input("4 x 6 = ?\n")
#         if q2 == "26":
#                 streak += 1
#                 print('correct !')
#                 print(f'current status: life(s): {lives} streak: {streak}')
#         else:
#             lives -= 1
#             streak -= 1
#             print("Wrong! - 1 life(s)")
#             q3 = input("6 x 6 = ?\n")
#         if q3 == "36":
#                 streak += 1
#                 print('correct !')
#                 print(f'current status: life(s): {lives} streak: {streak}')
#         else:
#             lives -= 1
#             streak -= 1
#             print("Wrong! - 1 life(s)")
#             print(f'current status: life(s): {lives} streak: {streak}')
#
# if number == 2:
#         print("------------------------------------")
#         print("welcome to [insert gameshow here]")
#         print("mode: [medium]")
#         print("the rules are simple\n you must answer correctly the math problems, if you answer 1 incorrectly, you lose a life")
#         print("------------------------------------")
#         print("[ ] loading...")
#         time.sleep(5)
#         print("[ | ] loading...")
#         time.sleep(5)
#         print("[ || ] loading...")
#         time.sleep(5)
#         print("[ ||| ] loading...")
#         time.sleep(5)
#         print("[ |||| ] loading...")
#         time.sleep(5)
#         print("[ ||||| ] loading...")
#         print("------------------------------------")
#         print(f"current lives: {lives}")
#         q4 = input("7 x 8 = ?\n")
#         if q4 == "56":
#             print('correct!')
#             streak += 1
#             print(f'current status: life(s): {lives} streak: {streak}')
#         else:
#           lives -= 1
#           streak -= 1
#           print("Wrong! - 1 life(s)")
#           print(f'current status: life(s): {lives} streak: {streak}')
#         q5 = input("8 x 9 = ?\n")
#         if q5 == "72":
#                 streak += 1
#                 print('correct !')
#                 print(f'current status: life(s): {lives} streak: {streak}')
#         else:
#             lives -= 1
#             streak -= 1
#             print("Wrong! - 1 life(s)")
#             q6 = input("7 x 11 = ?\n")
#         if q6 == "77":
#                 streak += 1
#                 print('correct !')
#                 print(f'current status: life(s): {lives} streak: {streak}')
#         else:
#             lives -= 1
#             streak -= 1
#             print("Wrong! - 1 life(s)")
#             print(f'current status: life(s): {lives} streak: {streak}')
#
# if number == 3:
#         print("------------------------------------")
#         print("welcome to [insert gameshow here]")
#         print("mode: [hard]") # wtf?!?!? impossible
#         print("the rules are simple\n you must answer correctly the math problems, if you answer 1 incorrectly, you lose a life")
#         print("------------------------------------")
#         print("[ ] loading...")
#         time.sleep(5)
#         print("[ | ] loading...")
#         time.sleep(5)
#         print("[ || ] loading...")
#         time.sleep(5)
#         print("[ ||| ] loading...")
#         time.sleep(5)
#         print("[ |||| ] loading...")
#         time.sleep(5)
#         print("[ ||||| ] loading...")
#         print("------------------------------------")
#         print(f"current lives: {lives}")
#         q7 = input("17 x 7 = ?\n")
#         if q7 == "119":
#             print('correct!')
#             streak += 1
#             print(f'current status: life(s): {lives} streak: {streak}')
#         else:
#           lives -= 1
#           streak -= 1
#           print("Wrong! - 1 life(s)")
#           print(f'current status: life(s): {lives} streak: {streak}')
#         q8 = input("18 x 9 = ?\n")
#         if q8 == "162":
#                 streak += 1
#                 print('correct !')
#                 print(f'current status: life(s): {lives} streak: {streak}')
#         else:
#             lives -= 1
#             streak -= 1
#             print("Wrong! - 1 life(s)")
#             q9 = input("46 x 22 = ?\n")
#         if q6 == "1012":
#                 streak += 1
#                 print('correct !')
#                 print(f'current status: life(s): {lives} streak: {streak}')
#         else:
#             lives -= 1
#             streak -= 1
#             print("Wrong! - 1 life(s)")
#             print(f'current status: life(s): {lives} streak: {streak}')
#
# if lives == 0:
#     print("Game over! No lifes left")
# if lives > 3:
#     print("Cheater! Your lifes are more than 3! \n (contact [host] if error)")