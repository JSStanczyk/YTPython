from random import randint

rand=randint(1,10)
attempts=0
print("Zgadnij liczbę od 1 do 10")
while True:
    attempts+=1
    bet=int(input("> "))
    if rand==bet:
        break
print("You son of a bitch you did it")
print("It took you",attempts,"attempts")