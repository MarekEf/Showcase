import random

def guess_card():
    cards = ['Ace', 'King', 'Queen']
    choice = random.choice(cards)
    
    print("Welcome to the 3-card guessing game!")
    print("I have selected a card. Can you guess which one it is?")
    
    while True:
        choice = random.choice(cards)
        guess = input("Enter your guess (Ace, King, or Queen): ")
        guess = guess.capitalize()
        
        if guess not in cards:
            print("Invalid input! Please enter a valid card name.")
            continue
        
        if guess == choice:
            print("Congratulations! You guessed correctly!")
        else:
            print("Sorry, that's incorrect. Try again!")
            print("Hint: The card is not " + guess)
            
        play_again = input("Do you want to play again? (yes/no): ")
        
               
        if play_again.lower() == "no":
            break

guess_card()