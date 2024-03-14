import os #importing the 'os module' which lets us use the system commands
import keyboard #importing the 'keyboard module' which lets us use the keyboard
import time #importing the 'time module' allows your program to use time / example: time.sleep(2) will make the program wait for 2 seconds
import subprocess #importing the 'subprocess module' allows us o open our program in a new terminal window



def open_terminal(): #function to open this program in a new terminal window
    script_name = "DCI_Class_Dating_App.py" #the name of the script
    gnome-terminal = "python3 " + script_name #the command to open the script in a new terminal window
    subprocess.Popen(open_terminal, shell=True) #opens the script in a new terminal window

open_terminal()



def clear_screen(): #function to clear the screen that we will call multiple times / this is the reason we imported the 'os module'
    os.system('clear')
clear_screen() #calling the function to clear the screen



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
player = 'man' #we give the variable 'player' the value of 'man'

print('\n''Viable options in this Demo are "Male" and "Female".''\n''Choose your sex:''\n')
print('1. Male              ''2. Female               ''\n')

player == input('Enter your choice: ')
if input == '1''man''male''men''males':
    player == 'man'
    print('\n''You have chosen to be a', player, '\n')
if input == '2''woman''female''women''females':
    player == 'woman'
    print('\n''You have chosen to be a', player, '\n')
else:
    print('\n''You have chosen to be a', player, '\n')


print('\n''Choose what you want to date:''\n')
print('1. Males              ''2. Females               ''3. Both''\n')
male = 1 #we give the variable 'male' the value of 1 / this is the first row of the list
female = 2 #we give the variable 'female' the value of 2 / this is the second row of the list

#we print out all the male names in the list
#for i in range(len(people[male])): #for each name in the first row
 #   print(people[male][i]) #print out a name from the list




#for sublist in people: #for each sublist in the list / there are a total of 2 sublists
 #   for name in sublist: #for each name in the list
  #      if name == 'Hassan': #if the name is Morgane
   #         print('Choose the lover you want to be') #prints out the name of the person you want to be
    #        break  #breaks the loop

