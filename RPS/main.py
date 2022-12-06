import random
import json

shapes = ["rock", "paper", "scissors", "spock", "lizard"]
countValues = {"player": 0, "cpu": 0, "draws": 0, "rock": 0, "paper": 0, "scissors": 0, "spock": 0, "lizard": 0}
dataFile = {}
weight = [0, 0, 0, 0, 0]


def pickCPU():
    count = 0
    for key in dataFile:
        if "player" not in key and "cpu" not in key and "draws" not in key:
            if dataFile[key] == 0:
                weight[count] = dataFile[key] + 0.01
            else:
                weight[count] = dataFile[key]
            count += 1

    move = weight[len(weight) - 1]
    weight.remove(weight[len(weight) - 1])
    weight.insert(0, move)
    choice = random.choices(shapes, k=1, weights=weight)
    return choice[0]


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


def reset():
    dataFile = {"player": 0, "cpu": 0, "draws": 0, "rock": 0, "paper": 0, "scissors": 0, "spock": 0, "lizard": 0}
    countValues = dataFile
    weight = [0, 0, 0, 0, 0]
    f = open("save.txt", "w")
    json.dump(dataFile, f)
    f.close()


def combine(a, b):
    for key in a:
        dataFile[key] = a[key] + b[key]
    return a


def update():
    f = open("save.txt", "r")
    saved = f.read()
    if saved:
        save_json = json.loads(saved)
        combine(countValues, save_json)
    f.close()
    f = open("save.txt", "w")
    json.dump(dataFile, f)
    f.close()


def game():
    update()
    wrong = 1
    print("Welcome to Rock-Paper-Scissors-Spock-Lizard!\n")
    while wrong == 1:
        print("What action do you want to perform?")
        print("     --START GAME (play)")
        print("     --SHOW STATS (stats)")
        print("     --UPDATE STATS (save)")
        print("     --RESET STATS (reset)")
        print("     --EXIT (exit)")
        choice = str(input().lower())
        if choice == "play":
            gameStatus = 1
            while gameStatus == 1:
                print("Which shape do you want to pick? (Rock/Paper/Scissors/Spock/Lizard)")
                shapePlayer = str(input().lower())
                if shapes.count(shapePlayer) == 0:
                    print("Please choose an existing shape!")
                else:
                    countValues[shapePlayer] += 1
                    shapeCPU = pickCPU()
                    print("\nYou picked: ", shapePlayer.upper())
                    print("The CPU picked: ", shapeCPU.upper())
                    win = checkWinner(shapePlayer, shapeCPU)
                    print("\nThe result is: ", win)
                    cont = 1
                    while cont == 1:
                        print("\nDo you want to play again? (yes/no)")
                        decision = input().lower()
                        if decision == "yes":
                            gameStatus = 1
                            cont = 0
                        elif decision == "no":
                            cont = 0
                            gameStatus = 0
                        else:
                            cont = 1
                            gameStatus = 0
            wrong = 1
        elif choice == "stats":
            print(dataFile)
            print()
            wrong = 1
        elif choice == "save":
            update()
            print("Your stats have been updatet!\n")
            wrong = 1
        elif choice == "reset":
            reset()
            print("Saved data has been reset!\n")
            wrong = 1
        elif choice == "exit":
            print("Until next time!")
            wrong = 0
        else:
            wrong = 1
            print("Please enter a valid command!\n")


if __name__ == '__main__':
    update()
    game()
