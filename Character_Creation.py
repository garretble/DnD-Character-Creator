### Character information up to date for DnD Next version 4/11/13 ###

import random as r

print "~~~~ Welome to DnD Next Simple Character Creator ~~~~"
print
print "This program will help you create a character quickly " \
      "to the point where you will need to begin choosing " \
      "choosing armor, items, skills, etc."
print
print "To create a character, simply create a race instance and follow " \
      "the directions."
print "To do so, type: CharacterName = Race(Level,Name)"
print "For example: Tim = Dwarf(4,'Tim')"
print "Note: leaving the arguments blank (e.g. Dwarf() ) will default to Level 1"\
      " with a random name."
print
print "Races are: Dwarf, Elf, Halfling, Human"






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

#Default names if no name is given when creating character
randomNames = {"Dwarf":['Adrik', 'Alberich', 'Baer', 'Barendd', 'Brottor',
                        'Dain', 'Darrak', 'Eberk', 'Einkil', 'Fargrim',
                        'Gardain', 'Harbek', 'Kildrak', 'Morgran', 'Orsik',
                        'Oskar', 'Rangrim', 'Rurik', 'Taklinn', 'Thoradin',
                        'Thorin', 'Tordek', 'Traubon', 'Travok', 'Ulfgar', 'Veit',
                        'Vondal'],
               "Elf":['Adran', 'Aelar', 'Aramil', 'Arannis', 'Aust', 'Beiro',
                      'Berrian', 'Carric', 'Enialis', 'Erdan', 'Erevan', 'Galinndan',
                      'Hadarai', 'Heian', 'Himo', 'Immeral', 'Ivellios', 'Laucian',
                      'Mindartis', 'Paelias', 'Peren', 'Quarion', 'Riardon', 'Rolen',
                      'Soveliss', 'Thamior', 'Tharivol', 'Theren', 'Varis'],
               "Halfling":['Alton', 'Ander', 'Cade', 'Corrin', 'Eldon', 'Errich',
                           'Finnan', 'Garret', 'Lindal', 'Lyle', 'Merric', 'Milo',
                           'Osborn', 'Perrin', 'Reed', 'Roscoe', 'Wellby'],
               "Human":['Alton', 'Ander', 'Cade', 'Corrin', 'Eldon', 'Errich',
                           'Finnan', 'Garret', 'Lindal', 'Lyle', 'Merric', 'Milo',
                           'Osborn', 'Perrin', 'Reed', 'Roscoe', 'Wellby','Adran', 'Aelar', 'Aramil', 'Arannis', 'Aust', 'Beiro',
                      'Berrian', 'Carric', 'Enialis', 'Erdan', 'Erevan', 'Galinndan',
                      'Hadarai', 'Heian', 'Himo', 'Immeral', 'Ivellios', 'Laucian',
                      'Mindartis', 'Paelias', 'Peren', 'Quarion', 'Riardon', 'Rolen',
                      'Soveliss', 'Thamior', 'Tharivol', 'Theren', 'Varis','Adrik', 'Alberich', 'Baer', 'Barendd', 'Brottor',
                        'Dain', 'Darrak', 'Eberk', 'Einkil', 'Fargrim',
                        'Gardain', 'Harbek', 'Kildrak', 'Morgran', 'Orsik',
                        'Oskar', 'Rangrim', 'Rurik', 'Taklinn', 'Thoradin',
                        'Thorin', 'Tordek', 'Traubon', 'Travok', 'Ulfgar', 'Veit',
                        'Vondal']}

#global list of skills
skills = {'administer first aid': 'wis',
                  'balance':'dex',
                  'bluff':'cha',
                  'break an object':'str',
                  'climb':'str',
                  'conceal an object':'dex',
                  'drive':'dex',
                  'gather rumors':'cha',
                  'handle an animal':'wis',
                  'intimidate':'cha',
                  'jump':'str',
                  'listen':'wis',
                  'perform':'cha',
                  'persuade':'cha',
                  'recall lore':'int',
                  'ride':'dex',
                  'search':'int',
                  'sense motive':'wis',
                  'sneak':'dex',
                  'spot':'wis',
                  'swim':'str',
                  'tumble':'dex'}

            

        
    
