import random

asf = random.randrange(1,100)

for i in range (7):
    user=int(input("guess: "))
    if user == 69 and not asf:
        print("nice, but nah")

    if user < asf:
        print("nah, try higher")
    elif user > asf:
        print("how about you try lower")
    if user == asf:
        print("boom ..  nigga can guess")
        break
    if i == 6:
        print("Game Over :(, the number was", asf)