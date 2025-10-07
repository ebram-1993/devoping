import random

numerisecreti=random.randint(1,20)

print("indovina")

for x in range(1,7):
    print("vai")
    guess = int(input())

    if guess > numerisecreti:
        print("valore alto")
    elif guess < numerisecreti:
        print("valore basso")
    else:
        break
if guess == numerisecreti:
    print("ottimo hai indovinato in " + str( x ) + " tentativi")
else:
    print("non hai indovinato niente, mi dispiace")