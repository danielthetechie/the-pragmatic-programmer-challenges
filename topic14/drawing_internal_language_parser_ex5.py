"""
In the previous exercise we implemented a parser for the
drawing language—it was an external domain language. Now
implement it again as an internal language. Don’t do anything
clever: just write a function for each of the commands. You may
have to change the names of the commands to lower case, and
maybe to wrap them inside something to provide some context.
"""

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

	def getPossibleErrorCodeFromUserParameter (parameter = None):
		if (parameter is None):
			return 1
		elif (type (parameter) != int):
			return 3
		else:
			return None

	def select_pen (pen_number):
		error_code_intent = getPossibleErrorCodeFromUserParameter (pen_number)
		if error_code is None:
			return ("Select pen " + str (pen_number))
		else:
			return error_code

	def draw_north (units):
		error_code_intent = getPossibleErrorCodeFromUserParameter (units)
		if error_code is None:
			return ("Draw north " + str (units) + " units")
		else:
			return error_code

	def draw_south (units):
		error_code_intent = getPossibleErrorCodeFromUserParameter (units)
		if error_code is None:
			return ("Draw south " + str (units) + " units")
		else:
			return error_code

	def draw_west (units):
		error_code_intent = getPossibleErrorCodeFromUserParameter (units)
		if error_code is None:
			return ("Draw west " + str (units) + " units")
		else:
			return error_code

	def draw_east (units):
		error_code_intent = getPossibleErrorCodeFromUserParameter (units)
		if error_code is None:
			return ("Draw east " + str (units) + " units")
		else:
			return error_code

	def pen_up (*args):
		return "Pen up "

	def pen_down (*args):
		return "Pen down"

	def getErrorMessageByCode (self, int_code, command = None):
		error_codes = {
			1: "Error: " + command + " requires an integer parameter.",
			2: "Error: Unknown command (" + command + ").",
			3: "Error: the parameter must be an integer."
		}

		return error_codes[int_code]

	"""
	def getActionByCommand (self, command, int_parameter = None):
		if command in self.actions:
			self.actions[command]

			if (command in self.requires_int_parameter) and int_parameter:
				action += " " + str (int_parameter)

			elif (command in self.requires_int_parameter) and type (int_parameter) != int:
				return 1

			return action
		else:
			return 2

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

			intent = self.getActionByCommand (command_verb, command_int_parameter)

			if type (intent) == int:
				return self.getErrorMessageByCodeAndCommand (intent, command_verb)

			if len (translated_actions) > 0 and ("draw" in translated_actions[i - 1] or "then" in translated_actions[i - 1]):
				current_action = self.getActionByCommand (command_verb, command_int_parameter).replace ("draw", "then")
			else:
				current_action = self.getActionByCommand (command_verb, command_int_parameter)

			translated_actions.append (current_action)
		
		for action in translated_actions:
			result += action + "\n"

		return result[:-1]
	"""