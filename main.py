import random
from art import logo

print("Welcome to Blackjack!")
print(logo)

money = 2500
prob_lst = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card(whom):
  whom.append(random.choice(prob_lst))

def score(card_lst):
  return sum(card_lst)

cont = True
game = True

while cont == True: # keeps Blackjack going
  your_cards = ''
  user_cards = []
  computer_cards = []

  print(f"Your balance is ${money}.")
  bet = int(input("How much money would you like to bet? $"))
  
  for i in range(2):
    deal_card(user_cards)
    deal_card(computer_cards)
  
  print(f"Your cards are {user_cards[0]} and {user_cards[1]}, your score is {score(user_cards)}.")
  print(f"The computer's cards are {computer_cards[0]} and unknown. ")

  while game == True:
    if score(user_cards) == 21 or score(computer_cards) == 21:
      if score(computer_cards) == 21:
        print("You lose.")
        money -= bet
        break
      elif score(user_cards) == 21:
        print("You win!")
        money += bet
        break
    elif score(user_cards) > 21:
      if 11 in user_cards:
        user_cards[user_cards.index(11)] = 1
        if score(user_cards) > 21:
          print("You lose.")
          money -= bet
          break
      else:
        print("You lose.")
        money -= bet
        break
    another = input("Would you like another card? Type 'yes' or 'no'\n")
    if another == 'yes':
      deal_card(user_cards)
      for i in user_cards[:-1]:
        your_cards += str(i) + ', '
      print(f"Your cards are {your_cards + str(user_cards[-1])} and your score is {score(user_cards)}")
      game == False
    elif another == 'no':
      while score(computer_cards) < 17:
        deal_card(computer_cards)
      if score(computer_cards) > 21:
        print("You win!")
        money += bet
        break
      elif score(computer_cards) > score(user_cards):
        print("You lose.")
        money -= bet
        break
      elif score(user_cards) > score(computer_cards):
        print("You win.")
        money += bet
        break
      elif score(computer_cards) == score(user_cards):
        print("It's a draw.")
        break
  if game == True:
    print(f"Your balance is now ${money}.")
    cont_game = input("Would you like to continue playing Blackjack? Type 'yes' or 'no': ")
    if cont_game == 'no':
      break
