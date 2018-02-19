import individual
import random
import village
import building
import player
import rep_vars






def make_name(mother_name,father_name): # makes random names for the first generation
    nameMom=mother_name.split()
    nameMo=nameMom[1]
    nameM=nameMo.split("'")
    nameFat=mother_name.split()
    nameFa=nameFat[1]
    nameF=nameFa.split("'")
    name=str(rep_vars.name_list3[random.randrange(len(rep_vars.name_list3))])+" "+str(nameM[0])+"'"+str(nameF[1])
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
    indvm={"Meat":random.randrange(1,4), "Mobility": random.randrange(1,4),"Mind": random.randrange(1,4),"Mouth": random.randrange(1,4),"Mana": random.randrange(1,4),"Sex":1,"Favored":list(rep_vars.vtypes.keys())[random.randrange(len(rep_vars.vtypes))]}
    return indvm

def create_attributesF(): # returns the paternal chormosomes for a created individual
    indvf={"Meat":random.randrange(1,4), "Mobility": random.randrange(1,4),"Mind": random.randrange(1,4),"Mouth": random.randrange(1,4),"Mana": random.randrange(1,4),"Sex":random.randrange(2),"Favored":list(rep_vars.vtypes.keys())[random.randrange(len(rep_vars.vtypes))]}
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
                new_pop["{0}_indv{1}".format(name,child)]=individual.individuals(mommy.get_name(),daddy.get_name(),get_attributesM(daddy.get_attrM(),daddy.get_attrF()),get_attributesF(mommy.get_attrM(),mommy.get_attrF()))
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
                new_pop["{0}_indv{1}".format(name,child)]=individual.individuals(mommy.get_name(),daddy.get_name(),get_attributesM(daddy.get_attrM(),daddy.get_attrF()),get_attributesF(mommy.get_attrM(),mommy.get_attrF()))
                new_pop["{0}_indv{1}".format(name,child)].set_hometown(name)
            del popm[list(popm.keys())[dadloc]]
            del popf[list(popf.keys())[momloc]]
    for i in popdict:
        popdict[i].death()
    return new_pop





