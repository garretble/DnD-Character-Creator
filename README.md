DnD-Character-Creator
=====================

A simple character creator for DnD Next (Work in Progress, runs on Python 2.7)

This program will make a simple character and give you stats, traits, class, background, skills, and feats
for the character. From there, you will need to select your gear and add up your AC score and gold.


"character" in these examples means the variable where your charecter is stored
(I am just assuming you'd make this variable his/her name).

To create a character, type: character = race(level,name) where "character" is just a variable,
"race" is the race of your character (Dwarf,Elf,Halfling,Human), "level" is an integer 
signalling the starting level of your character, and "name" is string of the name you want for your character.

ex. Narlbuck = Dwarf(1,"Narlbuck")

Note: You can leave the arguments blank and your character and you're character will start at level 1 with a 
random name. 

ex. random_char = Elf() will give you an Elf at level 1 with a random elfy name.

Some helpful methods you can use when making a character:

character.getAbilityScores()
--------------------------------
This will print out a list of all your ability scores for your character.

character.updateScore(ability, amount)
--------------------------------
Allows you to update ability's for your character. 
The "ability" argument is a string (ex. 'str') that tells the method which ability to modify,
and "amount" is by how much. You can use negative values here.

character.save()
--------------------------------
Saves your character to a .txt file in the same directory where the Character Creator file
resides. The file will be your character's name, race, class, and level.

ex. Narlbuck.save() -> Narlbuck_Dwarf_Ranger_lvl_1.txt

print character
--------------------------------
Will print out a full description of your character.
