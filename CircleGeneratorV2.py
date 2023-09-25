import itertools
import re

#initializes variables
ListOfNumbers = []
totalComp = []
answers = []
x = 0
total = 0
mewant = 0
exists = False

#special variable that is just for the guy who owns the program
HardList = [62, 100, 82, 78, 61, 101, 73, 64, 216, 98, 80, 65]

#function used to append "x" to the end of a list.
def accumulator():
    
    ListOfNumbers.append(x)
    
    print(ListOfNumbers)
    print(len(ListOfNumbers))

#essentially an infinite loop
while x != "stop":
    #applies an input to the variable x
    x = input("Enter a number ('stop' to stop, 'calc' to calculate, 'list' to use predefined list): ")

    if x != "stop" and x != "calc" and x != "list":
        #while "x" is not equle to stop or calc all inputs will be entered into a list though the accumulator funciton
        accumulator()

    elif x == "list":
        for i in HardList:
            ListOfNumbers.append(i)
        print(ListOfNumbers)
        print(len(ListOfNumbers))

    elif x == "calc":
        # show that the fuction is doing something
        print("calculating: ")

        # make a list of all combinations of each number put into the list, then print the first item in list.
        combinations = list(itertools.combinations_with_replacement(ListOfNumbers, 6))
        #print(combinations[0])
        
        #ask what sum of the numbers user is looking for
        mewant = input("what sum are you looking for? ")

        # iterate though all the list items in combinations so i can do math on each on of the list items.
        for i in combinations:
            #reset total to 0 after every full iteration of the loop for acurate couting
            total = 0

            totalComp.clear()

            # iterate though all the sencond layer of list items so that i can do math on each of the individual numbers.
            for ele in range(0, len(i)):
                #appends all numbers used in the accumulation of the total variable for further analysis
                totalComp.append(i[ele])

                #adds all numbers in seccond layer of list together
                total += int(i[ele])

                #depending on if the total equals the one the user wants it will explain what it got and how it got it.
                if int(total) == int(mewant):

                #------------------------------------------------------------------
                    #SHOULD check to see if the answer is allready in the list and if it is it SHOULD remove the last known version of it.
                    
                    for j in range(0, len(answers)):
                        #print("")
                        #print(answers[j])
                        #print(totalComp)
                        #print("")
                        if str(answers[j]) == str(totalComp):
                            exists = True
                    if exists == False:
                        #add the list of numbers to the answers list

                        TempList = []

                        for items in range(0, len(totalComp)):
                            TempList.append(totalComp[items])

                        answers += [TempList]

                        #outputs the answers
                        print("these numbers: " + str(totalComp) + " added up to " + str(total) + ".")
                    
                    exists = False
                #-------------------------------------------------------------------

            # printing total value
            # print("Sum of all list: ", total)

        print(len(combinations))

        exit()

    elif x == "stop":
        print("stopping!")
        exit()