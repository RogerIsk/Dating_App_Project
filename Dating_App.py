import os #importing the 'os module' which lets us use the system commands
import keyboard #importing the 'keyboard module' which lets us use the keyboard
import time #importing the 'time module' allows your program to use time / example: time.sleep(2) will make the program wait for 2 seconds
import subprocess #importing the 'subprocess module' allows us o open our program in a new terminal window
from faker import Faker

def open_terminal(): #function to open this program in a new terminal window
    script_name = "DCI_Class_Dating_App.py" #the name of the script
    terminal_command = "python3 " + script_name #the command to open the script in a new terminal window
    subprocess.Popen(terminal_command, shell=True) #opens the script in a new terminal window
open_terminal() #calling the function to open the script in a new terminal window

def clear_screen(): #function to clear the screen that we will call multiple times / this is the reason we imported the 'os module'
    os.system('clear') #this command clears the screen
clear_screen() #calling t1he function to clear the screen

def opening_screen(): #function to print the opening screen
    print('Welcome to the Dating App!''\n''\n')
opening_screen()
#time.sleep(2) #pauses the program for 2 seconds
clear_screen() #calling the function to clear the screen



#a list of people looking for love
people = [['Markus' , 'Anton' , 'Benjamin' , 'Erik' , 'Burak', 'Dess' , 'Roger' , 'Roman' , 'Sunny' , 'Hassan'] ,
          ['Hiba' , 'Morgane','Vanessa']] 

male   = ['man','male','men','males', 1]           #we give the variable different values through the usage of a list
female = ['woman','female','women','females', 2]   #we give the variable different values through the usage of a list
male   = 1 #we give the variable 'male' the value of 1 / this is the first row of the list
female = 2 #we give the variable 'female' the value of 2 / this is the second row of the list
player = 'man' #we give the variable 'player' the value of 'man'

print('\n''Viable options in this Demo are "Male" and "Female".''\n''Choose your sex:''\n')
print('1. Male              ''2. Female               ''\n')

player == input('Enter your choice: ' '\n')
if input == '1''man''male''men''males':
    player == 'man'
    clear_screen() #calling the function to clear the screen
    print('\n''You are a ', player, '\n')

if input == '2''woman''female''women''females':
    player == 'woman'
    
    clear_screen() #calling the function to clear the screen
    print('\n''You are a', player, '\n')









print('\n''Choose what you want to date:''\n')
print('1. Males              ''2. Females               ''3. Both''\n')



