"""
=====================================================================
=====================================================================

1) Design a small address book database (name, phone number, and
so on) using a straightforward binary representation in your language 
of choice. Do this before reading the rest of this challenge.

=====================================================================
=====================================================================
"""

CHAR_SIZE = 8 # In bits

class AddressBook ():
	def __init__ (self):
		self.entries = []

	def getEntries (self):
		return self.entries

	def addEntry (self, entry):
		self.entries.append (entry)

	def printAllContactsInfoTable (self):
		res = ""
		min_tabsize = 0

		if len (self.entries) > 0:
			first_entry = self.entries[0]
			for key in first_entry:
				res += str (key) + "\t"
			res += "\n"

		for entry in self.entries:
			for key in entry:
				res += str (entry[key]) + "\t"
			res += "\n"

		# To have an adequate tab size, let's find the longest entry value
		# because that's the one that will define the minimum tab size required.

		for entry in self.entries:
			for key in entry:
				if (len (str (entry[key])) > min_tabsize):
					min_tabsize = len (str (entry[key]))

		min_tabsize += 5

		print (res[:-1].expandtabs (min_tabsize))


# The algorithm idea is to map each character into an ASCII number
# and then convert it into binary.
def getBinaryRepresentationOfString (string):
	res = ""
	for c in string:
		c = ord (c) # Get the ASCI number of c
		c = str (bin (c)[2:]) # To remove the prefix '0b' returned by bin().

		# Since a char is 8 bits long, if the binary representation of c
		# is shorter than 8 bits, we need to fill the missing bits with 0s.

		missing_bits = CHAR_SIZE - len (c)
		c = ("0" * missing_bits) + c
		res += str (c)

	return res

address_book_db = AddressBook ()

address_book_db.addEntry ({ 'id': 1, 'name': 'John Doe', 'phone_number': '+14561234' })
address_book_db.addEntry ({ 'id': 2, 'name': 'Jin Kazama', 'phone_number': '+43910728' })
address_book_db.addEntry ({ 'id': 3, 'name': 'Son Goku', 'phone_number': '+43245001' })

address_book_data = address_book_db.getEntries ()
address_book_data_str = str (address_book_data)

binary_encoded_address_book_data = getBinaryRepresentationOfString (address_book_data_str)

print ("Answer of 1):")
print (binary_encoded_address_book_data)

"""
Output:

010110110111101100100111011010010110010000100111001110100010000000110001001011000010000000100
111011011100110000101101101011001010010011100111010001000000010011101001010011011110110100001
101110001000000100010001101111011001010010011100101100001000000010011101110000011010000110111
101101110011001010101111101101110011101010110110101100010011001010111001000100111001110100010
000000100111001010110011000100110100001101010011011000110001001100100011001100110100001001110
111110100101100001000000111101100100111011010010110010000100111001110100010000000110010001011
000010000000100111011011100110000101101101011001010010011100111010001000000010011101001010011
010010110111000100000010010110110000101111010011000010110110101100001001001110010110000100000
001001110111000001101000011011110110111001100101010111110110111001110101011011010110001001100
101011100100010011100111010001000000010011100101011001101000011001100111001001100010011000000
110111001100100011100000100111011111010010110000100000011110110010011101101001011001000010011
100111010001000000011001100101100001000000010011101101110011000010110110101100101001001110011
101000100000001001110101001101101111011011100010000001000111011011110110101101110101001001110
010110000100000001001110111000001101000011011110110111001100101010111110110111001110101011011
010110001001100101011100100010011100111010001000000010011100101011001101000011001100110010001
1010000110101001100000011000000110001001001110111110101011101
"""

"""
===================================================================
===================================================================

2) Translate that format into a plain-text format using XML or JSON

===================================================================
===================================================================
"""

# The algorith consists on splitting the binary sequence into chunks
# of 8 bits, convert them to base-10 integers and then map their 
# ASCII decimal representation to their corresponding char.
def getPlainTextRepresentationOfBinaryWord (binary_word):
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

# We assume the parameter we receive is a well formatted string,
# i.e. a string looking like a Python dictionary.
def getJSONFromDictionaryString (dictionary_string):
	json_result = ""
	dictionary_string = dictionary_string.replace ("', ", "',")
	for c in dictionary_string:
		if c == "{":
			json_result += "\n\t{\n\t\t"
		elif c == "'":
			json_result += "\""
		elif c == "}":
			json_result += "\n\t}"
		else:
			json_result += c

	json_result = json_result.replace ("\",", "\",\n\t\t")
	json_result = json_result.replace (", \"", ",\n\t\t\"")
	json_result = json_result.replace ("},\n", "},")
	json_result = json_result.replace ("}]", "}\n]")

	return json_result

