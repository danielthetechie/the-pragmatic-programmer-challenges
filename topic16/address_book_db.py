"""
Design a small address book database (name, phone number, and
so on) using a straightforward binary representation in your
language of choice. Do this before reading the rest of this challenge.
"""

# The algorithm idea is to map each character into an ASCII number
# and then convert it into binary.
def getBinaryRepresentationOfString (string):
	#return ''.join (format (ord(i), '08b') for i in string)
	res = ""
	for c in string:
		c = ord (c)
		c = str (bin (c)[2:]) # To remove the prefix '0b' returned by bin().

		# Since a char is 8 bits long, if the binary representation of c
		# is shorter than 8 bits, we need to fill the missing bits by 0s.

		missing_bits = 8 - len (c)
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

address_book_db.addEntryToAddressBook ({ 'id': 1, 'name': 'Johh Doe', 'phone_number': '+14561234' })
address_book_db.addEntryToAddressBook ({ 'id': 2, 'name': 'Jin Kazama', 'phone_number': '+43910728' })
address_book_db.addEntryToAddressBook ({ 'id': 3, 'name': 'Son Goku', 'phone_number': '+43245001' })

encoded_address_book = getBinaryRepresentationOfString (address_book_db.getAllEntries ())
print (encoded_address_book)

#00110001000010010100101001101111011010000110100000100000010001000110111101100101000010010010101100110001001101000011010100110110001100010011001000110011001101000000100100001010001100100000100101001010011010010110111000100000010010110110000101111010011000010110110101100001000010010010101100110100001100110011100100110001001100000011011100110010001110000000100100001010001100110000100101010011011011110110111000100000010001110110111101101011011101010000100100101011001101000011001100110010001101000011010100110000001100000011000100001001

"""
Translate that format into a plain-text format using XML or JSON
"""

