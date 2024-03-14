
#a list of subjects looking for love / 'dimensions' is a list that contains information that cannot be changed
dimension = [['Markus' , 'Anton' , 'Benjamin' , 'Erik' , 'Burak', 'Dess' , 'Roger' , 'Roman' , 'Sunny' , 'Hassan'] ,
             ['Hiba' , 'Morgane','Vanessa']] 

male = 1
female = 2

print('Choose your sex:')

row1 = 0 #we give the variable 'row1' the value of 0 / this is the first row of the list
row2 = 1 #we give the variable 'row2' the value of 1 / this is the second row of the list

for i in range(len(dimension[row1])): #for each number in the range of the length of the list
    print(dimension[row1][i]) #print out the name in the list




#for sublist in dimension: #for each sublist in the list / there are a total of 2 sublists
 #   for name in sublist: #for each name in the list
  #      if name == 'Hassan': #if the name is Morgane
   #         print('Choose the lover you want to be') #prints out the name of the person you want to be
    #        break  #breaks the loop
