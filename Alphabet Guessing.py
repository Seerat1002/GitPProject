#A game to guess a word using random library and its inbuilt functions

import random

word_bank = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "island", "jungle", "kangaroo", "lemon", "mountain", "notebook", "orange", "penguin","quartz", "river", "sunshine", "tiger", "umbrella", "violet", "whale", "xylophone", "yacht", "zebra", "anchor", "bridge", "cloud", "desert", "engine", "forest", "garden", "harbor", "iceberg", "jacket", "key", "ladder", "mirror", "needle", "ocean", "pencil", "queen", "rocket", "sword", "tower", "unicorn", "valley", "window", "xenon", "yarn", "zucchini", "artist", "butterfly", "camera", "dragon", "emerald", "feather", "guitar", "helmet", "insect", "jewel", "kitten", "lantern", "magnet", "necklace", "orchid", "planet", "quiver", "rainbow", "sailboat", "teapot", "uniform", "violin", "wallet", "xylitol", "yogurt", "zeppelin", "arrow", "book", "castle", "diamond", "envelope", "fountain", "galaxy", "hammer", "igloo", "journal", "kite", "lantern", "maple", "nest", "olive", "piano", "quilt", "rose", "shield", "train", "village", "watch"]
word = random.choice(word_bank)


print("Welcome to the Alphabet Guessing Game!")
attempts = 10
guessedWord = ['_'] * len(word)
while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
                print('Great guess!')

    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))

    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word.upper())
        break

if attempts == 0 and '_' in guessedWord:
    print('\nYou\'ve run out of attempts! The word was: ' + word.upper())

print("Thank you for playing the Alphabet Guessing Game!")
