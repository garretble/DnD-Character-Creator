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
        abilities = {'str':'strength','dex':'dexterity',
                     'con':'constitution','int':'intelligence',
                     'wis':'wisdom','cha':'charisma'}
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
                       "Speed":25,
                       "Languages":"Common, Dwarven",
                       "Low-Light Vision":"If there is no light within 30 feet of you, you treat shadows in that radius as normal light, and you treat darkness in that radius as shadows.",
                       "Dwarven Resilience":"You are immune to damage and other effects from poison.",
                       "Dwarven Weapon Training":"When you attack with an axe or a hammer with which you are proficient, the damage die for that weapon increases by one step: from d4 to d6, d6 to d8, d8 to d10, d10 to d12, and d12 to 2d6",
                       "Stonecunning":"While underground, you know your approximate depth and how to retrace your path. You can identify the age of visible stonework and make a reasonable guess as to the culture responsible for its construction.",
                       }
        
        
        if self.subclass == '1':
            self.str += 1
            self.traits['Dwarven Toughness'] = 'All your Hit Dice increase by one step: from d4 to d6, d6 to d8, d8 to d10, d10 to d12, and d12 to 2d6. At 1st level, you gain 1 extra hit point. Whenever you gain a level, you similarly increase the die rolled to determine how many hit points you gain (or simply gain 1 extra hit point per level).'
            
        elif self.subclass == '2':
            self.cha += 1
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
                       "Low-Light Vision":"If there is no light within 30 feet of you, you treat shadows in that radius as normal light, and you treat darkness in that radius as shadows.",
                       "Elf Weapon Training":"When you attack with a longsword, a shortbow, or a longbow with which you have proficiency, the damage die for that weapon increases by one step: from d6 to d8, or d8 to d10.",
                       "Keen Senses": "You have advantage on checks made to listen to, search for, or notice something.",
                       "Free Spirit": "You are immune to the charmed condition and to any effect that would put you to sleep.",
                       "Trance": 'Elves do not need to sleep. Instead, they meditate deeply for 4 hours a day. (The Common word for such meditation is "trance.") While meditating, you can dream after a fashion; such dreams are actually mental excercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.',
                       
                       }
        
        if self.subclass == '1':
            self.int += 1
            self.traits['Speed'] = 30
            self.traits['Cantrip'] = "Choose one minor spell from the wizard's spell list. You know and can cast this spell. Intelligence is your magic ability for it."
            
        elif self.subclass == '2':
            self.dex += 1
            self.traits['Speed'] = 35
            self.traits['Wood Elf Grace'] = 'You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.'

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
                       "Speed": 25,
                       "Languages":"Common, Halfling",
                       "Halfling Weapon Training":"When you attack with a dagger, a short sword, or a sling with which you have proficiency, the damage die for that weapon increases by one step: from d4 to d6, or d6 to d8.",
                       "Lucky": "Twice per day, when you make an attack roll, check, or saving throw and get a result you dislike, you can reroll the die and use either result. If you have advantage or disadvantage on the roll, you reroll only one of the dice.",
                       "Halfling Nimbleness": "You can move through the spaces of hostile creatures that are larger than you.",
                       
                       }
        
        if self.subclass == '1':
            self.dex += 1
            self.traits['Naturally Stealthy'] = "You can attempt to hide even when you are obscurred only by a creature that is one size category larger than you."
            
        elif self.subclass == '2':
            self.cha += 1
            self.traits['Fearless'] = 'When you are frightened, you can take an action to end the frightening effect on yourself.'

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
                       "Speed": 30,
                       "Languages":"Common"
                                               
                       }
         
    

        self.abilityScoreAdjustment()

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

