import random
import rep_vars
import individual
import building
import player
import helpers
import rep_main

def outside_gen(adict): # run the outside group through a generation, adict=outsiders
    new_out=next_generation("out",adict)
    global outsiders
    outsiders=new_out
    return outsiders

outsiders={} # this is going to be the wanderers that individuals emigrate to and from 
for i in range(15):

    mom_name=str(rep_vars.name_list3[random.randrange(len(rep_vars.name_list3))])+" "+str(rep_vars.name_list1[random.randrange(len(rep_vars.name_list1))])+"'"+str(rep_vars.name_list2[random.randrange(len(rep_vars.name_list2))])
    dad_name=str(rep_vars.name_list3[random.randrange(len(rep_vars.name_list3))])+" "+str(rep_vars.name_list1[random.randrange(len(rep_vars.name_list1))])+"'"+str(rep_vars.name_list2[random.randrange(len(rep_vars.name_list2))])   
    outsiders["outside_indv{0}".format(i)]=individual.individuals(mom_name,dad_name,helpers.create_attributesM(),helpers.create_attributesF())
    outsiders["outside_indv{0}".format(i)].set_hometown("Outside")



class village: # villages must have a type, max building slots, food production, max population size based on food production, technology level, and magic

    def __init__(self,init_name,init_player):
        self.name=init_name
        self.limits={"Buildings": 4, "Income": 50, "Population": 15, "Food":15, "Technology": 10, "Magic": 10}
        self.generation=0
        self.tech=0
        self.magic=0
        self.owner=init_player

    def set_type(self,vtype): # this sets teh village type that determines how it grows
        self.type=vtype
        self.growth=rep_vars.vtypes[self.type]
        for i in self.limits:
            self.limits[i]+=self.growth[i]
        self.buildings=[]

    def get_type(self):
        return self.type

    def set_population(self): # this generates the individuals for the initial population
        self.population={}
        for i in range(self.limits["Population"]):
            mom_name=str(rep_vars.name_list3[random.randrange(len(rep_vars.name_list3))])+" "+str(rep_vars.name_list1[random.randrange(len(rep_vars.name_list1))])+"'"+str(rep_vars.name_list2[random.randrange(len(rep_vars.name_list2))])
            dad_name=str(rep_vars.name_list3[random.randrange(len(rep_vars.name_list3))])+" "+str(rep_vars.name_list1[random.randrange(len(rep_vars.name_list1))])+"'"+str(rep_vars.name_list2[random.randrange(len(rep_vars.name_list2))])   
            self.population["{0}_indv{1}".format(self.name,i)]=individual.individuals(mom_name,dad_name,helpers.create_attributesM(),helpers.create_attributesF())
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
        self.new_pop=helpers.next_generation(self.name,self.population)
        while len(self.new_pop)>self.limits["Population"]:
            self.leavers={}
            for i in self.new_pop:
                if self.new_pop[i].emmigrate(self)=="Leave":
                    outsiders[i]=self.new_pop[i]
                    self.leavers[i]=self.new_pop[i]
            for i in self.leavers:
                del self.new_pop[i]

        for i in outsiders:
            if [i].immigrate(self)=="Leave":
                self.new_pop[i]=[i]
        

        self.old_pop=self.population.copy() # saves the population to be added to the list of the dead
        self.new_souls=open("{0}'s Souls.txt".format(self.get_owner()),'a+')
        for i in self.old_pop:
            self.output=self.old_pop[i].summary()
            self.new_souls.write(self.output + '\n')
        self.new_souls.close()

        self.population=self.new_pop.copy() # updates the population to the new individuals

    def build(self,buildtype): # let's build something
        if len(self.buildings)<self.limits["Buildings"]:
            self.buildings.append(building.building(buildtype))
            
