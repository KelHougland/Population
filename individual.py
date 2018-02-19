import random
import building
import player
import village
import rep_vars
import helpers



# skills={"Fight":0,"Talk":0,"Think":0,"Pray":0,"Hunt":0,"Shoot":0,"Make":0} # potential skills for reference


############  THIS SECTION IS FOR EVERYTHING HAVING TO DO WITH THE INDIVIDUALS CLASS ############

class individuals:         # Inidviduals after the starting generation need to have parents, attributes, tendencies, skills, and classes

    # let's initialize us some people
    def __init__(self, init_mother, init_father,init_attrF,init_attrM):
        self.mother=init_mother # this is really just for reference
        self.father=init_father # this is really just for reference
        self.attributesM=init_attrM # this is generated in the villiage class
        self.attributesF=init_attrF # this is generated in the village class
        self.attributes={}
        for i in self.attributesF:
            if type(self.attributesF[i])==str:
                self.attributes[i]=(self.attributesF[i]+" "+self.attributesM[i])
            else:
                self.attributes[i]=(self.attributesF[i]+self.attributesM[i])
        self.skills={} #these start at 0 and will update later
        self.classes={} # this will be generated later as they train
        self.name=helpers.make_name(self.mother,self.father) #the maternal lines are inhereted through females and paternal lines through males
        self.alive=True # individuals will be marked dead and stored in a dead file, players will be able to spend dead souls for god benefits
        self.health= self.attributes["Meat"]+5# all players start with health based on their Meat score
        self.mana=self.attributes["Mana"]+5 # all players start with mana based on their Mana score
        self.hometown=''
        
    
    def get_name(self): # returns the name for reference
        return self.name

    def get_parents(self): # returns the parents for reference
        return (self.mother,self.father)

    def get_attrF(self): # returns the chromosomes inhereted from father
        return self.attributesF

    def get_attrM(self): # returns chromosomes inhereted from mother
        return self.attributesM

    def get_attr(self): # returns the total attributes for the individuals
        return self.attributes

    def death(self): # kills the individual
        self.alive=False
        return self.alive
    
    def get_sex(self): # this function determines whether the individual is a male or female
        if (self.attributesM["Sex"]+self.attributesF["Sex"])==2:
            self.sex="Female"
        else:
            self.sex="Male"
        return self.sex

    def emmigrate(self,vill):
        indv_pref=self.attributes["Favored"].split()
        prob_leave=2
        for i in indv_pref:
            if indv_pref==vill.get_type():
                prob_leave=prob_leave-1
        if random.randrange(6)<prob_leave:
            return "Leave"
    
    def immigrate(self,vill):
        indv_pref=self.attributes["Favored"].split()
        prob_leave=0
        for i in indv_pref:
            if indv_pref==vill.get_type():
                prob_leave+=1
        if random.randrange(4)<=prob_leave:
            return "Leave"
    
    
    def set_hometown(self,hometown):
        self.hometown=hometown
             

    def summary(self):
        self.meanatt={}
        for i in self.attributes:
            if type(self.attributes[i])==int:
                self.meanatt[i]=self.attributes[i]

        return str(self.name) + " " + str(sum(self.meanatt.values())/len(self.meanatt)) #+ " " + str(sum(self.skills.values())/len(self.skills))

