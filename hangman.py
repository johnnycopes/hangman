import getpass

print """
Welcome to Hangman! You need two players for this game.
Player 1 chooses a word and player 2 tries to guess what it is,
one letter at a time, in seven guesses or less.
"""

# Ask for word to be guessed (characters hidden on screen)
target_word = getpass.getpass('Player 1, choose a word: ')

# Set guess counter
guesses_remaining = 7

# Make visual map of word to guess
word_to_guess = "*" * len(target_word)

# Create an empty list to store the user's guesses
guessed_letters = []

while guesses_remaining > 0:

    # Show guesses remaining, then subtract one
    if guesses_remaining == 1:
        print "\n%d guess remaining." % guesses_remaining
    else:
        print "\n%d guesses remaining." % guesses_remaining
    guesses_remaining -= 1

    # Show a visual map of the word
    print "Word to guess: %s" % word_to_guess

    # Prompt the user to guess another letter
    guess = raw_input("Guess a letter: ")

    if guess in target_word:
        print "\nNice!"
        word_to_guess = list(word_to_guess)
        print word_to_guess
        # print target_word.find(guess)
    else:
        print "\nNope."

    # Append guessed number to beginning of guessed_letters list
    guessed_letters.insert(0, guess)
    # Show guessed letters after first guess
    if guesses_remaining < 7:
        print "Letters guessed: %s" % guessed_letters

print "game over"
