
def convert():
	print("before you answer the another question copy the results")
	init = 1
	while init == 1:
		n= int(input("'1' for text to hex and '2' for hex to text: "))
		if n == 1:
			arr = input("text: ")   # takes the whole commandline stuff
			l = list(map(str,arr.split())) # split those numbers with space( becomes ['2','3','6','6','5']) and then map every element into int (becomes [2,3,6,6,5])
			hex_copy = []
			for x in range(len(l)):
				res = [] 
				res[:] = l[x]
				space = ' '
				for char in range(len(res)):
					res[char] = ord(res[char])
					res[char] = hex(res[char])
					hx = []
					hx[:] = res[char]
					hx[2] = hx[2] + hx[3] + space
					hex_copy.append(hx[2])
			for x in range((len(hex_copy)-1)):
				hex_copy[0] =  hex_copy[0] + hex_copy[x+1]
			print(hex_copy[0])	
			c = int(input("Another one? '1' or '0': "))
			if c == 1:
				continue
			else :
				break 
		else : 
			hex_input = input("hex with space like '71 64':")
			dec_output = list(map(str,hex_input.split(' ')))
			for hexi in range(len(dec_output)):
				dec_output[hexi] = bytes.fromhex(dec_output[hexi])
				dec_output[hexi] = dec_output[hexi].decode("ASCII")
			print(dec_output) 
			d = int(input("Another one? '1' or '0'"))
			if d == 1:
				continue
			else : 
				break 

convert()

		# for binary in range(len(byte_array)):
			# dec_output[bin] = hex(byte_array[binary])


