# This is where we make the individuals in the villages grow with each generation
# I need five classes individuals, villages, buildings, outsiders, and players
        
       

        # players must have names, login information, an associated village, angels, and god power

## TODO: Allow players to choose angels from population each gen, add gen tracker on indviduals, figure out how to use souls for things and delete them from the log
    ##: create lesson data base and figure out how to keep track of what lesson's a player has access to in their buildings, add max lessons and indv to building per level

############  THIS SECTION IS FOR IMPORTING MODULES I WANT TO USE ############

import random









############  THIS SECTION IS FOR INITIALIZING GLOBAL VARIABLES OUTHER THAN OUTSIDERS ############

name_list1=["O","El","De","Mac","Al","Yi","Un","Ya","Fil","La","Num","Fahn","Lok","Oth","Gol","Ti","Mng","Doth","Cumber","Chic"]
name_list2=["Donnel", "Dabumbum","Lothar","Azar","Smith","Batch","Chorro","Okgar","Lee","Yang","Ashon","Szar","Baqueta","Ocho","Chakrabourti","Heta","Dopplepopulous","Yan","Kor"]
name_list3=["Ed", "Pescador", "Beija", "Buscape", "Marinheio","Moonwhisper","Clef","Claudio","Miguel","Frank","Susy","Najeebah","Gunter","Rob","Brian","Jared","Keith","Cheri","Vicky","Nathan","Cebo","Kel"]
vtypes={"Farming" : {"Buildings": 1, "Income": 0, "Population": 0, "Food":5, "Technology":0, "Magic":0}, "Riverside":{"Buildings": 0, "Income": 10, "Population": 5, "Food":0, "Technology":0, "Magic":0}, "Mountainside": {"Buildings": 0, "Income": 10, "Population": 0, "Food":0, "Technology":2, "Magic":0},"Woodland":{"Buildings": 0, "Income": 0, "Population": 0, "Food":5, "Technology":0, "Magic": 2},"Swamp":{"Buildings": 0, "Income": 0, "Population": 0, "Food":0, "Technology": 3, "Magic": 3},"Desert":{"Buildings": 1, "Income": 0, "Population": 0, "Food":0, "Technology": 0, "Magic": 2}}
btypes={"Hunting Lodge":{"Hunt":2,"Shoot":1}, "Shrine": {"Pray":2,"Talk":1}, "Fighting Pit": {"Fight":2,"Shoot": 1},"Communal Hut": {"Talk":2,"Think":1}, "Crafting Area": {"Make":2,"Think":1} }


# skills={"Fight":0,"Talk":0,"Think":0,"Pray":0,"Hunt":0,"Shoot":0,"Make":0} # potential skills for reference







    
############  THIS SECTION IS FOR LISTING MY HELPER FUNCTIONS ############

def make_name(mother_name,father_name): # makes random names for the first generation
    nameMom=mother_name.split()
    nameMo=nameMom[1]
    nameM=nameMo.split("'")
    nameFat=mother_name.split()
    nameFa=nameFat[1]
    nameF=nameFa.split("'")
    name=str(name_list3[random.randrange(len(name_list3))])+" "+str(nameM[0])+"'"+str(nameF[1])
    return name

def get_attributesM(father_attM,father_attF): # determines the maternal chromosomes for a born individual
    indvm={"Meat":0, "Mobility": 0,"Mind": 0,"Mouth": 0,"Mana": 0,"Sex":0,"Favored":0}
    for i in father_attM:
        coin=random.randrange(2)
        if coin==0:
            indvm[i]=father_attM[i]
        elif coin==1:
            indvm[i]=father_attF[i]

    return indvm

def get_attributesF(mother_attM,mother_attF): # determines the paternal chromosomes for a born individual
    indvf={"Meat":0, "Mobility": 0,"Mind": 0,"Mouth": 0,"Mana": 0,"Sex":0,"Favored":0}
    for i in mother_attM:
        coin=random.randrange(2)
        if coin==0:
            indvf[i]=mother_attM[i]
        elif coin==1:
            indvf[i]=mother_attF[i]

    return indvf

def create_attributesM(): # returns the maternal chromosomes for a created individual
    indvm={"Meat":random.randrange(1,4), "Mobility": random.randrange(1,4),"Mind": random.randrange(1,4),"Mouth": random.randrange(1,4),"Mana": random.randrange(1,4),"Sex":1,"Favored":list(vtypes.keys())[random.randrange(len(vtypes))]}
    return indvm

