import os                               #lets us use the system commands
import keyboard                         #lets us use the keyboard
import time                             #allows your program to use time / example: time.sleep(2) will make the program wait for 2 seconds
import random                           #allows your program to use random / example: random.randint(1, 10) will return a random number between 1 and 10

def clear_screen():                     #function to clear the screen that we will call multiple times / this is the reason we imported the 'os module'
    os.system('clear')                  #this command clears the screen
clear_screen()                          #calling t1he function to clear the screen



print('\n''Welcome to the Dating App!') #print the welcome message
time.sleep(2)                           #wait for 2 seconds
clear_screen()                          #clear the screen


people = [['Markus' , 'Anton' , 'Benjamin' , 'Erik' , 'Burak', 'Dess' , 'Roger' , 'Roman' , 'Sunny' , 'Hassan'] ,   
          ['Hiba' , 'Morgane','Vanessa']]                          #a list of people looking for love
male   = ['man','male','men','males', 1]                           #we give the variable different values through the usage of a list
female = ['woman','female','women','females', 2]                   #we give the variable different values through the usage of a list
player = ''                                                        #we give the variable 'player' the value of an empty string

while True:                                                        #a while loop that will keep running until the user inputs a valid option
    print('\nViable options in this Demo are "1. Men" and "2. Women" for simplicity.\n') #print the message
    player = input('Choose your sex:\n\n').lower()                 # Convert input to lowercase for case-insensitive comparison
    if player in ['1', 'man', 'male', 'men', 'males']:             #if the user inputs a valid option
        player = 'man'                                             #we give the variable 'player' the value  
        clear_screen()                                             #clear the screen
        print('\nYou are a', player)                               #print the message
        time.sleep(2)                                              #wait for 2 seconds
        break                                                      #break the loop
    elif player in ['2', 'woman', 'female', 'women', 'females']:   #if the user inputs a valid option
        player = 'woman'                                           #we give the variable 'player' the value
        clear_screen()                                             #clear the screen
        print('\nYou are a', player)   
        time.sleep(2)                      #print the message
        break                                                      #break the loop
    else:                                                          #if the user inputs an invalid option
        print('\n Input a valid option! \n\n')                         #print the message
        time.sleep(2)                                              #wait for 2 seconds
        clear_screen()                                             #clear the screen
    


    print('\nYou are a', player, '\n')  
print('\n''Choose what do you want to date:''\n')
print('1. Men              ''2. Women               ''3. Both''\n')
player = ''                                                        #we give the variable 'player' the value of an empty string
while True:                                                        #a while loop that will keep running until the user inputs a valid option
    player = input('\n').lower()                 # Convert input to lowercase for case-insensitive comparison
    if player in ['1', 'man', 'male', 'men', 'males']:             #if the user inputs a valid option
        player = 'man'                                             #we give the variable 'player' the value  
        print('\nYou are a', player, '\n')                         #print the message
        time.sleep(2)                                              #wait for 2 seconds
        clear_screen()                                             #clear the screen
        break                                                      #break the loop
    elif player in ['2', 'woman', 'female', 'women', 'females']:   #if the user inputs a valid option
        player = 'woman'                                           #we give the variable 'player' the value
        clear_screen()                                             #clear the screen
        print('\nYou are a', player, '\n')                         #print the message
        break                                                      #break the loop
    else:                                                          #if the user inputs an invalid option
        print('Input a valid option!\n\n')                         #print the message
        time.sleep(2)                                              #wait for 2 seconds
        clear_screen()                                             #clear the screen

