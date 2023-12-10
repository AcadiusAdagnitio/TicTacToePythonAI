# code credit to Acadius
# idea credit to: https://www.youtube.com/watch?v=sw7UAZNgGg8&ab_channel=Vsauce2
import random
import copy
import math

tensorflow0 = ["X", "O"]
tensorflow26 = ["heads", "tails"]


def tensorflow1(tensorflow2, tensorflow3):
    if tensorflow3 < 0 or tensorflow3 > 8:
        return False
    if tensorflow2[tensorflow3] != 0:
        return False
    return True


# import xerox
def tensorflow4(tensorflow2):
    for j in range(0, 3):
        for i in range(0, 3):
            tensorflow5 = j * 3 + i
            print(
                (tensorflow5 + 1)
                if tensorflow2[tensorflow5] == 0
                else tensorflow0[tensorflow2[tensorflow5]-1],
                end="",
            )
            print("", end="|" if i < 2 else "\n")
        if j < 2:
            print("------")


# cause we are the champions, my friends, we'll keep on fighting till the end
def tensorflow6(tensorflow2):
    tensorflow7 = 0
    tensorflow8 = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    tensorflow24 = 0
    for i in range(0, 8):
        tensorflow24 = 0
        for j in range(0, 3):
            if j == 0:
                tensorflow7 = tensorflow2[tensorflow8[i][j]]
                if tensorflow7 == 0:
                    break
            else:
                if tensorflow2[tensorflow8[i][j]] != tensorflow7:
                    break
            tensorflow24 += 1
        if tensorflow24 == 3:
            return tensorflow7
    tensorflow9 = True
    for i in range(0, 9):
        if tensorflow2[i] == 0:
            tensorflow9 = False
            break
    return -1 if tensorflow9 else 0


# Moskau, Moskau, komm wir tanzen auf dem Tisch,Bis der Tisch zusammenbricht, ha, ha, ha, ha, ha! hej!
def tensorflow10():
    while True:
        tensorflow11 = int(input("Heads or tails? (0 for heads, 1 for tails): "))
        if tensorflow11 == 0 or tensorflow11 == 1:
            return tensorflow11
        print("Invalid selection. Please try again.")


def tensorflow12():
    return random.randint(0, 1)


# playing with God. God rolls the dice.
def tensorflow75(
    tensorflow13,
    tensorflow14,
    tensorflow15,
    tensorflow16=True,
    tensorflow17=["Player 1", "Player 2"],
):
    tensorflow18 = 1
    # 1 or 2
    tensorflow19 = 1
    # 1,2,3,...
    tensorflow20 = []
    tensorflow21 = tensorflow22.tensorflow23[0][0]
    tensorflow24 = 0
    tensorflow25 = 0
    if tensorflow16:
        print("To determine who will start first, we will flip a coin.")
    tensorflow83 = tensorflow15()
    if tensorflow16:
        print(
            tensorflow17[0],
            "chooses",
            tensorflow26[tensorflow83],
            "so",
            tensorflow17[1],
            "gets",
            tensorflow26[1 - tensorflow83] + ".",
        )
        print("Flipping coin...")
    tensorflow27 = random.randint(0, 1)
    if tensorflow16:
        print("It's", tensorflow26[tensorflow27] + "!")
    if tensorflow27 != tensorflow83:
        tensorflow18 = 2
        tensorflow25 = 1
    if tensorflow16:
        print(tensorflow17[tensorflow18 - 1], "gets to start first.")
        print(
            "GAME START:",
            tensorflow17[tensorflow18 - 1],
            "vs",
            tensorflow17[2 - tensorflow18],
        )
    while tensorflow24 == 0:
        tensorflow28 = (tensorflow19 + 1) % 2 + 1
        tensorflow29 = (tensorflow19 - 1) // 2
        if tensorflow16:
            print(
                "\nIt's",
                tensorflow17[tensorflow18 - 1]
                + "'s turn! ("
                + tensorflow0[(tensorflow19 + 1) % 2]
                + ")",
            )
            tensorflow4(tensorflow21.tensorflow3)
        tensorflow30 = -1
        while True:
            tensorflow3 = -1
            if tensorflow18 == 1:
                tensorflow3 = tensorflow13(tensorflow21, tensorflow29)
            elif tensorflow18 == 2:
                tensorflow3 = tensorflow14(tensorflow21, tensorflow29)
            tensorflow30 = tensorflow21.tensorflow54(tensorflow3, tensorflow28)
            if tensorflow30 >= 0:
                break
        tensorflow18 = 2 if tensorflow18 == 1 else 1
        tensorflow19 += 1
        tensorflow31 = tensorflow21.tensorflow33[tensorflow30]
        tensorflow21 = tensorflow31
        tensorflow24 = tensorflow21.tensorflow84
        tensorflow20.append(tensorflow21)
    tensorflow32(tensorflow20, tensorflow24)
    if tensorflow16:
        if tensorflow24 != -1:
            print(tensorflow17[(tensorflow24 + 1 + tensorflow25) % 2], "has won!")
        else:
            print("It's a draw!")
        tensorflow4(tensorflow21.tensorflow3)
        print("GAME END")