def create_attributesF(): # returns the paternal chormosomes for a created individual
    indvf={"Meat":random.randrange(1,4), "Mobility": random.randrange(1,4),"Mind": random.randrange(1,4),"Mouth": random.randrange(1,4),"Mana": random.randrange(1,4),"Sex":random.randrange(2),"Favored":list(vtypes.keys())[random.randrange(len(vtypes))]}
    return indvf

def next_generation(name,popdict):
    popsex={}
    for i in popdict:# returns the sexes of all individuals
        popsex[i]=popdict[i].get_sex()
    popm={} # the next chunk separates the males and females in the population
    popf={}
    for i in popsex:
        if popsex[i]=='Male':
            popm[i]=popdict[i]
        else:
            popf[i]=popdict[i]
    new_pop={} # now we start the mating
    if len(popm)<len(popf):
        while len(popm)>0:
            dadloc=random.randrange(len(popm)) # determines the father
            momloc=random.randrange(len(popf)) # determines the mother
            daddy=list(popm.values())[dadloc] # pulls the father from the list
            mommy=list(popf.values())[momloc] # pulls the mother from the list
            for child in range(len(new_pop),(len(new_pop)+random.randrange(3,6))): # this generates a new individual for each child a family has adds it to the family
                new_pop["{0}_indv{1}".format(name,child)]=individuals(mommy.get_name(),daddy.get_name(),get_attributesM(daddy.get_attrM(),daddy.get_attrF()),get_attributesF(mommy.get_attrM(),mommy.get_attrF()))
                new_pop["{0}_indv{1}".format(name,child)].set_hometown(name)
            del popm[list(popm.keys())[dadloc]] # deletes the father so they don't reproduce again
            del popf[list(popf.keys())[momloc]] # deletes the mother so they don't reproduce again 
    elif len(popf)<len(popm): # does the same things as above but used if there are more males than females in the population
        while len(popf)>0:
            dadloc=random.randrange(len(popm))
            momloc=random.randrange(len(popf))
            daddy=list(popm.values())[dadloc]
            mommy=list(popf.values())[momloc]
            for child in range(len(new_pop),(len(new_pop)+random.randrange(3,6))):
                new_pop["{0}_indv{1}".format(name,child)]=individuals(mommy.get_name(),daddy.get_name(),get_attributesM(daddy.get_attrM(),daddy.get_attrF()),get_attributesF(mommy.get_attrM(),mommy.get_attrF()))
                new_pop["{0}_indv{1}".format(name,child)].set_hometown(name)
            del popm[list(popm.keys())[dadloc]]
            del popf[list(popf.keys())[momloc]]
    for i in popdict:
        popdict[i].death()
    return new_pop


def outside_gen(adict): # run the outside group through a generation, adict=outsiders
    full_gen=next_generation("out",adict)
    while len(full_gen)>100:
        del full_gen[random.choice(list(full_gen.keys()))]
    else: new_out = full_gen.copy()
    global outsiders
    outsiders=new_out.copy()
    






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
        self.name=make_name(self.mother,self.father) #the maternal lines are inhereted through females and paternal lines through males
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















############  THIS IS WHERE I INITIALIZE THE OUTSIDERS POPULATION ############
def init_outsiders():
    global outsiders
    outsiders={} # this is going to be the wanderers that individuals emigrate to and from 
    for i in range(15):

        mom_name=str(name_list3[random.randrange(len(name_list3))])+" "+str(name_list1[random.randrange(len(name_list1))])+"'"+str(name_list2[random.randrange(len(name_list2))])
        dad_name=str(name_list3[random.randrange(len(name_list3))])+" "+str(name_list1[random.randrange(len(name_list1))])+"'"+str(name_list2[random.randrange(len(name_list2))])   
        outsiders["outside_indv{0}".format(i)]=individuals(mom_name,dad_name,create_attributesM(),create_attributesF())
        outsiders["outside_indv{0}".format(i)].set_hometown("Outside")
    











############  THIS SECTION IS FOR EVERYTHING HAVING TO DO WITH THE VILLAGE CLASS ############    

