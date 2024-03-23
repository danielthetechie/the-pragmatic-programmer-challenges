"""
Design a BNF grammar to parse a time specification. All of the
following examples should be accepted:
4pm, 7:38pm, 23:42, 3:16, 3:16am
"""

# Accepts the following formats: 4pm, 7:38pm, 23:42, 3:16, 3:16am
def getMinsAndHoursFromTimeSpec (time_spec):
	hours = None
	minutes = None

	#Parse the 4pm case
	if len (time_spec) == 3:
		if time_spec[1:] == "am" or time_spec[2:] == "pm":
			hours = time_spec[0]
			minutes = 0

	return { "hours": hours, "minutes": minutes }
	

def output_bnf_grammar (hours, minutes):
	print ("<time> ::= <hours> : <minutes>")
	print ("<hours> ::= \"" + str (hours) + "\"")
	print ("<minutes> ::= \"" + str (minutes) + "\"")

def parseTime (time_spec):
	time = getMinsAndHoursFromTimeSpec (time_spec)
	output_bnf_grammar (time["hours"], time["minutes"])

time1 = "4pm"
parseTime (time1)