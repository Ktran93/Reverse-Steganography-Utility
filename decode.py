from PIL import Image
import binascii
import math

#converts the binary string to ascii 
def stringDecode(input):
	input_l = [input[i:i+8] for i in range(0,len(input),8)]
	return ''.join([chr(int(c,base=2)) for c in input_l]) 

#adds LSB of rgb value to  myList
def createList(myList, rgb):	
	myList.append(rgb[0] & 1)  
	myList.append(rgb[1] & 1)
	myList.append(rgb[2] & 1)
	return myList

def main():

	#user enter filename 
	print("Enter fileName to decode:")
	myString = input()
	type(myString)

	
	#Open the image
	myImage = Image.open(myString + ".png")
	#get the width and height to image size
	width, height = myImage.size 			
	
	#Set width and height to actual size
	width, height = width -1, height -1

	#create the inital list to store the least significant bit
	readSize = []
	
	#gets the text size from the first 11 pixels starting from bottom right corner
	for i in range(0,11):
		
		#gets the current pixel rgb value
		rgb = myImage.getpixel((width - i , height))
			
		#adds the rgb value into a list 		
		createList(readSize, rgb)
	
	#resizes the list to drop the 33th item in list
	print(readSize)
	readSize = readSize[0:32:1]
	
	#join list into string 
	stringSize =''.join(str(e) for e in readSize )	
	
	#convert stringSize to int	
	bitsToRead = int(stringSize, 2)
	print(bitsToRead)
	
	#convert bits to pixel amount to read
	
	pixelsReaminder = bitsToRead % 3
	pixelsToRead = (math.ceil(bitsToRead // 3))
	pixelsToRead = pixelsToRead + pixelsReaminder
	
	
	
	print(pixelsToRead)
	
	#create new list to store full hex value for each r, g, b
	binaryText = []
	
	e = 11
	g = 0
	
	#create int for total pixels to read 
	totalPixelsToRead = int(pixelsToRead + 12)
	
	for f in range (12,totalPixelsToRead):	
		
		#checks if e reached the end of the line of pixels and resets position
		if e == width + 1:
			e = 0
			g += 1
		 
		rgb = myImage.getpixel((width - e, height - g))
		createList(binaryText, rgb)
		e += 1
	print(binaryText)
	#merge list into string
	stringText = ''.join(str(x) for x in binaryText)
	
	#converts the binary string to ascii
	print(stringDecode(stringText))
	
if __name__== '__main__':
	main()
