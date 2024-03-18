import os #importing the 'os module' which lets us use the system commands
import keyboard #importing the 'keyboard module' which lets us use the keyboard
import time #importing the 'time module' allows your program to use time / example: time.sleep(2) will make the program wait for 2 seconds

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

player = ''
print('\nViable options in this Demo are "Male" and "Female".\nChoose your sex:\n\n1. Male              2. Female\n')

while True:
    player = input('Enter your choice: \n\n').lower()  # Convert input to lowercase for case-insensitive comparison
    if player in ['1', 'man', 'male', 'men', 'males']:
        player = 'man'
        print('\nYou are a', player, '\n')
        time.sleep(2)
        clear_screen()
        break
    elif player in ['2', 'woman', 'female', 'women', 'females']:
        player = 'woman'
        clear_screen()
        print('\nYou are a', player, '\n')
        break
    else:
        print('Input a valid option!\n\n')
        time.sleep(2)
        clear_screen()
    

male   = 1 #we give the variable 'male' the value of 1 / this is the first row of the list
female = 2 #we give the variable 'female' the value of 2 / this is the second row of the list


print('\n''Choose what you want to date:''\n')
print('1. Males              ''2. Females               ''3. Both''\n')



