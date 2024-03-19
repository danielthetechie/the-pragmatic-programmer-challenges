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
# associated to the letter they follow.

import re

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

		self.requires_int_parameter = ['P', 'N', 'S', 'W', 'E']

	def getActionByCommand (self, command, int_parameter = None):
		if command in self.actions:
			action = self.actions[command]
			if (command in self.requires_int_parameter) and int_parameter:
				action += " " + str (int_parameter)
			return action
		else:
			return "Unknown command"

	def parseUserCommands (self, commands_list):
		commands_list = commands_list.split (" ")
		command_verb = None
		command_int_parameter = None
		translated_actions = []
		current_action = ""
		result = ""

		for i in range (0, len (commands_list)):
			command_verb = "".join (re.findall (r'[A-Za-z]', commands_list[i]))
			command_int_parameter = "".join (re.findall (r'\d', commands_list[i]))

			if len (translated_actions) > 0 and ("draw" in translated_actions[i - 1] or "then" in translated_actions[i - 1]):
				current_action = self.getActionByCommand (command_verb, command_int_parameter).replace ("draw", "then")
			else:
				current_action = self.getActionByCommand (command_verb, command_int_parameter)

			translated_actions.append (current_action)
		
		for action in translated_actions:
			result += action + "\n"

		return result[:-1]

	def addNewCommand (self, command, action, requires_int_parameter = False):
		if command in self.actions:
			print ("This command already exists and it means '" + action + "'")
		else:
			self.actions[command] = action
			if requires_int_parameter:
				self.requires_int_parameter.append (command)

cml = CustomMiniLanguage ()

commands_list = "P2 D W2 N1 E2 S1 U"
print (cml.parseUserCommands (commands_list))

#commands_list = input ("Enter commands: ")

"""
cml.addNewCommand ("C", "cancel")
print (cml.getActionByCommand ("C"))
cml.addNewCommand ("P", "paint")
"""