class Character(object):

    def __init__(self,level):
        
        self.level = level
        print "You can use randomized ability scores: "+str(abilityScores())
        print "Or simply use the standard array:      [8, 10, 12, 13, 14, 15]"
        print
        self.str = int(raw_input("Please enter STRENGTH value: "))
        self.dex = int(raw_input("Please enter DEXTERITY value: "))
        self.con = int(raw_input("Please enter CONSTITUTION value: "))
        self.int = int(raw_input("Please enter INTELLIGENCE value: "))
        self.wis = int(raw_input("Please enter WISDOM value: "))
        self.cha = int(raw_input("Please enter CHARISMA value: "))
        self.hp = 0
        self.classType = ''
        self.background = ''
        self.backgroundStory = ''
        self.backgroundProfession = ''
        self.skills = ''
        print

        #classMods for updating hp and other stats when leveling up, as determined by traits
        #or class specific characteristics
        #The list represents [str,dex,con,int,wis,cha,hp]
        self.classMods = [0,0,0,0,0,0,0]

        #Experience calculator
        xp_dict = {1: 0, 2: 250, 3: 950, 4: 2250, 5:4750,
                   6: 9500, 7:16000, 8:25000, 9: 38000, 10: 56000,
                   11: 77000, 12: 96000, 13: 120000, 14: 150000, 15: 190000,
                   16: 230000, 17: 280000, 18: 330000, 19: 390000, 20: 460000}
        self.xp = xp_dict[self.level]

        self.hit_dice = {"Barbarian": "d12",
                    "Cleric": "d8",
                    "Druid":"d8",
                    "Fighter":"d10",
                    "Monk":"d8",
                    "Paladin":"d10",
                    "Ranger":"d10",
                    "Rogue":"d6",
                    "Wizard":"d6"}
        
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
        
                
    def abilityScores(self):
        """
        Function used in save() method to return Ability Scores
        """
        mods = [(self.str -10)/2,
                (self.dex-10)/2,
                (self.con-10)/2,
                (self.int-10)/2,
                (self.wis-10)/2,
                (self.cha-10)/2]
        return "STR: {0} ({1}) \nDEX: {2} ({3})\nCON: {4} ({5})".format(self.str,
                                                                       mods[0],
                                                                       self.dex,
                                                                       mods[1],
                                                                       self.con,
                                                                       mods[2])+"\n" \
                "INT: {0} ({1})\nWIS: {2} ({3})\nCHA: {4} ({5})".format(self.int,
                                                                      mods[3],
                                                                      self.wis,
                                                                      mods[4],
                                                                      self.cha,
                                                                      mods[5])
        

    def updateScore(self,ability,amount):
        """ (str,int) -> Nonetype
        Use to update an ability score manually.
        """
        abilities = {'str':'strength','dex':'dexterity',
                     'con':'constitution','int':'intelligence',
                     'wis':'wisdom','cha':'charisma',
                     'hp':'hit points'}
        if ability == 'str':
            self.str += amount
            print "You added {0} point(s) to the {1} stat.".format(amount,abilities[ability])
        elif ability == 'dex':
            self.dex += amount
            print "You added {0} point(s) to the {1} stat.".format(amount,abilities[ability])
        elif ability == 'con':
            self.con += amount
            print "You added {0} point(s) to the {1} stat.".format(amount,abilities[ability])
        elif ability == 'int':
            self.int += amount
            print "You added {0} point(s) to the {1} stat.".format(amount,abilities[ability])
        elif ability == 'wis':
            self.wis += amount
            print "You added {0} point(s) to the {1} stat.".format(amount,abilities[ability])
        elif ability == 'cha':
            self.cha += amount
            print "You added {0} point(s) to the {1} stat.".format(amount,abilities[ability])
        elif ability == 'hp':
            self.hp += amount
            print "You added {0} point(s) to the {1} stat.".format(amount,abilities[ability])
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
        elif ability == 'hp':
            self.hp += amount

    def chooseClass(self):
        """
        Asks player to choose a class for his/her character. Called in each character class.
        """

        #Ask which class he/she would like
        chosen_class = raw_input("Which class would you like? Please choose from:\nBarbarian, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Wizard " ).lower() 
        while chosen_class not in ['barbarian','cleric','druid','fighter','monk','paladin','ranger','rogue','wizard']:
            chosen_class = raw_input("\nIncorrect input\n\nWhich class would you like? Please choose from:\nBarbarian, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Wizard " ).lower()           
        print

        #Adds character class to Class object for use in print statements
        self.classType = chosen_class.title()
        
        #Dictionary of classes with 0 values in a list (ex. [str,dex,con,int,wis,cha,hp])
        classes = {'barbarian': [0,0,0,0,0,0,self.con+12],
                   'cleric':[0,0,0,0,0,0,self.con+8],
                   'druid':[0,0,0,0,0,0,self.con+8],
                   'fighter':[0,0,0,0,0,0,self.con+10],
                   'monk':[0,0,0,0,0,0,self.con+8],
                   'paladin':[0,0,0,0,0,0,self.con+10],
                   'ranger':[0,0,0,0,0,0,self.con+10],
                   'rogue':[0,0,0,0,0,0,self.con+6],
                   'wizard':[0,0,0,0,0,0,self.con+6]
                   }

        #Class specific conditional statements. These update the various ability scores
        #in the classes variable
        if chosen_class == 'barbarian':
            barb_choice = raw_input('Would you like to boost (1) Strength or (2) Constitution? ')
            print
            while barb_choice not in ['1','2']:
                barb_choice = raw_input('Would you like to boost (1) Strength or (2) Constitution? ')
                print
            if barb_choice == '1':
                classes['barbarian'][0] = 1
            elif barb_choice == '2':
                classes['barbarian'][2] = 1
        elif chosen_class == 'cleric':
            clerc_choice = raw_input('Would you like to boost (1) Wisdom, (2) Strength, or (3) Constitution? ')
            print
            while clerc_choice not in ['1','2','3']:
                clerc_choice = raw_input('Would you like to boost (1) Wisdom, (2) Strength, or (3) Constitution? ')
                print
            if clerc_choice == '1':
                classes['cleric'][4] = 1
            elif clerc_choice == '2':
                classes['cleric'][0] = 1
            elif clerc_choice == '3':
                classes['cleric'][2] = 1
        elif chosen_class == 'druid':
            druid_choice = raw_input('Would you like to boost (1) Wisdom or (2) Constitution? ')
            print
            while druid_choice not in ['1','2']:
                druid_choice = raw_input('Would you like to boost (1) Wisdom or (2) Constitution? ')
                print
            if druid_choice == '1':
                classes['druid'][4] = 1
            elif druid_choice == '2':
                classes['druid'][2] = 1
        elif chosen_class == 'fighter':
            fight_choice = raw_input('Would you like to boost (1) Strength, (2) Dexterity, or (3) Constitution? ')
            print
            while fight_choice not in ['1','2','3']:
                fight_choice = raw_input('Would you like to boost (1) Strength, (2) Dexterity, or (3) Constitution? ')
                print
            if fight_choice == '1':
                classes['fighter'][0] = 1
            elif fight_choice == '2':
                classes['fighter'][1] = 1
            elif fight_choice == '3':
                classes['fighter'][2] = 1            
        elif chosen_class == 'monk':
            monk_choice = raw_input("Would you like to boost (1) Wisdom or (2) Dexterity? ")
            print
            while monk_choice not in ['1','2']:
                monk_choice = raw_input("Would you like to boost (1) Wisdom or (2) Dexterity? ")
                print
            if monk_choice == '1':
                classes['monk'][4] = 1
            elif monk_choice == '2':
                classes['monk'][1] = 1
        elif chosen_class == 'paladin':
            pal_choice = raw_input('Would you like to boost (1) Strength, (2) Constitution, or (3) Charisma? ')
            print
            while pal_choice not in ['1','2','3']:
                pal_choice = raw_input('Would you like to boost (1) Strength, (2) Constitution, or (3) Charisma? ')
                print
            if pal_choice == '1':
                classes['paladin'][0] = 1
            elif pal_choice == '2':
                classes['paladin'][2] = 1
            elif pal_choice == '3':
                classes['paladin'][5] = 1
        elif chosen_class == 'ranger':
            rang_choice = raw_input('Would you like to boost (1) Strength, (2) Dexterity, or (3) Constitution? ')
            print
            while rang_choice not in ['1','2','3']:
                rang_choice = raw_input('Would you like to boost (1) Strength, (2) Dexterity, or (3) Constitution? ')
                print
            if rang_choice == '1':
                classes['ranger'][0] = 1
            elif rang_choice == '2':
                classes['ranger'][1] = 1
            elif rang_choice == '3':
                classes['ranger'][2] = 1
        elif chosen_class == 'rogue':
            rog_choice = raw_input('Would you like to boost (1) Strength, (2) Dexterity, or (3) Intelligence? ')
            print
            while rog_choice not in ['1','2','3']:
                rog_choice = raw_input('Would you like to boost (1) Strength, (2) Dexterity, or (3) Intelligence? ')
                print
            if rog_choice == '1':
                classes['rogue'][0] = 1
            elif rog_choice == '2':
                classes['rogue'][1] = 1
            elif rog_choice == '3':
                classes['rogue'][3] = 1
        elif chosen_class == 'wizard':
            wiz_choice = raw_input('Would you like to boost (1) Intelligence or (2) Constitution? ')
            print
            while wiz_choice not in ['1','2']:
                wiz_choice = raw_input('Would you like to boost (1) Intelligence or (2) Constitution? ')
                print
            if wiz_choice == '1':
                classes['wizard'][3] = 1
            elif wiz_choice == '2':
                classes['wizard'][2] = 1
        
        #Update base stats

        #A basic list full of the types of ability scores
        stats_list = ['str','dex','con','int','wis','cha','hp']
        #loops through the stats_list and adds all numbers to character's
        #starting stats
        for i in range(len(stats_list)):
            self.stealthUpdate(stats_list[i],classes[chosen_class][i])
            

        #modify hp if character is starting out higher than level 1
        def update_hp_for_higher_level(chosen_class,level):
            """
            Helper function for chooseClass(). Updates character for
            levels greater than 1.
            """
            #Checks to see if your character is level 4,8,12,etc.
            def upgradedAbilityAt4(level):
                if level % 4 == 0:
                    upgraded_ability = raw_input("Level "+str(level)+"!\n  Which two abilities would you like to upgrade? (Adds +1 to ability)\n  Please input two from str/dex/con/int/wis/cha with a space in between.\n  (ex: cha dex) ").split(' ')
                    print
                    #To write:
                    #if either ability pushes ability score over 20, redo input

                    
                    for i in upgraded_ability:
                        self.stealthUpdate(i,1)
            #class specific HP calculations
            if chosen_class == 'barbarian':                
                for i in range(2,self.level+1):
                    upgradedAbilityAt4(i)
                    self.hp += r.randint(1,12) + self.con + self.classMods[6]
            elif chosen_class == 'cleric':
                for i in range(2,self.level+1):
                    upgradedAbilityAt4(i)
                    self.hp += r.randint(1,8) + self.con + self.classMods[6]
            elif chosen_class == 'druid':
                for i in range(2,self.level+1):
                    upgradedAbilityAt4(i)
                    self.hp += r.randint(1,8) + self.con + self.classMods[6]
            elif chosen_class == 'fighter':
                for i in range(2,self.level+1):
                    upgradedAbilityAt4(i)
                    self.hp += r.randint(1,10) + self.con + self.classMods[6]
            elif chosen_class == 'monk':
                for i in range(2,self.level+1):
                    upgradedAbilityAt4(i)
                    self.hp += r.randint(1,8) + self.con + self.classMods[6]
            elif chosen_class == 'paladin':
                for i in range(2,self.level+1):
                    upgradedAbilityAt4(i)
                    self.hp += r.randint(1,10) + self.con + self.classMods[6]
            elif chosen_class == 'ranger':
                for i in range(2,self.level+1):
                    upgradedAbilityAt4(i)
                    self.hp += r.randint(1,10) + self.con + self.classMods[6]
            elif chosen_class == 'rogue':
                for i in range(2,self.level+1):
                    upgradedAbilityAt4(i)
                    self.hp += r.randint(1,6) + self.con + self.classMods[6]
            elif chosen_class == 'wizard':
                for i in range(2,self.level+1):
                    upgradedAbilityAt4(i)
                    self.hp += r.randint(1,6) + self.con + self.classMods[6]
                    

        if self.level > 1:
            update_hp_for_higher_level(chosen_class,self.level)

    
    
    def backgroundAndSkills(self):
        """
        Helps user choose Background and Skills.
        """
        backgrounds = {}
        def createBackgrounds(fileName):
            """ (str) -> None
            Opens a file with background information and populates the backgrounds dictionary with
            that information
            """
            backgroundFile = open(fileName,'r')
            current_bg = ''
            for line in backgroundFile:
                #If there is no text, go to next line
                if line == "\n":
                    pass
                #Else if the line starts with "~~", create new key in top level
                #dictionary with the remainder of that line and set its value
                #to an empty dictionary
                elif line[:2] == "~~":
                    current_bg = line[2:-1]
                    backgrounds[line[2:-1]] = {}
                #Go through the next few lines and set them to keys and values
                #in the nestled dictionary
                elif ":" in line:
                    line_heading = line[:line.index(":")]
                    after_heading = line[line.index(":")+2:-1]
                    #create a key/value pair for the background regarding its profession
                    if line_heading == "hasProfession":
                        
                        #Change the string to a bool
                        if after_heading == "True":
                            backgrounds[current_bg][line_heading] = True
                        else:
                            backgrounds[current_bg][line_heading] = False
                    #Create professions list if current BG has professions
                    if line_heading == "professions" and backgrounds[current_bg]['hasProfession']:
                        backgrounds[current_bg]['professions'] = after_heading.split(', ')
                    #Create a two item list to store the trait name and its description
                    if line_heading == "trait":
                        backgrounds[current_bg]['trait'] = [line[line.index(":")+2: line.index("-")-1],\
                                                            line[line.index("-")+2:-1]]
                    #Create an entry for the story of a character's background
                    if line_heading == "story":
                        backgrounds[current_bg]['story'] = after_heading
                    #Create a list for the recommended skills
                    if line_heading == "recommended":
                        backgrounds[current_bg]['recommended'] = after_heading.split(', ')
            backgroundFile.close()
        createBackgrounds('Backgrounds.txt')

            
 
        
        #Make a list of backgrounds
        background_list = []
        for i in backgrounds:
            background_list.append(i)
        background_list.sort()
        #Ask user to choose a background and set that to self.background
        background_choice = raw_input('Enter a background from this list: '+str(background_list)+': ').title()
        print
        self.background = background_choice
        self.backgroundStory = backgrounds[self.background]['story']
        #Add the background's trait to self.traits
        self.traits[backgrounds[self.background]['trait'][0]] = backgrounds[self.background]['trait'][1]
        #If the background has a profession, add that now
        if backgrounds[self.background]['hasProfession'] == True:
            temp_choice = raw_input("Which profession would you like? "+str(backgrounds[self.background]['professions'])+"\n"\
                                    "Enter one from the list above or press Enter for random. ")
            print
            if temp_choice == '':
                temp_int = r.randint(0,len(backgrounds[self.background]['professions'])-1)
                self.backgroundProfession = backgrounds[self.background]['professions'][temp_int]
            else:
                self.backgroundProfession = temp_choice
        else:
            pass

        #Ask about skills.
        skill_choice = []
        print "You'll now choose 4 skills from this list:"
        print
        for i in skills:
            print i.title()
        print
        print "Recommended skills for your "+self.background+" are: "+str(backgrounds[self.background]['recommended'])
        for i in range(4):
            skill_choice.append(raw_input("Which Skill would you like for skill "+str(i+1)+"? ").title())
        self.skills = skill_choice
            
                               
        

    

    def createTraits(self,fileName,startLine,stopLine):
        """ (str,str,str) -> dict
        returns a dictionary of traits for character. Populates the self.traits
        variable for the character class.

        fileName: The file to open
        startLine: The function looks for this line before running; its usage
           here looks for "Traits:" before executing further
        stopLine: The place to stop; its usage here looks for line "Stop:" in
           the opened file. 
        """
        traits_file = open(fileName,'r')
        
        
        read_file = ''
        temp_dict = {}
        temp_line = ''
        while read_file[:-2].lower() != startLine.lower():
            read_file = traits_file.readline()
        
        for line in traits_file:
            if line == "\n":
                pass
            elif line[:-2] == stopLine or line[:-1] == stopLine:
                traits_file.close()
                return temp_dict            
            elif len(line) > 0 and ":" in line:
                temp_line = line[:line.index(":")]               
                temp_dict[line[:line.index(":")]] = ''
                
            elif len(line) > 0:
                if len(temp_dict) == 0:
                    pass
                else:
                    temp_dict[temp_line] = line[:-1]
                
                
    
    def save(self):
        """
        Saves a character to a .txt file in same directory as this file.
        """
        
        fileName=self.characterName+"_"+self.race+"_"+self.classType+"_lvl_"+str(self.level)
        new_file = open(str(fileName)+".txt","w")
        new_file.write("~~~~~~~~~~~ "+self.characterName+" the "+self.race+" "+self.classType+" ~~~~~~~~~~~\n\n")
        new_file.write("Level: "+str(self.level)+"   HP: "+str(self.hp)+"    XP: "+str(self.xp)+"    Hit Dice: "+str(self.level)+str(self.hit_dice[self.classType])+"\n")
        new_file.write(str(self.abilityScores()))
        new_file.write("\n\n~~~~~~~~~ Skills ~~~~~~~~~\n")
        for i in self.skills:
            new_file.write("\n"+i+" "+"("+skills[i.lower()].upper()+")")
        new_file.write("\n\n~~~~~~~~~ Traits ~~~~~~~~~\n")
        for i in self.traits:
            new_file.write("\n  ~~"+i+"~~\n    "+str(self.traits[i])+"\n")
        new_file.write("\n\n~~~~~~~~~ Background: "+self.background+" ~~~~~~~~\n")
        if self.backgroundProfession == '':
            pass
        else:
            new_file.write("Profession: "+self.backgroundProfession)
        new_file.write("\n  "+self.backgroundStory)
        
        new_file.close()
        print "File "+str(fileName)+".txt saved."        
        
            
    def __str__(self):
        print
        print "~~~~~~~~~~~~~~~~ "+self.characterName+" the "+self.race+" "+self.classType+" ~~~~~~~~~~~~~~~~"
        print
        print "Level: "+str(self.level)+"   HP: "+str(self.hp)+"    XP: "+str(self.xp)+"    Hit Dice: "+str(self.level)+str(self.hit_dice[self.classType])
        self.getAbilityScores()
        print
        print "~~~~~~~~~ Skills ~~~~~~~~~ "
        print
        for i in self.skills:
            print i+" "+"("+skills[i.lower()].upper()+")"
        print
        print "~~~~~~~~~ Traits ~~~~~~~~~ "
        for i in self.traits:
            print
            print "  ~~"+i+"~~"
            print"    "+str(self.traits[i])
        print
        print "~~~~~~~~~ Background: "+self.background+" ~~~~~~~~"
        if self.backgroundProfession == '':
            pass
        else:
            print "Profession: "+self.backgroundProfession
        print
        print "  "+self.backgroundStory
        return "End of "+self.race
    
        
        
