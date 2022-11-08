def displayIntro():  #introduction scene 
    print( "hello, friend. \n \nI'm glad you're awake now, I was beginning to feel alone.\n \n" + 
    "I know this may be hard to believe but we're in some weird cave right now.\n \n" + 
    "There are some options to leave this room.")

def getUserName(): #question for players name
    userName = input( "But just to make sure that you're actually here, what's your name: " )
    return userName

def askDoorQuestion(username):    #first scene, dialogue being provided to ask if they want to check the door or wait
    print("Alright " + username + ", let's stand up. I haven't found much while in here.\n \nI found comfort in an empty barrel the last few days and" + 
    " there is a creek on the wall that has let dropplets of water leaking through onto this bucket I found.\n \n" + 
    "Lastly, the door in front of us is locked, but it is where our only source of light is coming from.")
    answerToDoor = input("Should we try the door now or wait until tomorrow?\n \ntype in (door or wait): ")

    while answerToDoor != "door" and answerToDoor != "wait":    #depending on what the person chooses, it'll direct them through these two options
        answerToDoor = input("try a word related to the question.\n \ntype in (door or wait): ")
    return answerToDoor

def playDoorScene(answerToDoor):   
    if answerToDoor.lower() == "door":   #if player chose door, this is where is will lead.
        print("*you go to attempt the door*")
        userConfirmationAnswer = doorScene()    # Call door function
        # return userConfirmationAnswer
    elif answerToDoor.lower() == "wait": #if player chooses to wait, it'll lead them here
        #call wait function
        # print("*you decided to wait until tomorrow*")
        #waitUntilTomorrow()
    else:
        print("hm? can you say that again?\ntype in (door or wait): ")


# def doorScene():
#     print("Before you open the door, it did sound scary out there earlier.\nAll I heard was a bunch of slams and crashes for days.")
#     userConfirmationAnswer = input("are you sure you don't want to wait a little longer?\ntype in (open door or wait): ") #change variable name 

#     while userConfirmationAnswer.lower != "open door" and userConfirmationAnswer.lower != "wait":
#         userConfirmationAnswer = input("Try a word related to the question.\ntype in (open door or wait): ")
#     return userConfirmationAnswer

# def revealConfirmToOpenDoor(userConfirmationAnswer):
#     userConfirmationAnswerToLowercase = userConfirmationAnswer.lower() # Convert to lowercase so we can properly compare

#     if userConfirmationAnswerToLowercase == "open door":
#         # print("*you finally go to open the door*\n*the door is unlocked*")
#         return userConfirmationAnswerToLowercase
#     elif userConfirmationAnswerToLowercase == "wait":
#         return userConfirmationAnswerToLowercase
#         # print("*you decided to officially wait*")
#     else:
#         return 0 # You didn't type open door or wait

# def tunnelHallway(): #don't need to carry over variable from last function
#     print("oh.\nthe door was open all along.\n*it's only a long cave-like tunnel that leads to some bright light at the other end of it*")
#     enterTheTunnel = input("*do you want to enter?*\ntype in (yes or no): ")

#     while enterTheTunnel != "yes" and enterTheTunnel != "no":
#         enterTheTunnel = input("try a word related to the question.\ntype in (yes or no): ")
#         return enterTheTunnel

# def revealTunnelHallwayEntrance(enterTheTunnel):
#     if enterTheTunnel.lower() == "yes":
#         print("just check out the light and come right back, please.")
#         confirmEntranceToTunnel = input("type in (enter) when you're ready to leave: ") 
#         theLightAtTheEnd()
#     elif enterTheTunnel.lower() == "no":
#         print("*i think i'm too scared to go.*\n*how about we just sit down and wait a bit longer?*")
#         cancelTunnel = input("type in (sit down) when you're ready to stay: ")
#         # floorScene()
#     else:
#         print("*I have to make a decision right now*\ntype in (yes or no): ")

# def theLightAtTheEnd():
#     print("*you enter the tunnel*\n \n*its very dark, but i can see just enough*\n \n*it's getting bright*\n \n*did i make it out yet?*")

def main():
    displayIntro()
    userName = getUserName()
    answerToDoor = askDoorQuestion(userName)
    # Determine what happens when the user selects door or wait





    # print("You typed", answerToDoor)
    # revealAnswerToDoorQuestion()
    # doorScene()
    # confirmToOpenDoor = doorScene()
    # print("you typed", confirmToOpenDoor)
    # revealConfirmToOpenDoor()
    # tunnelHallway()
    # enterHallway = tunnelHallway()



main()