class village: # villages must have a type, max building slots, food production, max population size based on food production, technology level, and magic

    def __init__(self,init_name,init_player):
        self.name=init_name
        self.limits={"Buildings": 4, "Income": 50, "Population": 15, "Food":15, "Technology": 10, "Magic": 10}
        self.generation=0
        self.tech=0
        self.magic=0
        self.owner=init_player
        self.growth={"Buildings": 1, "Income": 10, "Population": 5, "Food":5, "Technology": 5, "Magic": 5}
        

    def set_type(self,vtype): # this sets teh village type that determines how it grows
        self.type=vtype
        for i in self.growth:
            self.growth[i]+=vtypes[self.type][i]
        for i in self.limits:
            self.limits[i]+=self.growth[i]
        self.buildings=[]

    def get_type(self):
        return self.type

    def set_population(self): # this generates the individuals for the initial population
        self.population={}
        for i in range(self.limits["Population"]):
            mom_name=str(name_list3[random.randrange(len(name_list3))])+" "+str(name_list1[random.randrange(len(name_list1))])+"'"+str(name_list2[random.randrange(len(name_list2))])
            dad_name=str(name_list3[random.randrange(len(name_list3))])+" "+str(name_list1[random.randrange(len(name_list1))])+"'"+str(name_list2[random.randrange(len(name_list2))])   
            self.population["{0}_indv{1}".format(self.name,i)]=individuals(mom_name,dad_name,create_attributesM(),create_attributesF())
            self.population["{0}_indv{1}".format(self.name,i)].set_hometown(self.name)

    def get_limits(self): # returns the limits of the village for reference
        return print(self.limits)
    
    def get_popnames(self): # returns the current population for reference
        for i in self.population:
            indv=self.population[i]
            print(indv.get_name())
            
    def get_population(self): #returns the population dictionary
        return self.population
            
    def get_gen(self): # returns the current generation
        return self.generation

    def get_owner(self):
        return self.owner.name

      
    def next_gen(self): # make sure to save the old population to the list of the dead
        self.generation+=1 # updates generation
        for i in self.limits: # updates the limits according to village growth
            self.limits[i]+=self.growth[i]
        self.new_pop={}
        self.new_pop=next_generation(self.name,self.population)

        for i in outsiders:
            if outsiders[i].immigrate(self)=="Leave":
                self.new_pop[i]=outsiders[i]
        
        while len(self.new_pop)>self.limits["Population"]:
            self.leavers={}
            for i in self.new_pop:
                if self.new_pop[i].emmigrate(self)=="Leave":
                    outsiders[i]=self.new_pop[i]
                    self.leavers[i]=self.new_pop[i]
            for i in self.leavers:
                del self.new_pop[i]
                
        

        

        self.old_pop=self.population.copy() # saves the population to be added to the list of the dead
        self.new_souls=open("{0}'s Souls.txt".format(self.get_owner()),'a+')
        for i in self.old_pop:
            self.output=self.old_pop[i].summary()
            self.new_souls.write(self.output + '\n')
        self.new_souls.close()

        self.population=self.new_pop.copy() # updates the population to the new individuals

    def build(self,buildtype): # let's build something
        if len(self.buildings)<self.limits["Buildings"]:
            self.buildings.append(building(buildtype))
            










############  THIS SECTION IS FOR EVERYTHING HAVING TO DO WITH THE BUILDING CLASS ############  

class building:  # buildings must have their special attributes, levels, dependencies, and available classes

    def __init__(self,init_buildtype):
        self.building=init_buildtype
        self.level=1
        self.lessons=[btypes[self.building]]

    def add_lesson(self,new_lesson):
        self.lessons.append(new_lesson)

    def get_test(self):
        return self.lessons










############  THIS SECTION IS FOR EVERYTHING HAVING TO DO WITH THE PLAYER CLASS ############  
class player:

    def __init__(self):
        self.name=input("What is your Name?")
        self.deity_type=input("What kind of God are you?")
        self.vill=village(input("What Village's Name?"),self)
        self.souls=open("{0}'s Souls.txt".format(self.name),'w+')
        self.souls.close()



    








# below is the code that returns the average for a value within a population
# for i in d.get_population():
   # meat+=a[i].get_attr()["Meat"]
# meanmeat=meat/len(d.get_population())