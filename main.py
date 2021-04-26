import random
from hangman_words import word_list
from hangman_art import stages, logo


print(logo)
choosen_word = random.choice(word_list)
word_length = len(choosen_word)
lives = len(stages) - 1

display = []
count = 0
while count < word_length:
    display.append("_")
    count += 1

print(' '.join(display))
print("")

end_of_game = False
while not end_of_game:
    guess = input("Choose a letter: ").lower()
    
    if guess in display:
        print(f"You have already guessed {guess}")
    
    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    
    if guess not in choosen_word:
        print("\n")
        print(f"You guessed {guess}. It's not in the word. You loose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("*****************")
            print("* You lose! *")
            print("*****************")
        print(f"The chosen word was: {choosen_word}")
    
    if '_' not in display:
        end_of_game = True
        print("*****************")
        print("* You have won! *")
        print("*****************")
        
    print(stages[lives])