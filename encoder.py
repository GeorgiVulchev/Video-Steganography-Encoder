import cv2
import os
import sys
from colorama import init
from colorama import Fore,Style,Back
from PIL import Image, ImageFilter, ImageDraw, ImageFont

def preparation()
    file = open("file_name.txt", "r")
    secret_word = file.read()
    file.close()
    print (secret_word)
    vidcap = cv2.VideoCapture("file_name.avi")
    length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

def algorithm():
	len_sentence = int(len(secret_word))
	letters=1
    
	while (length-2)<(len_sentence/letters) :
		letters+=1
        
	number_frames = len_sentence/letters
	print("The number of frames in the video is: " + str (length))
	print("The length is: " + str (len_sentence))
	print("The letters in one frame: "+ str (letters))
	return str (letters), str (number_frames)

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

def strToBin(secret):
    string = ""
    for letter in secret:
        string = string + str(format(ord(letter), '08b'))
    return string

def even(color):
    if (color % 2 == 0):
        return True
    else:
        return False

def change(color, bit):
    if (bit == "0") and (even(color)):
        return color
    if (bit == "0") and not (even(color)):
        return color - 1
    if (bit == "1") and even(color):
        return color + 1
    if (bit == "1") and not (even(color)):
        return color

def numberBytes_digits():
	codeText = strToBin(secret_word)
	numberBytes = len(codeText)
	count = len(str(numberBytes))
	digits_number = (str(count))
	digits = strToBin (str(count))
	br = 0
	path = "PATH"
	pic = Image.open(path + "frame00000.bmp")
	pixels = pic.load()
	stop = 0
    
	for i in range(0, 3):
		r, g, b = pixels[i, 0]
		if (br < numberBytes) and (stop < 8):
			r = change(r, digits[br])
			br += 1
			stop += 1
		if (br < numberBytes) and (stop < 8):
			g = change(g, digits[br])
			br += 1
			stop += 1
		if (br < numberBytes) and (stop < 8):
			b = change(b, digits[br])
			br += 1
			stop += 1
		pixels[i, 0] = r, g, b
        
	pic.save(path + "frame00000.bmp")
	pic.close()
	return digits_number

def numberBytes():
	digits_number =  numberBytes_digits()
	codeText = strToBin(secret_word)
	numberBytes = len(codeText)
	hide = strToBin(str(numberBytes))
	br = 0
	path = "PATH"
	pic = Image.open(path + "frame00000.bmp")
	pixels = pic.load()
	stop = 0
    
	for i in range(0, 3 * int(digits_number)):
		r, g, b = pixels[i, 9]
		if (br < numberBytes) and (stop < 8 * int(digits_number)):
			r = change(r, hide[br])
			br += 1
			stop += 1
		if (br < numberBytes) and (stop < 8 * int(digits_number)):
			g = change(g, hide[br])
			br += 1
			stop += 1
		if (br < numberBytes) and (stop < 8 * int(digits_number)):
			b = change(b, hide[br])
			br += 1
			stop += 1
		pixels[i, 9] = r, g, b
        
	pic.save(path + "frame00000.bmp")
	pic.close()

def coder():
	blockPrint()
	letters, number_frames = algorithm()
	enablePrint()
	list1 = []
	path = "PATH"
    
	for filename1 in os.listdir(path):
		list1.append(path + "\\" + filename1)
		
	codeText = strToBin(secret_word)
	numberBytes = len(codeText)
	br=0
	
	for img in range(1,len(list1)):
		orig_Image = Image.open(list1[img])	
		orig_pixels = orig_Image.load()
		stop = 0
        
		for i in range(0, 3 * int (letters)):
			r, g, b = orig_pixels[i, 0]
            
			if (br < numberBytes) and (stop < 8 * int (letters)):
				r = change(r, codeText[br])
				br += 1
				stop += 1
			if (br < numberBytes) and (stop < 8 * int (letters)):
				g = change(g, codeText[br])
				br += 1
				stop += 1
			if (br < numberBytes) and (stop < 8 * int (letters)):
				b = change(b, codeText[br])
				br += 1
				stop += 1
                
			orig_pixels[i, 0] = r, g, b
		orig_Image.save(list1[img])
		orig_Image.close()

init()
preparation()
algorithm()
numberBytes_Digits()
numberBytes()
coder()
