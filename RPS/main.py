import random
import json
import operator


shapes = ["rock", "paper", "scissors", "spock", "lizard"]
countValues = {"player": 0, "cpu": 0, "draws": 0, "rock": 0, "paper": 0, "scissors": 0, "spock": 0, "lizard": 0}


def pickCPU():
    return shapes[random.randint(0, 4)]


def checkWinner(player, cpu):
    indexPlayer = shapes.index(player)
    indexCPU = shapes.index(cpu)
    if (indexPlayer + 2) > 4:
        indexPlayer = indexPlayer - 5
    if (shapes[indexPlayer + 2] == shapes[indexCPU]) or (shapes[indexPlayer - 1] == shapes[indexCPU]):
        winner = "Player won!"
        countValues["player"] += 1
    elif (shapes[indexPlayer - 2] == shapes[indexCPU]) or (shapes[indexPlayer + 1] == shapes[indexCPU]):
        winner = "CPU won!"
        countValues["cpu"] += 1
    else:
        winner = "It's a draw!"
        countValues["draws"] += 1
    return winner


def combine(a, b, op=operator.add):
    return dict(a.items() + b.items() +
        [(k, op(a[k], b[k])) for k in set(b) & set(a)])


def update():
    f = open("save.txt", "r")
    x = f.read()
    print(json.load(x))



def game():
    gameStatus = 1
    print("Welcome to Rock-Paper-Scissors-Spock-Lizard!\n")
    while gameStatus == 1:
        cont = 1
        print("Which shape do you want to pick? (Rock/Paper/Scissors/Spock/Lizard)")
        shapePlayer = str(input().lower())
        if shapes.count(shapePlayer) == 0:
            print("Please choose an existing shape!")
        else:
            countValues[shapePlayer] += 1
            shapeCPU = pickCPU()
            countValues[shapeCPU] += 1
            print("\nYou picked: ", shapePlayer.upper())
            print("The CPU picked: ", shapeCPU.upper())
            win = checkWinner(shapePlayer, shapeCPU)
            print("\nThe result is: ", win)

            while cont == 1:
                print("\nDo you want to play again? (yes/no)")
                decision = input().lower()
                if decision == "yes":
                    gameStatus = 1
                    cont = 0
                elif decision == "no":
                    f = open("save.txt", "r")
                    new = json.loads(f.read())
                    f.close()

                    if new == "" or new == "null" or new is None:
                        newDict = countValues
                    else:
                        newDict = combine(new, countValues)

                    f = open("save.txt", "w")

                    f.write(json.dumps(newDict))
                    print(newDict)
                    f.close()

                    cont = 0
                    gameStatus = 0
                else:
                    cont = 1
                    gameStatus = 0


if __name__ == '__main__':
    update()
    game()