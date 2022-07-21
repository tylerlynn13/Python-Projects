




def start():
    f_name = "Tyler"
    l_name = "Stamper"
    age = 21
    gender = "Female"
    get_info(f_name,l_name,age,gender)


def get_info(f_name,l_name,age,gender):
    print("My name is () (). I am () yearold ().".format(f_name,l_name,age,gender))




def start(nice=0,mean=1,name=""):
    # get users name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
from colorama import Fore, Back, Style

print(Fore.RED + 'Nice or Mean Game')

def describe_game(name):
    """
        check if new game
        if it is, get users name
        if it is not thanke the player
    """
    #meaning, if we not already have the users name
    #then they are a new player and need to get their name
    if name !="":
        print("\nThank you for palying again, ()!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, ()!".format(name))
                    print("\nIn this game you be greeted \nby different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions")
                    stop = False

    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice +1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean +1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()





def show_score(nice,mean,name):
    print("\n(), your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))



def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variable
    if nice > 2: # if condtion is vald, call win functuon
        win(nice,mean,name)
    if mean> 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)



def win(nice,mean,name):
    #Substitute the {} wildcards with in our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    #call again function and pass our variables
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>" ).lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES' ( N ) for 'NO':\n>>>")



def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)


if __name__== "__main__":
    start()
        
