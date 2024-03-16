"""
=====================================================================
1) Design a small address book database (name, phone number, and
so on) using a straightforward binary representation in your language 
of choice. Do this before reading the rest of this challenge.
=====================================================================
"""

CHAR_SIZE = 8 # In bits

# The algorithm idea is to map each character into an ASCII number
# and then convert it into binary.
def getBinaryRepresentationOfString (string):
	res = ""
	for c in string:
		c = ord (c) # Get the ASCI number of c
		c = str (bin (c)[2:]) # To remove the prefix '0b' returned by bin().

		# Since a char is 8 bits long, if the binary representation of c
		# is shorter than 8 bits, we need to fill the missing bits by 0s.

		missing_bits = CHAR_SIZE - len (c)
		c = ("0" * missing_bits) + c
		res += str (c)

	return res

class AddressBook ():
	def __init__ (self):
		self.entries = []

	def getAllEntries (self):
		res = ""
		for entry in self.entries:
			for key in entry:
				res += str (entry[key]) + "\t"
			res += "\n"
		return res[:-1] # To remove the last extra '\n'.

	def addEntryToAddressBook (self, entry):
		self.entries.append (entry)


address_book_db = AddressBook ()

address_book_db.addEntryToAddressBook ({ 'id': 1, 'name': 'John Doe', 'phone_number': '+14561234' })
address_book_db.addEntryToAddressBook ({ 'id': 2, 'name': 'Jin Kazama', 'phone_number': '+43910728' })
address_book_db.addEntryToAddressBook ({ 'id': 3, 'name': 'Son Goku', 'phone_number': '+43245001' })

binary_encoded_address_book = getBinaryRepresentationOfString (address_book_db.getAllEntries ())
#print (binary_encoded_address_book)

"""
Output:

0011000100001001010010100110111101101000011010000010000001000100011011110110010100001001001010
1100110001001101000011010100110110001100010011001000110011001101000000100100001010001100100000
1001010010100110100101101110001000000100101101100001011110100110000101101101011000010000100100
1010110011010000110011001110010011000100110000001101110011001000111000000010010000101000110011
0000100101010011011011110110111000100000010001110110111101101011011101010000100100101011001101
000011001100110010001101000011010100110000001100000011000100001001
"""

"""
===================================================================
2) Translate that format into a plain-text format using XML or JSON
===================================================================
"""

# The algorith consists on splitting the binary sequence into chunks
# of 8 bits, convert them to base-10 integers and then map their 
# ASCII decimal representation to their corresponding char.
def getStringRepresentationOfBinaryWord (binary_word):
	string_result = ""
	byte_word = ""
	bite_count = 0
	for b in binary_word:
		bite_count += 1
		byte_word += str (b)
		if (bite_count == CHAR_SIZE):
			ascii_dec_number = int ("0b" + byte_word, 2)
			string_result +=  chr (ascii_dec_number)
			byte_word = ""
			bite_count = 0
	return string_result

print ("")
print (getStringRepresentationOfBinaryWord (binary_encoded_address_book))

"""
Output: 

1	Johh Doe	+14561234	
2	Jin Kazama	+43910728	
3	Son Goku	+43245001
"""

# For convenience, I will assume that each row contains 
# all 'id', 'name' and 'phone_number' fields - they are all mandatory.
def getAddressBookJSONFromBinary (address_book_entries_binary_encoded):
	bin_asciiname_map = { 
		"00001001": "tab",
		"00001010": "newline"
	}
	json_result = "["
	byte_word = ""
	bite_count = 0
	is_next_new_entry = True
	for b in address_book_entries_binary_encoded:
		bite_count += 1
		byte_word += str (b)
		if bite_count == CHAR_SIZE:

			if is_next_new_entry == True:
				json_result += "\n\t{\n\t\t\""

			if (byte_word in bin_asciiname_map) and (bin_asciiname_map[byte_word] == "tab"):
				json_result += "\",\n\t\t\""
				is_next_new_entry = False
			elif (byte_word in bin_asciiname_map) and (bin_asciiname_map[byte_word] == "newline"):
				json_result += "},"
				is_next_new_entry = True
			else:
				ascii_dec_number = int ("0b" + byte_word, 2)
				json_result +=  chr (ascii_dec_number)
				is_next_new_entry = False
			byte_word = ""
			bite_count = 0

	json_result += "\n]"
	json_result = json_result.replace ("\t\"}", "}")
	json_result = json_result.replace (",\n\t}", "\n\t}")
	json_result = json_result.replace (",\n\t\t\"\n]", "\n\t}\n]")

	return json_result

print ("")
print (getAddressBookJSONFromBinary (binary_encoded_address_book))

"""
Intended output:

[
    {
        "id": 1,
        "name": "John Doe",
        "phone_number": "+14561234"
    },
    {
        "id": 2,
        "name": "Jin Kazama",
        "phone_number": "+43910728"
    },
    {
        "id": 3,
        "name": "Son Goku",
        "phone_number": "+43245001"
    }
]
"""

#address_book_entries_plain_text = address_book_db.getAllEntries ()