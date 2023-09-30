import art 
from game_data import data
import random 

def compare(a, b, choice, score):
  
  # compare (def)
    ## compare the choice   
    ## Chick if right or false
    ## Display the score
    # Correction 
      ## if user's choice false : end
      ## if user's choice right : Repeat
  
  correct = True
  if choice == 'a' and a > b or choice == 'b' and a<b:
    score += 1
    return f"You're right! Current score: {score}", correct
  
  else:
    correct = False
    return f"Sorry, that's wrong. Final score: {score}", correct
    


def game ():
  repeat = True
  score = 0
  # Print
    ## logo one
    ## compare A
    ## logo 2
    ## compare B
    ## Ask for user's choice
  compare_a = random.choice(data)
  while repeat == True:
    print(art.logo)
    compare_b = random.choice(data)
    while compare_b == compare_a:
      compare_b = random.choice(data)
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
    print(art.vs)
    print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")
  
    
    choice = input("Who has more followers? Type 'A' or 'B':").lower()
  
    is_correct = compare(compare_a["follower_count"], compare_b["follower_count"], choice, score)
  
    print(is_correct[0])
    # If Repeat 
      ## increse the score
      ## switch A to B
      ## keep repeating untill false
    
    if is_correct[1] == False:
      repeat = False
    score += 1 
    compare_a = compare_b

game()