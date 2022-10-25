def displayIntro():
    print( "hello, friend. \nI'm glad you're awake now, I was beginning to feel alone.\n" + 
    "I know this may be hard to believe but we're in some weird cave right now.\n" + 
    "There are some options to leave this room.")

def getUserName():
    userName = input( "But just to make sure that you're actually here, what's your name: " )
    return userName

def askDoorQuestion(username):
    print("Alright " + username + ", let's stand up. I haven't found much while in here.\nI found comfort in an empty barrel the last few days and" + 
    " there is a creek on the wall that has let dropplets of water leaking through onto this bucket I found.\n" + 
    "Lastly, the door in front of us is locked, but it is where our only source of light is coming from.")
    answerToDoor = input("Should we try the door now or wait until tomorrow?\ntype in (door or wait): ")

    while answerToDoor != "door" and answerToDoor != "wait":
        answerToDoor = input("Please correct! Should we try the door now or wait until tomorrow?\ntype in (door or wait): ")

    return answerToDoor

def revealAnswerToDoorQuestion(answerToDoor):
    if answerToDoor.lower() == "door":
        print()
        # Call door function
    elif answerToDoor.lower() == "wait":
        #call wait function
        print()
    else:
        print()


def DoorScene(answerToDoor):
    print("Okay, but before you check the door")


def main():
    displayIntro()
    userName = getUserName()
    answerToDoor = askDoorQuestion(userName)
    print("You typed", answerToDoor)

main()
