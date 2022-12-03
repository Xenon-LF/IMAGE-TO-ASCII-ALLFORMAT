import sys
import os
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
u = Fore.YELLOW

print()
print()
def main():


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


    def ASCII():

        print('     '+p+r+'~ '+p+u+'found your image path')
        while True:
            query = input(p+r+'do you want to CONTINUE?(yes/no)'+'  '+p+s+'>'+t+' ')
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
                print('     '+p+r+'~ '+p+u+'eg ÷  ../Download/XENON.png')
                print('     '+p+r+'~ '+p+u+"image in this folder don't want path. you can enter image name")
                image_path = input(p+r+'PLEASE ENTER IMAGE PATH'+' '+p+s+'>'+t+' ')
                img = Image.open(image_path)
                width, height = img.size
                aspect_ratio = height/width
                print()
                print("\t"+p+q+"made by "+p+s+"X3N0N"+" "+p+q+"using python")
                print()
                print()
                

                
                while True:
                        query = input(p+r+'DO YOU WANT TO RESIZED OUTPUT?(yes/no) '+p+s+' >  '+t)
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
                                        print('     '+p+r+'~ '+p+u+'ONLY ENTED NUMBERs !')
                                        print('     '+p+r+'~ '+p+u+'now you enter width pixel no. for resized and automaticaly resized hight !')
                                        new_size = ''
                                        new_size = input(p+r+'WIDTH pixel number for resized'+p+s+'  >  '+p+t)
                                        if not new_size.isdigit():
                                        		print(p+r+'       please ENTED number!')
                                        		continue
                                        else:
                                        		int(new_size)
                                        		new_size=int(new_size)
                                        		new_width = new_size
                                        		new_height = aspect_ratio * new_width * 0.55
                                        		img = img.resize((new_width, int(new_height)))
                                        		img = img.convert('L')
                                        		pixels = img.getdata()
                                        		chars = ["B","S","#","&","@","$","%","*","!",":","."]
                                        		new_pixels = [chars[pixel//25] for pixel in pixels]
                                        		new_pixels = ''.join(new_pixels)
                                        		new_pixels_count = len(new_pixels)
                                        		ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
                                        		ascii_image = "\n".join(ascii_image)
                                        		print()
                                        		print(p+s+ascii_image)
                                        		print()
                                        		print('     '+p+r+'~ '+p+u+'you'+p+r+' must'+p+u+' enter name for output')
                                        		outputnam= ''
                                        		outname = (input(p+r+"Enter name for output"+' '+p+s+'>'+t+' '))
                                        		if not outname.isalnum():
                                        				print (p+r+ '      please ENTER OUTPUT FILE NAME')
                                        				continue
                                        		else:
                                        				with open(outname, "w") as f:
                                        				 f.write(ascii_image)
                                        				 print()
                                        				 print('     '+p+r+'~ '+p+u+'do you want to go main menu enter'+p+s+' main')
                                        				 print('     '+p+r+'~ '+p+u+'you entered'+p+r+" 'y' "+p+u+'you can resized this image again !')
                                        				 cont = input(p+r+"do you WANT TO REPEAT? yes/no/main"+p+s+" > "+p+t)
                                        				 print()
                                        				 if cont == ("main"):
                                        				    				os.system('clear')
                                        				    				main()
                                        				 elif cont == '' or not cont in ['y','yes','YES','Y']:
                                        				    			     print()
                                        				    			     print(p+s+"\tTHANK YOU!")
                                        				    			     break
                                
                                        
                                        
                                        
                if Fl == ('n'):
                        print()
                        print("\t"+p+q+"made by "+p+s+"X3N0N"+" "+p+q+"using python")
                        print()
                        print()
                        print('     '+p+r+'~ '+p+u+'now output is orginal size')
                        print()
                        img = img.convert('L')
                        pixels = img.getdata()
                        chars = ["B","S","#","&","@","$","%","*","!",":","."]
                        new_pixels = [chars[pixel//25] for pixel in pixels]
                        new_pixels = ''.join(new_pixels)
                        new_pixels_count = len(new_pixels)
                        ascii_image = [new_pixels[index:index +width] for index in range(0, new_pixels_count , width)]
                        ascii_image = "\n".join(ascii_image)
                        print()
                        print(p+s+ascii_image)
                        print()
                        outname = ''
                        outname = input(p+r+"Enter name for output"+' '+p+s+'>'+t+' ')
                        if not outname.isalnum():
                        		print()
                        		print(p+r+'      please ENTER OUTPUT name')
                        		print()
                        		continue
                        else:
                        	       with open(outname, "w") as f:
                        	       	f.write(ascii_image)
                        	       print()
                        	       cont = input(p+r+'do you WANT TO REPEAT? yes/no'+' '+p+s+'>'+q+' ')
                        	       print()
                        	       if cont == ("main"):
                        	              os.system('clear')
                        	              main()
                        	       elif cont == '' or not cont in ['y','yes','YES','Y']:
                        	               	       	       print()
                        	               	       	       print(p+s+"\tTHANK YOU!")
                        	               	       	       break
                
                
                if cont == '' or not cont in ['y','yes','YES','Y']:
                    print()
                    print(p+s+"\tTHANK YOU!")
                    break
                    
                    
                    
        if Fl == '' or not Fl in ['y','yes','YES','Y'] :
            print()
            print(p+s+'\tTHANK YOU!')

    ASCII()

main()

