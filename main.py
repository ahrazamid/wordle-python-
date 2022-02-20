from word_list import words
import random

### game loop
for i in range(1,7):
    ### 6 tries max
    guess = input().lower()
    generated = random.choice(words)
    for x in range(min(len(guess),5)):
    ###only accepts 5 letter words

        ###checks for letter in the exact index
        if guess[x] == generated[x]:
            print("🟩",end=" ")
        ###checks for letter somewhere in the generated word
        elif guess[x] in generated:
            print("🟨",end=" ")
        ###returns black if letter is no where in the generated word
        else:
            print("⬛",end=" ")







