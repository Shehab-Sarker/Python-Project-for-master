import random

def play():
    user=input("Which are you choice? 'r' for rock,'p' for paper,'s' for scissor :\n")
    computer=random.choice(['r','p','s'])
    print("Computer choice:",computer)
    if user==computer:
        return "It's game Tie."
    if is_win(user,computer):
        return "You are win the game!"
    
    return "You are lost the game!"
 
#   r>>s ,p>>r,s>>p
    
def is_win(user,opponenet):
    if (user=='r' and opponenet=='s') or (user=='p' and opponenet=='r') or (user=='s' and opponenet=='p'):
        return True
    
print(play())
    
