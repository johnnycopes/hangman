import getpass

print """
Welcome to Hangman! You need two players for this game.
Player 1 chooses a word and player 2 tries to guess what it is,
one letter at a time, in seven guesses or less.
"""

# Ask for word to be guessed (characters hidden on screen)
target_word = getpass.getpass('Player 1, choose a word: ')
# Make visual map of word to guess
word_to_guess = "*" * len(target_word)

# Track guesses
guesses_remaining = 7
guessed_letters = []

while guesses_remaining > 0:

    if guesses_remaining == 1:
        print "\n%d guess remaining." % guesses_remaining
    else:
        print "\n%d guesses remaining." % guesses_remaining
    guesses_remaining -= 1
    print "Word to guess: %s" % word_to_guess

    guess = raw_input("Guess a letter: ")

    if guess in target_word:
        # Find out where the guessed letter occurs in the target word
        print "\nNice!"
        indices = []
        for i, j in enumerate(list(target_word)):
            if j == guess:
                indices.append(i)
        # Show guessed letter in visual map
        for index in indices:
            word_to_guess = list(word_to_guess)
            word_to_guess[index] = guess
        word_to_guess = "".join(word_to_guess)
        print word_to_guess
    else:
        print "\nNope."

    # Append guessed number to beginning of guessed_letters list
    guessed_letters.insert(0, guess)
    # Show guessed letters after first guess
    if guesses_remaining < 7:
        print "Letters guessed: %s" % guessed_letters

print "game over"
