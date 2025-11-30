# ask user for number input.Assume the guess is 65
# create a number guessing game for number between 1 to 100
# if the number is not equal to the correct number,ask user to guess again
# if number is out of range,please ask user to enter again
# the number of attempts is 5 times

number = 65
attempt = 5
min = 1
max = 100
guess = int(input(f"Enter a number between {min}-{max} here:"))
attempt = attempt - 1
while guess > max or guess < min:
    print(f"Out of range! You still left {attempt} attempt.")
    guess = int(input(f"Enter a number between {min}-{max}here:"))

    attempt = attempt - 1
    if attempt == 0:
        break
    # use another while loopthat check guess not equal to correct and attempt is more than zero
    # get another input for guess and using inner while loop to repeat if number out of range

    while guess != number and attempt > 0:
        print(f"You still left {attempt}attempt.")
        guess = int(input(f"Enter a number between {min}-{max}here:"))
        attempt=attempt-1
    if guess == number and attempt > 0;
        if correct > guess:
        min = guess
else:
    max = guess
print(f"You still left {attempt}attempt.")
guess = int(input(f"Enter a number between {min}-{max} here:"))
attempt=attempt-1
if guess == number:

    print(("Congratulation you guessed the correct number"))
    else:
        print("You used all the attempts")