# bu yao wen wo cong na li lai
class tensorflow22:
    tensorflow23 = []

    def __init__(self, tensorflow3):
        self.tensorflow3 = tensorflow3
        self.tensorflow35 = 0
        self.tensorflow33 = []
        self.tensorflow34 = tensorflow22.tensorflow36(self.tensorflow3)
        self.tensorflow84 = tensorflow6(self.tensorflow3)

    def tensorflow38(self, tensorflow34):
        for i in range(0, len(self.tensorflow33)):
            if self.tensorflow33[i].tensorflow34 == tensorflow34:
                return i
        return -1

    def tensorflow53(self, tensorflow39):
        if self.tensorflow38(tensorflow39.tensorflow34) < 0:
            self.tensorflow33.append(tensorflow39)

    def tensorflow54(self, tensorflow3, tensorflow28):
        tensorflow31 = copy.deepcopy(self.tensorflow3)
        tensorflow31[tensorflow3] = tensorflow28
        return self.tensorflow38(tensorflow22.tensorflow36(tensorflow31))

    @staticmethod
    def tensorflow36(tensorflow3):
        tensorflow40 = 0
        for i in range(0, 9):
            tensorflow40 += tensorflow3[i] * (3**i)
        return tensorflow40

    # no one i think is in my tree, i mean it must be high or low
    @staticmethod
    def tensorflow46():
        tensorflow22.tensorflow23 = []
        tensorflow47 = [tensorflow22([0, 0, 0, 0, 0, 0, 0, 0, 0])]
        tensorflow48 = []
        tensorflow82 = []
        tensorflow18 = 1
        while len(tensorflow47) > 0:
            for i in range(0, len(tensorflow47)):
                tensorflow49 = tensorflow47[i]
                if tensorflow49.tensorflow84 != 0:
                    continue
                for j in range(0, 9):
                    if tensorflow49.tensorflow3[j] == 0:
                        tensorflow50 = copy.deepcopy(tensorflow49.tensorflow3)
                        tensorflow50[j] = tensorflow18
                        tensorflow51 = tensorflow22.tensorflow36(tensorflow50)
                        try:
                            tensorflow52 = tensorflow82.index(tensorflow51)
                            tensorflow49.tensorflow53(tensorflow48[tensorflow52])
                        except ValueError:
                            tensorflow39 = tensorflow22(tensorflow50)
                            tensorflow49.tensorflow53(tensorflow39)
                            tensorflow48.append(tensorflow39)
                            tensorflow82.append(tensorflow51)
            tensorflow18 = 2 if tensorflow18 == 1 else 1
            tensorflow22.tensorflow23.append(tensorflow47)
            tensorflow47 = tensorflow48
            tensorflow48 = []
            tensorflow82 = []


