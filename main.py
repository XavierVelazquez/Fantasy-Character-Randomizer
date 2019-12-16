import random

name = input("Name:\n")

abilityScore = []

def rolling(): # Rolls 4d6 and removes lowest one
  abilityScoreDie1 = random.randint(1,6)
  abilityScoreDie2 = random.randint(1,6)
  abilityScoreDie3 = random.randint(1,6)
  abilityScoreDie4 = random.randint(1,6)
  scores = [abilityScoreDie1, abilityScoreDie2, abilityScoreDie3, abilityScoreDie4]
  scores.sort()
  scores.pop(0)
  scoreFinal = scores[0] + scores[1] + scores[2]
  abilityScore.append(scoreFinal)
rolling()
rolling()
rolling()
rolling()
rolling()
rolling()
abilityScore.sort()

races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-elf", "Half-orc", "Halfling", "Human", "Tiefling"]
raceSelect = random.randint(0,8)

characterClass = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
classSelect = random.randint(0,11)

background = ["Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero", "Guild Artisan", "Hermit", "Noble", "Outlander", "Sage", "Sailor", "Soldier", "Urchin"]
backgroundSelect = random.randint(0,12)

alignment = ["Chaotic Evil", "Chaotic Neutral", "Chaotic Good", "Lawful Evil", "Lawful Neutral", "Lawful Good", "Neutral", "Neutral Good", "Neutral Evil"]
alignmentSelect = random.randint(0,8)

print ("-----------------------------")
print ("|  " + name)
print ("-----------------------------")
print ("|  " + races[raceSelect] + " " + characterClass[classSelect])
print ("|  " + alignment[alignmentSelect])
print ("|  " + background[backgroundSelect])
print ("-----------------------------")
print (abilityScore)