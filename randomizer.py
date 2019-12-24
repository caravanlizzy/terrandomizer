import random

class Faction:
	def __init__(self, name, color):
		self.name = name
		self.color = color
		
	def setVariableColor(self, color):
		self.color = color


class Randomizer:	
	colorPool = ['red', 'green', 'gray', 'blue', 'black', 'brown', 'yellow']
	factions = [Faction('giants', 'red'), Faction('chaosmagicians', 'red'),
			Faction('engineers', 'grey'), Faction('dwarves', 'red'), 
			Faction('witches', 'green'), Faction('auren', 'green'),
			Faction('mermaids', 'blue'), Faction('swarmlings', 'blue'), 
			Faction('alchemists', 'black'), Faction('darklings', 'black'), 
			Faction('cultists', 'brown'), Faction('halflings', 'brown'),
			Faction('nomads', 'yellow'), Faction('fakirs', 'yellow'), 
			Faction('shapeshifters', 'variable'), Faction('riverwalkers', 'variable'), 
			Faction('acolytes', 'variable'), Faction('dragonlords', 'variable'),
			Faction('icemaidens', 'variable'), Faction('yetis', 'variable')]
	def __init__(self):
		self.maps = ['Original', 'Original balanced VP 2017', 'Fire and Ice side 1', 'Fire and Ice side 2', 'Loon Lakes', 'Fjords']
		self.playerCount = 0
		self.finalFactions = []
		self.finalMap = ''
		self.includeExpansion = False


	def drawFaction(self):
		newFaction = random.choice(self.factions)
		if newFaction.color == 'variable':
			self.setVariableColor(newFaction)
		return newFaction
	
	def findValidFaction(self):
		newFaction = self.drawFaction()
		while self.isColorOccupied(newFaction.color):
			newFaction = self.drawFaction()
		self.finalFactions.append(newFaction)
		self.factions.remove(newFaction)
		self.colorPool.remove(newFaction.color)
		# ~ return newFaction
		
		
	def isColorOccupied(self, color):
		for y in self.colorPool:
			if color == y:
				return False
		return True
		
	def setVariableColor(self, faction):
		newColor = random.choice(self.colorPool)
		faction.setVariableColor(newColor)


	def askPlayerCount(self):
		self.playerCount = int(input('How many players to participate?\n'))
		if self.playerCount > 7:
			self.playerCount = 7
			print('Cannot take more than 7 players! Assume 7 players.\n')
		elif self.playerCount < 1:
			self.playerCount = 1
			print('Cannot take less than 1 player! Assume 1 player.\n')
	
	def askExpansion(self):
		include = 'yes'
		newInclude = input('Do you want to include the expansion factions?')
		if len(newInclude) > 0:
			include = newInclude
		if include.lower()[0] == 'n':
			self.excludeExpansion()
		
		
	def printResults(self):
		print('\nRESULT\n')
		print('Map - '+ self.finalMap + ' \n')
		for i in range(self.playerCount):
			print('Player ' + str(i+1) + ' : ' + self.finalFactions[i].name + ' ' + self.finalFactions[i].color +'\n')
	
	def excludeExpansion(self):
		for i in range(6):
			self.factions.pop(-1)
	
	def run(self):
		self.askPlayerCount()
		self.askExpansion()
		self.finalMap = random.choice(self.maps)
		for i in range(self.playerCount):
			self.findValidFaction()
	

r = Randomizer()
r.run()
r.printResults()
