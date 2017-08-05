from sys import argv


def Gold_Room():
    print "You are in a golden mine, collect some gold \n >"
    result = raw_input()
    if result.isdigit() == False or int(result) > 10:
        print "Your are so greedy! go hell!"
        DeadMan("greedy")
        return -10
    elif result.isdigit() == True and int(result) <= 10:
        print "You are a good guy, get the gold!"
        return int(result)
    else:
        print "Give the number! fool"
        DeadMan("foolish")
        return -10


def Exit_Room():
    print "You safely exit from the Dungeon, good luck!"

def DeadMan(Reason):
    print "You are deadman because of %s, lost of 10 gold" %(Reason)

def Right_Room():
    print "You are in a dark room with a pool, what's the next steps? \n >",
    action = raw_input()
    if action == "swimming":
        print "You go cross the cold water and escape to the Exit"
        Exit_Room()
        return 0
    else:
        DeadMan("starve")
        return -10

def Middle_Room():
    print "You are falling into a trap, pighead"
    DeadMan("starve")
    return -10

def Left_Room():
    print "You are in front of a gaint Dragons, what's the next?"
    action = raw_input()
    if action == "fight":
        print "You kill the dragon with your sword, well done!"
        return Gold_Room()
    elif action == "flight":
        print "You are burning by the dragon's fire"
        DeadMan("burning")
        return -10
    else:
        print "Your should fight or flight, fool"
        DeadMan("foolish")
        return -10

script, username, life = argv

life = argv[2]
if life.isdigit() == False or life < 0 or life > 3:
    DeadMan("Input the right number of third argument in the range 1-3")



Gold = 0

for life in range(0, int(argv[2])):
    print "Hi, %s Welcome to Dungeon and Dragons" %(argv[1])
    print "There are three room in front of you. What's your selection? (R/M/L) \n >",
    choice = raw_input()
    if choice == "R" or choice == "r":
        Gold += Right_Room()
    elif choice == "M" or choice == "m":
        Gold += Middle_Room()
    elif choice == "L" or choice == "l":
        Gold += Left_Room()
    else:
        print "Input R/M/L, You Bastard!"
        life -= 1

print ("Your final wealth is %s after %s try" %(Gold, argv[2]))
