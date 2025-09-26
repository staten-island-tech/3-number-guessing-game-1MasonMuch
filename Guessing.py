# count = 1 

# while count <= 5:
#     print("This is loop number", count)
#     count = count + 1

# order = ""
# while order != "done":
#     order = input("What would you like ro order? (type 'done' to finish): ")
# print ("Thanks for your order")

#Challenge
# number = 10
# while number > 0: 
#      print("This is loop number", number)
#      number = number - 1


# order = ""
# while order != "stop":
#      order = input("What is your favorite color? (type 'stop' to finish): ")
# print ("Thanks for your input")

#__________________________________________________________________________________
#NUMBER GUESSING GAME

import random 
number = random.randint(1,10)
answer = 0
guess_history = int([])
while answer != number:
     answer = int(input("Please guess a number 1-10"))
     if answer > number:
          print("Lower")
     elif answer < number:
          print("Higher")
     guess_history.append[answer]
print(f"You got it! Your previous answers were {guess_history} ")
