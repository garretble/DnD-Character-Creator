DnD-Character-Creator
=====================

A simple character creator for DnD Next (Work in Progress)

This program will make a simple character and give you stats and traits for the character.
From there, you will need to select your gear and skills and add up your AC score.


Some helpful methods you can use when making a character:

"character" in these examples means your character's name that you created at the beginning.
For example, to check the Dwarf Narlbuck's ability scores, you'd type: Narlbuck.getAbilityScores()


character.getAbilityScores()
--------------------------------
This will print out a list of all your ability scores for your character.

character.updateScore(ability, amount)
--------------------------------
Allows you to update ability's for your character. 
The "ability" argument is a string (ex. 'str') that tells the method which ability to modify,
and "amount" is by how much. You can use negative values here.


