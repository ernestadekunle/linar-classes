import random

# Generate a random number between 1 and 100
target_num = random.randint(1, 100)

# Prompt the user to guess the number
guess = int(input("Guess a number between 1 and 100: "))

# Keep track of the number of guesses
num_guesses = 1

# Keep looping until the user guesses the number
while guess != target_num:
    # Give the user a hint
    if guess > target_num:
        print("Your guess is too high. Try again.")
    else:
        print("Your guess is too low. Try again.")

    # Get the user's next guess
    guess = int(input("Guess a number between 1 and 100: "))

    # Increment the number of guesses
    num_guesses += 1

# Print a success message
print("Congratulations! You guessed the number in {} guesses.".format(num_guesses))
