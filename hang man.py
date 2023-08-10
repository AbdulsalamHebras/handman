from random import *

words =['book','pen','work']
chosenWord = choice(words)
wordLetters = set(chosenWord) 
alphabet = set(list('abcdefghijklmnopqrstuvwxyz'))
usedLetters = set()
trys=4

while len(wordLetters) > 0 and trys > 0:
    wordList = [letter if letter in usedLetters else '-' for letter in chosenWord] 
    print('the word is: ', ' '.join(wordList))

    enteredChar = input('Guess a letter: ').lower()
    if enteredChar in alphabet - usedLetters:
        usedLetters.add(enteredChar)
        if enteredChar in wordLetters:
            wordLetters.remove(enteredChar)
        else:
            trys -= 1 
            print('Letter is not in word.')
    else:
        print("invailed enter try again")

if trys==0:
    print(f"you lose the word was: {chosenWord}")
else:
    print(f"you win the word is: {chosenWord}")
