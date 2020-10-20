
def convert():
	init = 0
	while init == 0:
		n1= int(input("'1' for text to hex and '2' for hex to text:"))
		if n1 == 1:
			while n1 == 1:
				n4 = 0
				n3 = int(input("one phrase'1' or one char'2':"))
				if n3 == 1:	
					while n3 == 1:
						arr = input("Text: ")   # takes the whole commandline stuff
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
						c = int(input("Another text phrase? '1' or '0':"))
						if c == 1:
							continue
						else :
							break 
					n4 = int(input("But another text char ? '0' or '1':"))
					if n4 == 1:
						continue
					else : 
						break 
				else :
					while n3 == 2:
						arr = input("Char: ")
						arr = ord(arr)
						arr = hex(arr)
						hx = []
						hx[:] = arr
						hx[2] = hx[2] + hx[3]
						print(hx[2])
						c = int(input("Another text char? '1' or '0':"))
						if c == 1:
							continue
						else :
							break
					n4 = int(input("But another text phrase ? '0' or '1':"))
					if n4 == 1:
						continue
					else : 
						break 
		else : 
			while n1 == 2:
				n4 = 0
				n2 = int(input("'1' for one char ='FF' and '2' for more ='FF FF':"))
				if n2 == 2:				
					while n2 == 2:	
						hex_input = input("Hex with space like '71 64':")
						dec_output = list(map(str,hex_input.split(' ')))
						for hexi in range(len(dec_output)):
							dec_output[hexi] = bytes.fromhex(dec_output[hexi])
							dec_output[hexi] = dec_output[hexi].decode("ASCII")
						print(dec_output) 
						d = int(input("Another hex phrase? '1' or '0':"))
						if d == 1:
							continue
						else : 
							break
					n4 = int(input("But another hex char ? '0' or '1':")) 
					if n4 == 1:
						continue
					else : 
						break 
				else :
					while n2 == 1:	
						hex_input = input("Hex:")
						dec_output = list(map(str,hex_input.split(' ')))
						for hexi in range(len(dec_output)):
							dec_output[hexi] = bytes.fromhex(dec_output[hexi])
							dec_output[hexi] = dec_output[hexi].decode("ASCII")
						print(dec_output) 
						d = int(input("Another hex char? '1' or '0':"))
						if d == 1:
							continue
						else : 
							break
					n4 = int(input("But another hex phrase ? '0' or '1':"))
					if n4 == 1:
						continue	
					else :
						break			
		init = int(input("Quit? '1' or '0':"))
		 	
convert()

		# for binary in range(len(byte_array)):
			# dec_output[bin] = hex(byte_array[binary])


