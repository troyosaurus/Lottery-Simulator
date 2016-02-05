print("\t\tWelcome to the California Lottery Number Generator") # Instructions
print("\t\t\tSuperLottoPlus Lottery Program")

# Required Python Modules to Import
import random

winning_numbers = random.sample(range(1,47),5)
winning_mega_number = random.sample(range(1,27),1)
counter = 1
mega_counter = 0

print("")
print("Enter your 5 numbers between 1 and 47 and see if you win any cash")
print("")
regular_lottonums = []		#List to store regular lottery numbers
mega_num = []			#List to store mega numbers

while counter < 6:
    print("Please type in the ", counter," number")
    i = input("--> ")
    print('Your selected number is', i)
    
    if((i not in regular_lottonums) and (1 <= int(i) <= 47)):
        regular_lottonums.append(i)
        counter += 1
    else:
        print("Please enter a valid, non-duplicate number between 1 and 47!")

while mega_counter < 1:
    print("Please enter a valid mega number")
    j = input("--> ")
    print('Your selected mega number is', j)

    if((i not in mega_num) and (1 <= int(j) <= 27)):
        mega_num.append(j)
        mega_counter += 1
    else:
        print("Please enter a valid, non-duplicate number between 1 and 27!")
          
print('Your randomly chosen numbers are',regular_lottonums)
print('Your randomly chosen mega number is', mega_num)
print('The winning regular numbers are', winning_numbers)
print('The winning mega number is', winning_mega_number)
	
    # # check if i is unique and has a value from 1 to 50
    # # and is an integer, otherwise don't append               
 
n = 0
for i in regular_lottonums:
    if i in winning_numbers:
        n += 1
        print("You got %d numbers right out of 6" % n)
    if n < 3:
        print("Bad luck!! You have not won this time")
        break
    elif n == 3:
        print("Congratulations!!! You have won $9")
    elif n == 4:
        print("Congratulations!!! You have won $76")
    elif n == 5:
        print("Congratulations!!! You have won $39214")
    elif n == 6:
        print("Congratulations!!! You have won the JACKPOT")
