from PIL import Image
import binascii
import math

#function to write string binary value to rgb values
def writeToImage(startPos,offset, myImage, myList, len, width, height):
	n = 0
	e = offset
	for f in range (startPos, len + e):

		#reset the width when it reaches the end of a roll
		if e == width + 1:
			e = 0

			#reduces the height of the image by 1	
			n += 1	

		#cycle through each pixel's rgb value 
		for k in range(0,3):
			
			if k == 0:
				
				#check first element in list is 0
				if myList[0] == 0:

					myList.pop(0)
					
					#if the element at width and height is odd, subtract 1 to make it even
					if myImage[width - e, height - n][0] % 2 == 1:
						value = myImage[width - e, height - n][0] - 1
						myImage[width - e, height - n] = (value, myImage[width - e, height - n][1], myImage[width - e, height - n][2])
						
				#check first element in list is 1
				elif myList[0] == 1:

					myList.pop(0)

					#if the elemnt at width and height is even, subtract 1 to make it odd
					if myImage[width - e, height - n][0] % 2 == 0:
						value = myImage[width - e, height - n][0] + 1
						myImage[width - e, height - n] = (value, myImage[width - e, height - n][1], myImage[width - e, height - n][2])
						
					
			elif k == 1:
				
				if myList[0] == 0:

					myList.pop(0)

					if myImage[width - e, height - n][1] % 2 == 1:
						value = myImage[width - e, height - n][1] - 1
						myImage[width - e, height - n] = (myImage[width - e, height - n][0], value, myImage[width - e, height - n][2])
						
				elif myList[0] == 1:

					myList.pop(0)

					if myImage[width - e, height - n][1] % 2 == 0:
						value = myImage[width - e, height - n][1] + 1
						myImage[width - e, height - n] = (myImage[width - e, height - n][0], value, myImage[width - e, height - n][2])
						
            
			else:
				
				if myList[0] == 0:

					myList.pop(0)

					if myImage[width - e, height - n][2] % 2 == 1:
						value = myImage[width - e, height - n][2] - 1
						myImage[width - e, height - n] = (myImage[width - e, height - n][0], myImage[width - e, height - n][1], value)
						
				elif myList[0] == 1:

					myList.pop(0)
					
					if myImage[width - e, height - n][2] % 2 == 0:
						value = myImage[width - e, height - n][2] + 1
						myImage[width - e, height - n] = (myImage[width - e, height - n][0], myImage[width - e, height - n][1], value)
					
		e += 1					
	return myImage
				

def main():

	print ("Enter Message: ")
	
	#create for user input
	myString = input()
	type(myString)	

	#get size of string
	myStringSize = len(myString)

	#convert string size to bits
	myStringSize = myStringSize * 8
	
	pixelsToWrite = (math.ceil(myStringSize / 3))
	
	pixelsToWrite = int(pixelsToWrite)
	
	#format string bits to binary and to 33 bits
	StringSizeInBinary = '{0:032b}'.format(myStringSize) 
	StringSizeInBinary = StringSizeInBinary + '0'	
	
	#Open the image
	print("Enter image name to open: ")
	imageToOpen = input()
	type(imageToOpen)	

	myImage = Image.open(imageToOpen +".png")
	manipImage = myImage.load()

	#Set the width and height to image size
	width, height = myImage.size 			
	
	#Set width and height to actual size
	width, height = width -1, height -1
		
	#create list to store the least significant bit
	StringSizeInBinaryList =[int(i) for i in str(StringSizeInBinary)]
	
	#write the string size to the first 11 pixels 
	manipImage = writeToImage(0, 0, manipImage, StringSizeInBinaryList, 11, width, height)		
	
	myStringInBinary = ''.join(format(ord(x), 'b').zfill(8) for x in myString)
	
	myStringInBinaryList = list(map(int, myStringInBinary))

	#write the string to every pixel after 12 to until equal to size of string
	manipImage = writeToImage(12, 11, manipImage, myStringInBinaryList, pixelsToWrite, width, height)
	
	print("Enter name of Image to save: ")
	imageName = input()
	type(imageName)
	myImage.save(imageName + ".png")
	
if __name__== '__main__':
	main()
