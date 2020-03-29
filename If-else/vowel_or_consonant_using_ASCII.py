character_ASCII = int(input("Enter ASCII of character:\n"))

if character_ASCII == 97 or character_ASCII == 101 or character_ASCII == 105 or character_ASCII == 111 or character_ASCII == 117 or character_ASCII == 65 or character_ASCII == 69 or character_ASCII == 73 or character_ASCII == 79 or character_ASCII == 85 :
	print(character_ASCII,"is a vowel")
else :
	print(character_ASCII,"is a consonant")