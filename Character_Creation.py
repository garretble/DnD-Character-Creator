### Character information up to date for version 4/11/13 ###

import random as r

def abilityScores():
    """ () -> list
    Randomly chooses six scores by adding top three d6
    rolls per score and appending those scores to a
    list. Returns that list.
    """

    scores_list = []

    for i in range(6):
        temp_list = []
        for j in range(4):
            temp_list.append(r.choice([1,2,3,4,5,6]))
        temp_list.sort()
        scores_list.append(temp_list[1]+temp_list[2]+temp_list[3])
    scores_list.sort()
    return scores_list


            
def chooseClass():
    """
    Asks player to choose a class for his/her character.
    """

    #Ask which class he/she would like
    
    #create list based on that choice to update stats [str,dex,con,int,wis,cha,hp]
    stats_list = []
    

    #modify hp if character is starting out higher than level 1
    #if self.level > 1:
        
    
class Character(object):

    def __init__(self,level):
        
        self.level = level
        print "You can use randomized ability scores: "+str(abilityScores())
        print "Or simply use the standard array: [8, 10, 12, 13, 14, 15]"
        print
        self.str = int(raw_input("Please enter STRENGTH value: "))
        self.dex = int(raw_input("Please enter DEXTERITY value: "))
        self.con = int(raw_input("Please enter CONSTITUTION value: "))
        self.int = int(raw_input("Please enter INTELLIGENCE value: "))
        self.wis = int(raw_input("Please enter WISDOM value: "))
        self.cha = int(raw_input("Please enter CHARISMA value: "))
        self.hp = 0
        print
        
    
        
    def getAbilityScores(self):
        """
        Prints the six ability scores for the character.
        """
        mods = [(self.str -10)/2,
                (self.dex-10)/2,
                (self.con-10)/2,
                (self.int-10)/2,
                (self.wis-10)/2,
                (self.cha-10)/2]
        print "STR: {0} ({1}) \nDEX: {2} ({3})\nCON: {4} ({5})".format(self.str,
                                                                       mods[0],
                                                                       self.dex,
                                                                       mods[1],
                                                                       self.con,
                                                                       mods[2])
        print "INT: {0} ({1})\nWIS: {2} ({3})\nCHA: {4} ({5})".format(self.int,
                                                                      mods[3],
                                                                      self.wis,
                                                                      mods[4],
                                                                      self.cha,
                                                                      mods[5])
        

    def updateScore(self,ability,amount):
        """
        Use to update an ability score manually.
        """
        abilities = {'str':'strength','dex':'dexterity',
                     'con':'constitution','int':'intelligence',
                     'wis':'wisdom','cha':'charisma'}
        if ability == 'str':
            self.str += amount
            print "You added {0} points to the {1} stat.".format(amount,abilities[ability])
        elif ability == 'dex':
            self.dex += amount
            print "You added {0} points to the {1} stat.".format(amount,abilities[ability])
        elif ability == 'con':
            self.con += amount
            print "You added {0} points to the {1} stat.".format(amount,abilities[ability])
        elif ability == 'int':
            self.int += amount
            print "You added {0} points to the {1} stat.".format(amount,abilities[ability])
        elif ability == 'wis':
            self.wis += amount
            print "You added {0} points to the {1} stat.".format(amount,abilities[ability])
        elif ability == 'cha':
            self.cha += amount
            print "You added {0} points to the {1} stat.".format(amount,abilities[ability])
        else:
            print "Please use 'str','dex','con','int','wis', or 'cha' as input."

        

    def stealthUpdate(self,ability,amount):
        """
        Use when needing to stealthily update stats.
        """
 
        if ability == 'str':
            self.str += amount
        elif ability == 'dex':
            self.dex += amount    
        elif ability == 'con':
            self.con += amount
        elif ability == 'int':
            self.int += amount
        elif ability == 'wis':
            self.wis += amount
        elif ability == 'cha':
            self.cha += amount
            
        
    
        
        
class Dwarf(Character):

    def __init__(self,level):

        Character.__init__(self,level)

        self.subclass = raw_input("Are you a (1) Hill Dwarf or (2) Mountain Dwarf? (input number) ")
        self.traits = {"Size":"Medium",
                       "Speed":"25 feet. Your speed is not reduced by wearing heavy armor with which you have proficiency or for carrying a heavy load.",
                       "Languages":"Common, Dwarven",
                       "Darkvision":"You treat darkness within 60 feet of you as dim light. When you do so, your vision is in  black and white.",
                       "Dwarven Resilience":"You have advantage on saving throws against poison, and you have resistance against poison damage.",
                       "Dwarven Weapon Training":"You are proficient with the battleaxe, handaxe, throwing hammer, and warhammer.",
                       "Stonecunning":"While you are underground, you have advantage on all Wisdom checks to listen and spot, and you roughly know your depth beneath the surface.\n  You also know the approximate age and origin of worked stone you inspect.",
                       }
        
        #if Hill Dwarf
        if self.subclass == '1':
            self.str += 1
            self.traits['Dwarven Toughness'] = 'Your hit point maximum increases by 1. and it increases by 1 every time you gain a level. Additionally, whenever you roll Hit Dice during a rest, you regain 1 extra hit point for each Hit Die you roll.'
            self.hp += 1
        #if Mountain Dwarf
        elif self.subclass == '2':
            self.wis += 1
            self.traits['Armor Mastery'] = 'You are proficient with light and medium armor. While wearing medium or heavy armor, you gain a +1 bonus to Armor Class.'

    def __str__(self):
        print "Level: "+str(self.level)
        self.getAbilityScores()
        print
        print "~~~~~~~~~Traits~~~~~~~~~ "
        for i in self.traits:
            print
            print "  ~~"+i+"~~"
            print"    "+str(self.traits[i])
        print
        return "End of Dwarf"

