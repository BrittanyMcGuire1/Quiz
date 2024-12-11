print('Hello! Welcome to the quiz game')

#I made sure to add .lower() to the prompts so that no matter what the user typed the answer in, it would convert it to lowercase.
play = input('Would you like to play?: ').lower()
if play == 'yes':
  topic = input("Awesome! Let's get started. We are going to quiz you on 3 subjects:\n Biology,\n History,\n and Astronomy\n (Hit enter)").lower()
else:
  input("Seems as though that wasn't a 'yes'\nWell thanks for stopping by!")

#initializing th variable  
score = 0 

input("Let's begin with the subject Biology, hit enter for your first question!")
#This is the starting point for the quesions and their conditions.
answer = input('What is the study of living organisms called?: ').lower()
if answer == "biology":
  print('Correct!')
  score += 1 #This is how the score gets +1 for correct answers
else:
  print('Incorrect!')
answer = input('What is the fluid that carries nutrients and oxygen throughout the body?: ').lower()
if answer == "blood":
  print('Correct!')
  score += 1
else:
  print('Incorrect!')
answer = input('What is the fastest land animal?: ').lower()
if answer == "cheetah":
  print('Correct!')
  score += 1
else:
  print('Incorrect!')
  
#This is an input just telling the player we are moving into the history portion of the quiz. Score is still being tallied and not starting over
input("Let's move onto the History portion\nHit enter")
answer = input('Who was the first president of the United States?: ').lower()
if answer == "george washington":
  print('Correct!')
  score += 1
else:
  print('Incorrect!')
answer = input('Who was the first person to step on the moon?: ').lower()
if answer == "neil armstrong":
  print('Correct!')
  score += 1
else:
  print('Incorrect!')
answer = input('What holiday do we celebrate in the United States on July 4th?: ').lower()
if answer == "independence day":
  print('Correct!')
  score += 1
else:
  print('Incorrect!')

#This is the last section of the quiz and the subject is astrology  
input("And finally Astronomy\nHit enter")
answer = input('What do we call a group of stars that form a pattern in the night sky?: ').lower()
if answer == "constellation":
  print('Correct!')
  score += 1
else:
  print('Incorrect!')
answer = input('What is the name of the planet in our solar system that is known as the "Red Planet"?: ').lower()
if answer == "mars":
  print('Correct!')
  score += 1
else:
  print('Incorrect!')
answer = input('What is the name of the largest planet in our solar system?: ').lower()
if answer == "jupiter":
  print('Correct!')
  score += 1
else:
  print('Incorrect!')

#Added the total answers correct and made sure to convert the score to a string in order to concatenate the score and the strings 'you got this' and 'questions correct'. Divided the score by th total number of questions to get the percentage
print('You got ' + str(score) + ' question(s) correct!')
print('That is ' + str((score/9) * 100) + '%!')
#I wanted to have 2 diffrent options at the end. If the player get >=7 they get a diffrent promt than if they got < 7
if score >= 7:
  print("Great job")
else:
  print("You can try again for a better score") 
print('Thanks for playing! :) ')
    