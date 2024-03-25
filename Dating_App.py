#================================================================
#importing libraries that we will use in the program
import os               #lets us use the system commands
import keyboard                         #lets us use the keyboard
import time                             #allows your program to use time / example: time.sleep(2) will make the program wait for 2 seconds
import random                           #allows your program to use random / example: random.randint(1, 10) will return a random number between 1 and 10
#================================================================
#function to clear the screen, we will call in later in the program
def clear_screen():     #function to clear the screen that we will call multiple times / this is the reason we imported the 'os module'
    os.system('clear')  #this command clears the screen
clear_screen()          #calling t1he function to clear the screen
#================================================================
#creating global variables that we will use in the program
player = ''
partnergender = ''
partner = ''
#================================================================
#a list of partners looking for love
partners = (['Marius', 'Panton', 'Ben 10', 'Edison', 'Burg', 'Desmond', 'Rolland', 'Romeo', 'Sandy', 'Haschwald'],
            ['Himber', 'Kilimari', 'Lady Gaga', 'Mariana', 'Merry', 'Katty', 'Perry', 'Samanta', 'Clover', 'Luna'])         
#================================================================
print('\n''Welcome to the Dating App!') #print the welcome message
time.sleep(2)                           #wait for 2 seconds
clear_screen()                          #clear the screen
#================================================================
#while loop that lets us choose what gender we are                                                       
while True:                                                        
    print('\nViable options in this Demo are "1. Men" and "2. Women" for simplicity.\n') #print the message
    player = input('Choose your sex:\n\n').lower()                 # Convert input to lowercase for case-insensitive comparison
    if player in ['1', 'man', 'male', 'men', 'males']:             #if the user inputs a valid option
        player = 'man'                                             #we give the variable 'player' the value  
        clear_screen()                                             #clear the screen
        print('\nYou are a', player + '.')                         #print the message
        time.sleep(2)                                              #wait for 2 seconds
        break                                                      #break the loop
    elif player in ['2', 'woman', 'female', 'women', 'females']:   #if the user inputs a valid option
        player = 'woman'                                           #we give the variable 'player' the value
        clear_screen()                                             #clear the screen
        print('\nYou are a', player + '.')                         #print the message
        time.sleep(2)                                              #print the message
        break                                                      #break the loop
    else:                                                          #if the user inputs an invalid option
        print('\nInput a valid option! \n')                        #print the message
        time.sleep(2)                                              #wait for 2 seconds
        clear_screen()                                             #clear the screen
#================================================================
#while loop that lets us choose what gender we want to date                  
while True:           
    print('\n''Choose what do you want to date:''\n')
    print('1. Men              ''2. Women               ''3. Both''\n')  
    partnergender = input().lower()                                        # Convert input to lowercase for case-insensitive comparison
    if partnergender in ['1', 'man', 'male', 'men', 'males']:               #if thelid o user inputs a vaption     
        malepartners = ', '.join(map(str, partners[0]))                     #we output to the screen the first row of the list 'partners' with commas inbetween them
        clear_screen() 
        print('\nYou have decided to date men.')
        time.sleep(2) 
        clear_screen()
        print('\nThese are your potential male partners:', malepartners, '\n' )         
        break                                                               #break the loop
    elif partnergender in ['2', 'woman', 'female', 'women', 'females']:            #if the user inputs a valid option
        femalepartners = ', '.join(map(str, partners[1]))                   #we output to the screen the second row of the list 'partners' with commas inbetween them
        clear_screen() 
        print('\nYou have decided to date women.')
        time.sleep(2) 
        clear_screen()
        print('\nThese are your potential female partners:', femalepartners, '\n' )
        break           
    elif partnergender in ['3', 'women and men', 'men and women', 'females and males', 'males and females', 'both', 'all']: #if the user inputs a valid option
        malepartners = ', '.join(map(str, partners[0]))                   #we output to the screen the second row of the list 'partners' with commas inbetween them
        femalepartners = ', '.join(map(str, partners[1])) 
        clear_screen() 
        print('\nYou have decided to date both genders.')
        time.sleep(2) 
        clear_screen()
        print('\nThese are your potential partners:\n\n', malepartners , '\n' ,femalepartners, '\n' )
        break                                                          #break the loop
    else:                                                                   #if the user inputs an invalid option
        print('\nInput a valid option!\n')                                  #print the message
        time.sleep(2)                                                       #wait for 2 seconds
        clear_screen()                                                      #clear the screen
