if __name__ == "__main__":
    while True:
        print("'hello, friend.'")
        print("'I'm glad you're awake. I was beginning to feel lonely.'")
        print("'I know this may be hard to believe but we're in some weird cave right now.'")
        print("'There may be some options to leave.'")
        print("'To make sure that you're acutally here, what's your name?'")
        name = input()
        print("Alright " +name+ ", let's stand up.")
        introScene()

def introScene():
    wait = ["wait, tomorrow"]
    door = ["try, door, attempt"]
    print("I haven't found much while staying here. There is a barrel, which I have been finding comfort in for the last few days. A creek on the wall has let dropplets of water that I collected on this bucket. Lastly, the door in front of us is locked, but we get our only source of light through the edges of the door. Should we try the door again right now or wait until tomorrow?'")
    userInput = "" 
    print("I don't mind waiting another day.")
    while userInput not in wait and door:
    userInput = input()
    if userInput == "wait, tomorrow":
        nextDayScene()
    elif userInput == "try, door, attempt":
        DoorScene()
    else:
        print("can you say stuff related to the question? your head must be hurting again")

def DoorScene ():
    open = ["open the door"]
    sit_down = ["sit down"]
    print("okay, but before you try it, just know that it's been days since I actually tried opening the door...")