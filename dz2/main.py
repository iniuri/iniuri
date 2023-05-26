import time
import random
import time
hunger = 0
thirsty = 0
ugly = 0
# no time
# не было времени

print("Sims kind of thing idk\n kinda basically rp but random stuff")
print("Name: Kajin houroshi")
print("Gender: M")
print("Age: 23")
rn = input("What are you going to do now? [relax/cook/eatz]")
if rn == 'relax':
    print("You are now relaxing...")
    time.sleep(10)
    print("you didnt bring snacks, character got bored +10 hunger")
    hunger += 10
    print(f"Current status: hunger - {hunger}, thirst - {thirsty}, ugly'o'meter - {ugly}")
    print("/shrug - game over")
elif rn == "cook":
        number = random.randint(1, 5)
        print('!!! Your character is on fire !!!')
        question = input("Extinguish it? [y/n]")
        if question == 'y':
            print("[        ]")
            time.sleep(1)
            print("[ |      ]")
            time.sleep(1)
            print("[ ||     ]")
            time.sleep(1)
            print("[ |||    ]")
            time.sleep(1)
            print("[ ||||   ]")
            time.sleep(1)
            print("[ |||||  ]")
            time.sleep(1)
            print("[ |||||| ]")
            time.sleep(1)
            print("[ |||||| ]")
            if number == 1:
                print("Extinguishing failed ! Character died, RIP")
            else:
                print("Extinguishing success !")
        elif question == 'n':
            print("Your character died because of fire. RIP")

if rn == 'eat':
  ques = input("What will you eat? [chips/oreo/Pom-Bär Original/m&m]")
  if ques == 'chips':
      print("Eating...")
      time.sleep(3)
      print("Success ! -10 hunger")
      hunger -= 10
      print(f"Current status: hunger - {hunger}, thirst - {thirsty}, ugly'o'meter - {ugly}")
      print("/shrug - game over")
  if ques == 'oreo':
      print("Eating...")
      time.sleep(3)
      print("Success ! -10 hunger")
      hunger -= 10
      print(f"Current status: hunger - {hunger}, thirst - {thirsty}, ugly'o'meter - {ugly}")
      print("/shrug - game over")
  if ques == 'Pom-Bär Original':
      print("Eating...")
      time.sleep(3)
      print("Success ! -2 hunger")
      hunger -= 2
      print(f"Current status: hunger - {hunger}, thirst - {thirsty}, ugly'o'meter - {ugly}")
      print("/shrug - game over")
  if ques == 'm&ms':
      print("Eating...")
      time.sleep(3)
      print("Success ! -2 hunger")
      hunger -= 2
      print(f"Current status: hunger - {hunger}, thirst - {thirsty}, ugly'o'meter - {ugly}")
      print("/shrug - game over")