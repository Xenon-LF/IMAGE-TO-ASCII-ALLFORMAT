import sys
from PIL import Image
import datetime
import colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)

p = Style.BRIGHT
q = Fore.LIGHTBLUE_EX
r = Fore.LIGHTRED_EX
s = Fore.LIGHTMAGENTA_EX
t = Fore.RESET


print('\t'+p+s+'██╗░░██╗███████╗███╗░░██╗░█████╗░███╗░░██╗')
print('\t'+p+s+'╚██╗██╔╝██╔════╝████╗░██║██╔══██╗████╗░██║')
print('\t'+p+s+'░╚███╔╝░█████╗░░██╔██╗██║██║░░██║██╔██╗██║')
print('\t'+p+s+'░██╔██╗░██╔══╝░░██║╚████║██║░░██║██║╚████║')
print('\t'+p+s+'██╔╝╚██╗███████╗██║░╚███║╚█████╔╝██║░╚███║')
print('\t'+p+s+'╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝')
print('\t'+p+r+'        '+'https://github.com/Xenon-LF')
print('\t'+p+q+'     '+'█░░ █ █▀▀ █▀▀   █░█ ▄▀█ █▀▀ █▄▀')
print('\t'+p+q+'     '+'█▄▄ █ █▀░ ██▄   █▀█ █▀█ █▄▄ █░█')
print()
print()


def greetMe():
    CurrentHour = int(datetime.datetime.now().hour)
    if CurrentHour >= 0 and CurrentHour < 12:
       print('\t' +p+q+ 'GOOD MORNING')

    elif CurrentHour >= 12 and CurrentHour < 18:
       print('\t' +p+q+ 'GOOD AFTERNOON')

    elif CurrentHour >= 18 and CurrentHour < 0:
       print('\t' +p+q+ 'GOOD NIGHT')
    print()
    print()

greetMe()

while True:
    query = input(p+r+'do you want to CONTINUE?(yes/no)'+' '+p+s+'>'+t+' ')
    Fl = query[0].lower()
    if query == '' or not Fl in ['y', 'n']:
        break
    else:
        break
        
        
        
if Fl == ('y'):
    while True:
        print()
        print("\t"+p+q+"made by "+p+s+"X3N0N"+" "+p+q+"using python")
        print()

        print()
        print(p+q+'eg= ../Download/XENON.png')
        image_path = input(p+r+'PLEASE ENTER IMAGE PATH'+' '+p+s+'>'+t+' ')
        img = Image.open(image_path)
        width, height = img.size
        aspect_ratio = height/width

        
        while True:
        	query = input(p+r+'DO YOU WANT TO RESIZED OUTPUT'+p+s+'>'+t)
        	Fl = query[0].lower()
        	if query == '' or not Fl in ['y', 'n']:
        		break
        	else:
        		break
        		
        	
        if Fl == ('y'):
        		while True:
        			print()
        			print("\t"+p+q+"made by "+p+s+"X3N0N"+" "+p+q+"using python")
        			print()
        			imgrz = input('rezize')
        			new_width = imgrz
        			new_height = aspect_ratio * new_width * 0.55
        			img = img.resize((new_width, int(new_height)))
        			img = img.convert('L')
        			pixels = img.getdata()
        			chars = ["B","S","#","&","@","$","%","*","!",":","."]
        			new_pixels = [chars[pixel//25] for pixel in pixels]
        			new_pixels = ''.join(new_pixels)
        			new_pixels_count = len(new_pixels)
        			ascii_image = [new_pixels[index:index + new_width] for index in                   range(0, new_pixels_count, new_width)]
        			ascii_image = "\n".join(ascii_image)
        			print(ascii_image)
        			with open("XENON.txt", "w") as f:
        				f.write(ascii_image)
        				print()
        				cont = input("do you WANT TO REPEAT? yes/no > ")   
        				
        				if cont == '' or not cont in ['y','yes','YES','Y']:
        					print()
        					print("\tTHANK YOU!")
        					break
        			
        			
        if Fl == ('n'):
        	print()
        	print('\t now output is orginal size')
        	img = img.convert('L')
        	pixels = img.getdata()
        	chars = ["B","S","#","&","@","$","%","*","!",":","."]
        	new_pixels = [chars[pixel//25] for pixel in pixels]
        	new_pixels = ''.join(new_pixels)
        	new_pixels_count = len(new_pixels)
        	ascii_image = [new_pixels[index:index + width] for index in                    range(0, new_pixels_count, width)]
        	ascii_image = "\n".join(ascii_image)
        	print(ascii_image)
        	with open("XENON.txt", "w") as f:
        		f.write(ascii_image)
        	cont = input(p+r+'do you WANT TO REPEAT? yes/no'+' '+p+s+'>'+q+' ')   
        
        
        if cont == '' or not cont in ['y','yes','YES','Y']:
            print()
            print(p+s+"\tTHANK YOU!")
            break
            
            
            
if Fl == ('n'):
    print()
    print(p+s+'\tTHANK YOU!')