class Dwarf(Character):

    def __init__(self,level=1,characterName=randomNames["Dwarf"][r.randint(0,len(randomNames["Dwarf"])-1)]):

        Character.__init__(self,level)
        self.characterName = characterName
        self.race = "Dwarf"
        
        
        
        self.subrace = raw_input("Are you a (1) Hill Dwarf or (2) Mountain Dwarf? (input number) ")
        print
        while self.subrace not in ['1','2']:
            self.subrace = raw_input("Are you a (1) Hill Dwarf or (2) Mountain Dwarf? (input number) ")
            print            
        self.traits = self.createTraits('Races/Dwarf_Traits.txt','Traits','Stop')

        
        
        #if Hill Dwarf
        if self.subrace == '1':
            self.str += 1
            self.traits['Dwarven Toughness'] = 'Your hit point maximum increases by 1 and it increases by 1 every time you gain a level. Additionally, whenever you roll Hit Dice during a rest, you regain 1 extra hit point for each Hit Die you roll.'
            self.traits['Subrace'] = "Hill Dwarf"
            self.hp += 1
            self.classMods[6] += 1
        #if Mountain Dwarf
        elif self.subrace == '2':
            self.wis += 1
            self.traits['Armor Mastery'] = 'You are proficient with light and medium armor. While wearing medium or heavy armor, you gain a +1 bonus to Armor Class.'
            self.traits['Subrace'] = 'Mountain Dwarf'
        #Choose a class
        self.chooseClass()
        self.backgroundAndSkills()

        print self.__str__()
  

