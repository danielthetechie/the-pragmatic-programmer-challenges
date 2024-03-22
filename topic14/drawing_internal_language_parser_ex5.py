"""
In the previous exercise we implemented a parser for the
drawing language—it was an external domain language. Now
implement it again as an internal language. Don’t do anything
clever: just write a function for each of the commands. You may
have to change the names of the commands to lower case, and
maybe to wrap them inside something to provide some context.
"""

import re

class ParserToInternalLanguage ():
	def __init__ (self):
		self.actions = {
			'P': self.select_pen,
			
			'N': self.draw_north,
			'S': self.draw_south,
			'W': self.draw_west,
			'E': self.draw_east,

			'U': self.pen_up,
			'D': self.pen_down
		}

		self.requires_int_parameter = ['P', 'N', 'S', 'W', 'E']

	def getErrorMessageByCode (self, int_code, command = None):
		error_codes = {
			1: "Error: " + command + " requires an integer parameter.",
			2: "Error: Unknown command (" + command + ")."
		}

		return error_codes[int_code]

	def getPossibleErrorCodeFromUserCommand (self, command, parameter = None):
		if command not in self.actions:
			return 2
		if command not in self.requires_int_parameter:
			return None
		if (parameter is None or len (parameter) == 0):
			return 1

		return None

	def select_pen (self, pen_number):
		return "Select pen " + str (pen_number)

	def draw_north (self, units):
		return "Draw north " + str (units) + " units"

	def draw_south (self, units):
		return "Draw south " + str (units) + " units"

	def draw_west (self, units):
		return "Draw west " + str (units) + " units"

	def draw_east (self, units):
		return "Draw east " + str (units) + " units"

	def pen_up (self, *args):
		return "Pen up "

	def pen_down (self, *args):
		return "Pen down"

	
	def getActionByCommand (self, command):
		command_verb = "".join (re.findall (r'[A-Za-z]', command))
		command_int_parameter = "".join (re.findall (r'\d', command))

		error_code_intent = self.getPossibleErrorCodeFromUserCommand (command_verb, command_int_parameter)

		if error_code_intent is not None:
			return self.getErrorMessageByCode (error_code_intent, command_verb)

		return self.actions[command_verb] (command_int_parameter)

	
	def parseUserCommands (self, commands_list):
		commands_list = commands_list.split (" ")
		result = ""

		for command in commands_list:
			result += self.getActionByCommand (command) + "\n"

		return result[:-1]
	

commands_list = "P2 D W2 N1 E2 S1 U"

pil = ParserToInternalLanguage ()
print (pil.parseUserCommands (commands_list))

"""
Output:

Select pen 2
Pen down
Draw west 2 units
Draw north 1 units
Draw east 2 units
Draw south 1 units
Pen up 
"""