decoded_to_str_address_book_entries = getPlainTextRepresentationOfBinaryWord (binary_encoded_address_book_data)

print ("\n\nAnswer of 2):")
print (getJSONFromDictionaryString (decoded_to_str_address_book_entries))

"""
Output: 

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

# Additionally, and although this is not the main goal of this exercise,
# we could also print it nicely as a table

print ("")
address_book_db.printAllContactsInfoTable ()

"""
Output: 

id             name           phone_number   
1              John Doe       +14561234      
2              Jin Kazama     +43910728      
3              Son Goku       +43245001
"""

"""
=======================================================================
=======================================================================

3) For each version, add a new, variable-length field called directions
in which you might enter directions to each person’s house.

=======================================================================
=======================================================================
"""

# 3.1) Plain text file version:

# The AddressBook class is already defined, and for the sake of keeping
# the order in the exercises, I will create a separate function and add
# add it to the class as a method.

def addDirectionToEntryById (self, direction, entry_id):
	entries = self.getEntries ()

	for entry in entries:
		if entry["id"] == entry_id:
			entry["direction"] = direction
			return entry

AddressBook.addDirectionToEntryById = addDirectionToEntryById

address_book_db.addDirectionToEntryById ("Yakushima's mountains, Japan", 2)

print ("\n\nAnswer of 3):\n3.1) After modifying the entries with plain text: \n")
print (getJSONFromDictionaryString (str (address_book_db.getEntries ())))

"""
Output:

[
	{
		"id": 1,
		"name": "John Doe",
		"phone_number": "+14561234"
	}, 
	{
		"id": 2,
		"name": "Jin Kazama",
		"phone_number": "+43910728",
		"direction": "Yakushima"s mountains, Japan"
	}, 
	{
		"id": 3,
		"name": "Son Goku",
		"phone_number": "+43245001"
	}
]
"""

# 3.2) Binary version:

def addDirectionToBinaryEntryById (direction_value, entry_id, address_book_data_binary):
	is_updated = False
	direction_key = getBinaryRepresentationOfString (", 'direction': ")
	direction_value = getBinaryRepresentationOfString ("'" + direction_value + "'")
	entry_id = getBinaryRepresentationOfString (str (entry_id))

	id_key = getBinaryRepresentationOfString ("'id': ")
	id_key_and_value_bin = id_key + entry_id

	updated_entries_binary = ""

	for c in address_book_data_binary:
		updated_entries_binary += c
		if (id_key_and_value_bin in updated_entries_binary) and is_updated == False:
			updated_entries_binary += direction_key + direction_value
			is_updated = True

	return updated_entries_binary

updated_address_book_binary = addDirectionToBinaryEntryById ("Mount Paozu, Japan", 3, binary_encoded_address_book_data)
updated_address_book_plain_text = getPlainTextRepresentationOfBinaryWord (updated_address_book_binary)
json_updated_address_book = getJSONFromDictionaryString (updated_address_book_plain_text)

print ("\n\n3.2) After modifying the entries through their binary representation: \n")
print (json_updated_address_book)

"""
Output:

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
		"direction": "Mount Paozu, Japan",
		"name": "Son Goku",
		"phone_number": "+43245001"
	}
]
"""

"""
=======================================================================
=======================================================================

4) What issues come up regarding versioning and extensibility? 
5) Which form was easier to modify? 
6) What about converting existing data?

=======================================================================
=======================================================================
"""

"""
Answers:

4)	In the binary way of working with the address book, adding a new "direction" key was more challenging 
	because you have to parse the binary code and find the correct needle, and in the function
	addDirectionToBinaryEntryById () I didn't even write a validation code to check whether the key
	"direction" exists or not, so this would have been another not-so-straighforward subchallenge.

5)	By looking at the code below the 3.1) section and then the code below 3.2) the question answers itself.

6)	Converting data is not a problem once we use the getBinaryRepresentationOfString () and
	getPlainTextRepresentationOfBinaryWord () functions defined before, but of course, if the database grows large,
	then working with plain text directly is more performant than encoding and decoding data for every operation
	we do in the database.

"""