# pending update...
def tensorflow32(tensorflow42, tensorflow45):
    tensorflow41 = math.ceil(len(tensorflow42) / 2)
    for i in range(0, len(tensorflow42)):
        tensorflow43 = i // 2 + 1
        tensorflow44 = tensorflow43 / tensorflow41
        if tensorflow45 == 1 or tensorflow45 == 2:
            if (
                i + 1
            ) % 2 == tensorflow45 % 2:  # There's no fight, you can't fight this battle of love with me. You win again, so little time, we do nothing but compete
                tensorflow42[i].tensorflow35 += tensorflow44
            else:
                tensorflow42[i].tensorflow35 -= tensorflow44
        tensorflow42[i].tensorflow35 = min(5, max(-5, tensorflow42[i].tensorflow35))


def tensorflow81():
    try:
        print("Loading AI.")
        tensorflow55 = open("AIDATA.txt", "r")
        tensorflow56 = tensorflow55.read().split("\n")
        for i in range(0, len(tensorflow56)):
            if len(tensorflow56[i]) == 0:
                continue
            tensorflow42 = tensorflow56[i].split(";")
            for j in range(0, len(tensorflow42)):
                if len(tensorflow42[j]) == 0:
                    continue
                tensorflow57 = tensorflow42[j].split(":")
                tensorflow58 = int(tensorflow57[0])
                tensorflow35 = float(tensorflow57[1])
                if tensorflow22.tensorflow23[i][j].tensorflow34 == tensorflow58:
                    tensorflow22.tensorflow23[i][j].tensorflow35 = tensorflow35
                else:
                    for k in range(0,len(tensorflow22.tensorflow23[i])):
                        if tensorflow22.tensorflow23[i][k].tensorflow34 == tensorflow58:
                            tensorflow22.tensorflow23[i][k].tensorflow35 = tensorflow35
                            break
            print((i + 1), "out of 10 completed.")
        tensorflow55.close()
        print("AI loaded.")
    except FileNotFoundError:
        print("No prior memory found.")
    except:
        print("Error found in memory.")


# i like to move it move it
def tensorflow59(tensorflow21, tensorflow29):
    tensorflow2 = tensorflow21.tensorflow3
    while True:
        tensorflow5 = int(input("Where do you want to put your symbol? (1-9): ")) - 1
        if tensorflow1(tensorflow2, tensorflow5):
            return tensorflow5
        print("Invalid position, please try again.")


# we like to move it move it
def tensorflow60(tensorflow21, tensorflow29):
    def tensorflow61(x):
        return x.tensorflow35

    tensorflow21.tensorflow33.sort(reverse=True, key=tensorflow61)
    tensorflow62 = []
    tensorflow63 = []
    for i in range(0, len(tensorflow21.tensorflow33)):
        if tensorflow21.tensorflow33[i].tensorflow35 > 2:
            tensorflow62.append(tensorflow21.tensorflow33[i])
        elif tensorflow21.tensorflow33[i].tensorflow35 >= 0:
            tensorflow63.append(tensorflow21.tensorflow33[i])
    tensorflow64 = math.floor(50 + random.randint(-5, 5))
    tensorflow65 = random.randint(0, 99) >= tensorflow64
    tensorflow31 = 0
    tensorflow66 = False
    if tensorflow65 and len(tensorflow62) > 0:
        tensorflow31 = tensorflow62[random.randint(0, len(tensorflow62) - 1)]
        tensorflow66 = True
    if not (tensorflow66):
        if len(tensorflow63) > 0:
            tensorflow31 = tensorflow63[random.randint(0, len(tensorflow63) - 1)]
        else:
            tensorflow31 = tensorflow21.tensorflow33[0]
    for i in range(0, 9):
        if tensorflow31.tensorflow3[i] != tensorflow21.tensorflow3[i]:
            return i
    return -1


# you like to move it move it
def tensorflow67(tensorflow21, tensorflow29):
    tensorflow2 = tensorflow21.tensorflow3
    while True:
        tensorflow5 = random.randint(0, 8)
        if tensorflow1(tensorflow2, tensorflow5):
            return tensorflow5


