
def advconvert():
	while True:
		print('-'*70)
		input_c = input("Universal Chiffre hier eingeben: ")
		hex_k = "0123456789ABCDEF"
		output = ""
		puffer = ""
		for char in input_c:
			if (puffer != ""):
				puffer += char
				output += chr(int(puffer, 16))
				puffer = ""
				continue
			if char in hex_k:
				puffer += char
			else : 
				output += char
		print('-'*70)
		print(output)
advconvert()

