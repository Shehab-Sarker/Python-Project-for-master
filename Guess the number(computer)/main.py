import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Guess the number between 1 and {x} : "))
        if guess>random_number:
            print("Sorry,the number is too high.")
        elif guess < random_number:
            print("Sorry the number is very low.")
    print("Congrats,you are win .you have guessed the number. ",random_number)
    
def computer_guess(x):
    low =1
    high =x
    feedback = ""
    while feedback !="c":
        if low !=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback = input(f"Is {guess} too high (H), too low (L) , or correct (C) ??:")
        if feedback =='h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
            
    print(f"yay! The computer guessed your number, {guess}, correctly!.")

computer_guess(10)                         