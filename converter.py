
def convert():
	con = 2
	c = 0
	init = 0
	space = ' '
	while init == 0:
		try:
			n1	= int(input("'1' for text to hex and '2' for hex to text:"))
			if not ((n1 == 1)|(n1 == 2)): 
				raise ValueError 
		except ValueError :
			pl10(1,2)
			continue
		platz(70)
		if n1 == 1:
			while con == 2:
				hex_output = []
				arr = input("Text: ")   							# takes the whole commandline stuff
				l = list(map(str,arr.split())) 						# splits into words at ' '
				for word in range(len(l)):
					hex_copy = []
					res = [] 
					res[:] = l[word]								# splits chars 
					for char in range(len(res)):	 
						res[char] = ord(res[char])
						res[char] = hex(res[char])
						hx = []
						hx[:] = res[char]							#splits hex into [0,x,F,F]
						hx[2] = hx[2] + hx[3] 						#adds index 3 to index 2 [0,x,FF,F]
						hex_copy.append(hx[2])						#adds index 3 to hex_copy 
					frti1(hex_copy)
					hex_output.append(hex_copy[0])
				frti1(hex_output,1)
				print(hex_output[0])
				platz(70)
				while con == 2:	
					try:
						c = int(input("Another text phrase/char ? '1' or '0':"))
						break
					except ValueError :
						pl10(1,0)
						continue
				if c == 1:
					continue
				else :
					break 

		else : 
			while n1 == 2:
				n4 = 0
				while con == 2:
					hex_input = input("Seperate with space '5E6971 647E 74':")
					hex_input += ' '
					dec_output = list(map(str,hex_input.split(' ')))
					output = []
					if (len(dec_output)==1):        #kein Space in der Eingabe
						n5 = 0
						n6 = 0
						for word in dec_output:
							n5 += 1
						n6 = n6+n5
						n5 = 0
					else:
						n5 = 0
						n6 = 0
						for word in dec_output:     #für jedes seperrierte Element
							for char in word:		#erhöhe pro Zahl n5 um 1
								n5 += 1
							n6 = n6 + n5
							n5 = 0
					if ((n6%2) == 1):
						print("Please enter Hex code only / immer 2 Elemente pro HEX") 
						continue
					else :
						break
				for hexi in range(len(dec_output)):
					dec_output[hexi] = bytes.fromhex(dec_output[hexi])
					dec_output[hexi] = dec_output[hexi].decode("ANSI")
					dec_output[hexi] = dec_output[hexi] + space
					output.append(dec_output[hexi])
				frti1(output)
				platz(70)
				print(output[0]) 
				platz(70)
				while con == 2:
					try:
						d = int(input("Another hex phrase? '1' or '0':"))
						break
					except ValueError:
						pl10(1,0)
						continue
				if d == 1:
					continue
				else : 
					break
											
		init = int(input("Quit? '1' or '0':"))
		 	
def platz(a=0):
	print('-'*a)

def frti1(array, a=0):									#adds everything to index 0
	space=' '
	for x in range(len(array)-1):				
		array[0]=array[0]+a*space+array[x+1]

def pl10(a=0, b=0):
	print("'",a,"' or '",b,"' please!",sep='')

platz(70)
convert()

		