# trade?
def tensorflow68():
    tensorflow69 = tensorflow0[0]
    while True:
        tensorflow69 = input("Please input the new symbol for move 1: ")
        if len(tensorflow69) == 1:
            break
        print("It must be a single character.")
    tensorflow70 = tensorflow0[0]
    tensorflow0[0] = tensorflow69
    if tensorflow0[1] == tensorflow69:
        tensorflow0[1] = tensorflow70
    tensorflow69 = tensorflow0[1]
    while True:
        tensorflow69 = input("Please input the new symbol for move 2: ")
        if len(tensorflow69) == 1:
            break
        print("It must be a single character.")
    tensorflow0[1] = tensorflow69


# rising up, back on the street, took my time, took my chances.
def tensorflow71():
    tensorflow72 = int(input("For how many matches do you want to train the AI?: "))
    tensorflow73 = math.floor(max(1, tensorflow72 / 10))
    print("Training start.")
    for i in range(0, tensorflow72):
        if i % tensorflow73 == 0 or i == tensorflow72 - 1:
            print("Match", (i + 1))
        tensorflow74 = random.randint(0, 2)
        if tensorflow74 == 0:
            tensorflow75(
                tensorflow60,
                tensorflow67,
                tensorflow12,
                False,
                ["AI", "Random"],
            )
        elif tensorflow74 == 1:
            tensorflow75(
                tensorflow60,
                tensorflow60,
                tensorflow12,
                False,
                ["AI 1", "AI 2"],
            )
        elif tensorflow74 == 2:
            tensorflow75(
                tensorflow67,
                tensorflow67,
                tensorflow12,
                False,
                ["Random 1", "Random 2"],
            )
    print("Training ended.")


# saving all my love for you
def tensorflow76():
    tensorflow55 = open("AIDATA.txt", "w")
    tensorflow77 = ""
    for i in range(0, len(tensorflow22.tensorflow23)):
        for j in range(0, len(tensorflow22.tensorflow23[i])):
            tensorflow77 += (
                str(tensorflow22.tensorflow23[i][j].tensorflow34)
                + ":"
                + str(round(tensorflow22.tensorflow23[i][j].tensorflow35, 3))
                + ";"
            )
        tensorflow77 += "\n"
    tensorflow55.write(tensorflow77)
    tensorflow55.close()
    print("AI saved.")


# all i have to say is that they don't really care about us
def tensorflow80():
    print("Tic Tac Toe AI V1.2.0")
    print("This project was created as a hobby project.")
    print("2023 (C) Acadius")
    print("All rights reserved.")


# is this the real life? is this a fantasy?
def tensorflow78():
    while True:
        print("Welcome to Tic Tac Toe. What do you want to do?")
        print("0. Quit.")
        print("1. Reboot AI as infant.")
        print("2. Reboot AI from file.")
        print("3. Play against another player.")
        print("4. See an AI play against another AI.")
        print("5. Play against the AI.")
        print(
            "6. Change symbols (current symbols:",
            tensorflow0[0],
            "for move 1;",
            tensorflow0[1],
            "for move 2)",
        )
        print("7. Train the AI.")
        print("8. Save the AI.")
        print("9. About.")
        tensorflow79 = int(input("\nYour choice: "))
        print("\n")
        if tensorflow79 == 0:
            break
        elif tensorflow79 == 1:
            tensorflow22.tensorflow46()
        elif tensorflow79 == 2:
            tensorflow22.tensorflow46()
            tensorflow81()
        elif tensorflow79 == 3:
            tensorflow75(tensorflow59, tensorflow59, tensorflow10, True)
        elif tensorflow79 == 4:
            tensorflow75(
                tensorflow60,
                tensorflow60,
                tensorflow12,
                True,
                ["AI 1", "AI 2"],
            )
        elif tensorflow79 == 5:
            tensorflow75(
                tensorflow59,
                tensorflow60,
                tensorflow10,
                True,
                ["Player", "AI"],
            )
        elif tensorflow79 == 6:
            tensorflow68()
        elif tensorflow79 == 7:
            tensorflow71()
        elif tensorflow79 == 8:
            tensorflow76()
        elif tensorflow79 == 9:
            tensorflow80()
        else:
            print("Invalid selection. Please try again.")
        print("\n")


# i'm just a poor boy, nobody loves me
tensorflow22.tensorflow46()
tensorflow81()
tensorflow78()