#================================================================
#while loop that lets us choose which exact male partner do we wanna date                         
while partnergender in ('1', 'man', 'male', 'men', 'males'): 
    print('Chose the person you want to date from the list above: \n')
    partner = input().title()
    if player in ('man'):                                                                                                           
        if partner in ['Marius', 'Panton', 'Ben 10', 'Edison', 'Burg', 'Desmond', 'Rolland', 'Romeo', 'Sandy', 'Haschwald']:                                    
            clear_screen()                                                                     
            print('You have chosen to date', partner + '.')                                           
            time.sleep(2)
            clear_screen()     
            print('\nHe takes you upstairs and starts...\n')
            time.sleep(2)
            print('..slurping on that juicy..\n')     
            time.sleep(2)
            print('...watermelon juice while watching netflix with you.\n') 
            time.sleep(2)                                                            
            break                                                                          
        else:                                                                                 
            print('\nInput a valid option!\n')                                                 
            time.sleep(2)                                                                      
            clear_screen()        
    if player in ('woman'):                                                                   
        if partner in ['Marius', 'Panton', 'Ben 10', 'Edison', 'Burg', 'Desmond', 'Rolland', 'Romeo', 'Sandy', 'Haschwald']:                                    
            clear_screen()                                                                     
            print('You have chosen to date', partner + '.')                                           
            time.sleep(2)
            clear_screen()     
            print('\nHe takes down his pants...\n')
            time.sleep(2)
            print('..you go down on your knees..\n')     
            time.sleep(2)
            print('...and you start sewing his loose button.\n')  
            time.sleep(2)                                                           
            break                                                                          
        else:                                                                                 
            print('\nInput a valid option!\n')                                                 
            time.sleep(2)                                                                      
            clear_screen()
#================================================================
#while loop that lets us choose which exact female partner do we wanna date                            
while partnergender in ('2', 'woman', 'female', 'women', 'females'): 
    print('Chose the person you want to date from the list above: \n')
    partner = input().title()
    if player in ('man'):                                                                                                           
        if partner in ['Himber', 'Kilimari', 'Lady Gaga', 'Mariana', 'Merry', 'Katty', 'Perry', 'Samanta', 'Clover', 'Luna']:                                    
            clear_screen()                                                                     
            print('You have chosen to date', partner + '.')                                           
            time.sleep(2)
            clear_screen()     
            print('\nShe ties her hair in a ponytail...\n')
            time.sleep(2)
            print('..removes her bra and starts..\n')     
            time.sleep(2)
            print('...washing it in the sink.\n') 
            time.sleep(2)                                                            
            break                                                                          
        else:                                                                                 
            print('\nInput a valid option!\n')                                                 
            time.sleep(2)                                                                      
            clear_screen()        
    if player in ('woman'):                                                                   
        if partner in ['Himber', 'Kilimari', 'Lady Gaga', 'Mariana', 'Merry', 'Katty', 'Perry', 'Samanta', 'Clover', 'Luna']:                                    
            clear_screen()                                                                     
            print('You have chosen to date', partner + '.')                                           
            time.sleep(2)
            clear_screen()     
            print('\nShe pushes you on the bed...\n')
            time.sleep(2)
            print('..goes down on you and removes..\n')     
            time.sleep(2)
            print('...your socks so she can wash them.\n')  
            time.sleep(2)                                                           
            break                                                                          
        else:                                                                                 
            print('\nInput a valid option!\n')                                                 
            time.sleep(2)                                                                      
            clear_screen()