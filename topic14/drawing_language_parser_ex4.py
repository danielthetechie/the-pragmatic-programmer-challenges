"""
===============================================================
We want to implement a mini-language to control a simple
turtle-graphics system. The language consists of single-letter
commands, some followed by a single number. For example, the
following input would draw a rectangle:

P 2 # select pen 2
D # pen down
W 2 # draw west 2cm
N 1 # then north 1
E 2 # then east 2
S 1 # then back south
U # pen up

Implement the code that parses this language. It should be
designed so that it is simple to add new commands.
===============================================================
"""

# We assume that the commands input is SVG-like, that is, a string in which
# each command is separated by a space. If there are numbers, they are 
# associated to the last letter.

class CustomMiniLanguage ():
	def __init__ (self):
		self.actions = {
			'P': 'select pen',
			
			'N': 'draw north',
			'S': 'draw south',
			'W': 'draw west',
			'E': 'draw east',

			'U': 'pen up',
			'D': 'pen down'
		}

	def getActionByCommand (self, command):
		if command in self.actions:
			return self.actions[command]
		else:
			return ""

	def parseUserCommands (self, commands_list):
		commands_list = commands_list.split (" ")
		translated_actions = []
		result = ""
		for i in range (0, len (commands_list)):
			if len (translated_actions) > 0 and ("draw" in translated_actions[i - 1] or "then" in translated_actions[i - 1]):
				translated_actions.append (self.getActionByCommand (commands_list[i]).replace ("draw", "then"))
			else:
				translated_actions.append (self.getActionByCommand (commands_list[i]))
		
		for action in translated_actions:
			result += action + "\n"

		return result[:-1]

	def addNewCommand (self, command, action):
		if command in self.actions:
			print ("This command already exists and it means '" + action + "'")
		else:
			self.actions[command] = action

cml = CustomMiniLanguage ()

commands_list = "P D W N E S U"

print (cml.parseUserCommands (commands_list))

"""
cml.addNewCommand ("C", "cancel")
print (cml.getActionByCommand ("C"))
cml.addNewCommand ("P", "paint")
"""