class Elf(Character):

    def __init__(self,level=1,characterName=randomNames["Elf"][r.randint(0,len(randomNames["Elf"])-1)]):

        Character.__init__(self,level)
        self.characterName = characterName
        self.race = "Elf"
        
        self.subrace = raw_input("Are you a (1) High Elf or (2) Wood Elf? (input number) ")
        print
        while self.subrace not in ['1','2']:
            self.subrace = raw_input("Are you a (1) High Elf or (2) Wood Elf? (input number) ")
            print
        self.traits = self.createTraits('Races/Elf_Traits.txt','Traits','Stop')

        
        
        #Added dex due to trait
        self.dex += 1

        #if High Elf
        if self.subrace == '1':
            self.int += 1
            self.traits['Extra Language'] = "You can speak, read, and write one extra language of your choice."
            self.traits['Cantrip'] = "You know one cantrip of your choice from the wizard's cantrip list. Intelligence is your magic ability for it."
            self.traits['Subrace'] = 'High Elf'
        #if Wood Elf    
        elif self.subrace == '2':
            self.wis += 1
            self.traits['Speed'] = "35 Feet"
            self.traits['Fleet of Foot'] = "Your speed increases by 5 feet. (Already calculated)"
            self.traits['Mask of the Wild'] = 'You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.'
            self.traits['Subrace'] = "Wood Elf"
        #Choose a class
        self.chooseClass()
        self.backgroundAndSkills()

        print self.__str__()
        
    

