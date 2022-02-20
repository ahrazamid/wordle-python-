from misc import words
from termcolor import colored
import random
import misc



### game loop
for i in range(1,7):
    guess = input().lower()
    generated = random.choice(words)
    for x in range(min(len(guess),5)):
        if guess[x] == generated[x]:
            print("🟩",end=" ")
        elif guess[x] in generated:
            print("🟨",end=" ")
        else:
            print("⬛",end=" ")