class Elf(Character):

    def __init__(self,level):

        Character.__init__(self,level)
 
        self.subclass = raw_input("Are you a (1) High Elf or (2) Wood Elf? (input number) ")
        self.traits = {"Size":"Medium",
                       "Languages":"Common, Elf",
                       "Speed": "30 Feet",
                       "Ability Score Adjustment":"You starting Dexterity score increases by 1.",
                       "Low-Light Vision":"You can see in dim light as well as you do in bright light.",
                       "Elf Weapon Training":"You are proficient with a long sword, short sword, shortbow, and longbow.",
                       "Keen Senses": "You have advantage on all Wisdom checks to listen and spot.",
                       "Free Spirit": "You are immune to the charmed condition and to any effect that would put you to sleep.",
                       "Trance": 'Elves do not need to sleep. Instead, they meditate deeply for 4 hours a day. (The Common word for such meditation is "trance.") While meditating, you can dream after a fashion; such dreams are actually mental excercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.',
                       
                       }
        #Added dex due to trait
        self.dex += 1

        #if High Elf
        if self.subclass == '1':
            self.int += 1
            self.traits['Extra Language'] = "You can speak, read, and write one extra language of your choice."
            self.traits['Cantrip'] = "You know one cantrip of your choice from the wizard's cantrip list. Intelligence is your magic ability for it."
        #if Wood Elf    
        elif self.subclass == '2':
            self.wis += 1
            self.traits['Speed'] = "35 Feet"
            self.traits['Fleet of Foot'] = "Your speed increases by 5 feet."
            self.traits['Mask of the Wild'] = 'You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.'

    def __str__(self):
        print "Level: "+str(self.level)
        self.getAbilityScores()
        print
        print "~~~~~~~~~Traits~~~~~~~~~ "
        for i in self.traits:
            print
            print "  ~~"+i+"~~"
            print"    "+str(self.traits[i])
        print
        return "End of Elf"

class Halfling(Character):

    def __init__(self,level):

        Character.__init__(self,level)

        self.subclass = raw_input("Are you a (1) Lightfoot or (2) Stout? (input number) ")
        self.traits = {"Size":"Small",
                       "Speed": "25 feet",
                       "Ability Score Adjustment": "Your starting Dexterity score increases by 1.",
                       "Languages":"Common, Halfling",
                       "Fearless":"You have advantage on saving throws against being frightened",
                       "Halfling Nimbleness":"You can move through the space of any creature that is of a size larger and yours.",
                       "Lucky":"When you roll a natural 1 on an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll.",
                       }

        #Added dex due to trait
        self.dex += 1

        #if Lightfoot
        if self.subclass == '1':
            self.cha += 1
            self.traits['Naturally Stealthy'] = "You can attempt to hide even when you are obscurred only by a creature that is one size category larger than you."
        #if Stout
        elif self.subclass == '2':
            self.con += 1
            self.traits['Stout Resilience'] = 'You have advantage on saving throws against poison, and you have resistance against poison damage.'

    def __str__(self):
        print "Level: "+str(self.level)
        self.getAbilityScores()
        print
        print "~~~~~~~~~Traits~~~~~~~~~ "
        for i in self.traits:
            print
            print "  ~~"+i+"~~"
            print"    "+str(self.traits[i])
        print
        return "End of Halfling"

class Human(Character):

    def __init__(self,level):

        Character.__init__(self,level)

        self.traits = {"Size":"Medium",
                       "Speed": "30 feet",
                       "Languages":"Common",
                       "Ability Score Adjustment":"Your starting ability scores each increase by 1."
                                               
                       }
        #A list of abilities 
        abilities_list = ['str','dex','con','int','wis','cha']
        #Add 1 to each ability score as guided by trait
        for i in abilities_list:
            self.stealthUpdate(i,1)
        
    '''
    def abilityScoreAdjustment(self):
        """
        This function is only called for Human races to calculate their
        upgraded ability scores as per called by their race.
        """
        #Asks which ability score to add 2 to (Human trait)
        score_plus_two = raw_input("Which Ability Score would you like to go up by 2? \n Pleast choose: str,dex,con,int,wis,cha ")

        #A list of the ability scores
        abilities_list = ['str','dex','con','int','wis','cha']

        #Updates score for chosen ability by 2 then removes it from list
        self.stealthUpdate(score_plus_two,2)
        abilities_list.pop(abilities_list.index(score_plus_two))

        #Updates all remaining scores by 1
        for i in abilities_list:
            self.stealthUpdate(i,1)
     '''
        
    def __str__(self):
        print "Level: "+str(self.level)
        self.getAbilityScores()
        print
        print "~~~~~~~~~Traits~~~~~~~~~ "
        for i in self.traits:
            print
            print "  ~~"+i+"~~"
            print"    "+str(self.traits[i])
        print
        return "End of Human"

