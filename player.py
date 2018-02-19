import random
import rep_vars
import helpers
import village
import individual
import building



class player:

    def __init__(self):
        self.name=input("What is your Name?")
        self.deity_type=input("What kind of God are you?")
        self.vill=village.village(input("What Village's Name?"),self)
        self.souls=open("{0}'s Souls.txt".format(self.name),'w+')
        self.souls.close()