class Halfling(Character):

    def __init__(self,level=1,characterName=randomNames["Halfling"][r.randint(0,len(randomNames["Halfling"])-1)]):

        Character.__init__(self,level)
        self.characterName = characterName
        self.race = "Halfling"
        
        self.subrace = raw_input("Are you (1) Lightfoot or (2) Stout? (input number) ")
        print
        while self.subrace not in ['1','2']:
            self.subrace = raw_input("Are you a (1) Lightfoot or (2) Stout? (input number) ")
            print
        
        self.traits = self.createTraits('Races/Halfling_Traits.txt','Traits','Stop')

        #Added dex due to trait
        self.dex += 1

        #if Lightfoot
        if self.subrace == '1':
            self.cha += 1
            self.traits['Naturally Stealthy'] = "You can attempt to hide even when you are obscurred only by a creature that is one size category larger than you."
            self.traits['Subrace'] = 'Lightfoot'
        #if Stout
        elif self.subrace == '2':
            self.con += 1
            self.traits['Stout Resilience'] = 'You have advantage on saving throws against poison, and you have resistance against poison damage.'
            self.traits['Subrace'] = 'Stout'

        #Choose a class
        self.chooseClass()
        self.backgroundAndSkills()

        print self.__str__()
        
    

class Human(Character):
    ''' Input Level or leave blank for Level 1 '''
    def __init__(self,level=1,characterName=randomNames["Human"][r.randint(0,len(randomNames["Human"])-1)]):

        Character.__init__(self,level)
        self.characterName = characterName
        self.race = "Human"
        
        self.traits = self.createTraits('Races/Human_Traits.txt','Traits','Stop')
        
        
        #A list of abilities 
        abilities_list = ['str','dex','con','int','wis','cha']
        #Add 1 to each ability score as guided by trait
        for i in abilities_list:
            self.stealthUpdate(i,1)

        #Choose a class
        self.chooseClass()
        self.backgroundAndSkills()

        print self.__str__()
        
    
        
    

