import random

rolls = 0

while True:
    rolls += 1
    rolls = random.randint(1, 6)

    if rolls == 6:
        print("You got a 6!")
        break
    else:

        print("Try again!")

