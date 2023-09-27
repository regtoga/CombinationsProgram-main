import itertools

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


class fileArchitect():
    """This class holds a bunch of functions for manipulaing files"""

    #Define Self variables
    def __init__(self):
        self.localfilename = ""
    
    def Create_File(self, locationfromuser: str, filenamefromuser: str, answerstxt: list, mewanttxt: int) -> str:
        """Creates a file using the arguments, and makes a global name for the file so other blocks can access it"""
        try:
            if filenamefromuser == "" and locationfromuser == "":
                #create a file object
                Author = open(f"./{len(answerstxt)}_answers_equled_{mewanttxt}.txt", "x")
                self.localfilename = f".\{len(answerstxt)}_answers_equled_{mewanttxt}.txt"
                #print(f"Created file {len(answerstxt)}_equled_{mewanttxt}.txt in Downloads")
                return f"Created file {len(answerstxt)}_answers_equled_{mewanttxt}.txt in whatever location you ran this."
            else:
                Author = open(f"{locationfromuser}{filenamefromuser}.txt", "x")
                self.localfilename = f"{locationfromuser}{filenamefromuser}.txt"
                #print(f"Created file{filenamefromuser}.txt in {locationfromuser}")
                return f"Created file{filenamefromuser}.txt in {locationfromuser}"
        except:
            print("Failed to create file because one with the same name allready exists")
            return "Critical Failure"
        #Close Author object
        Author.close()

    #function containging code about how to write a file   
    def Write_File(self, answerstxt: list) -> str:
        """Using a list parametere this function will write it to the file defined in the create file function"""
        try:
            Author = open(self.localfilename, "w")
            Author.write(str(answerstxt)) 
            Author.close()
            return "Success!"
        except:
            print("Something Went wrong when writing the file")
            return "Critical Failure"

    #function containging code about how to read a file
    def Read_File(self) -> str:
        """Returns a string containing all the information on the file"""
        try:
            Author = open(self.localfilename, "r")
            _contents = Author
            Author.close()
            return _contents
        except:
            print("Something Went wrong when reading the file")
            return "Critical Failure"

# makes FileArchitect object
archie = fileArchitect()

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

                    #SHOULD check to see if the answer is allready in the list and if it is it SHOULD remove the last known version of it:
                    
                    #checks if anything in answers is == to anything allready in totalComp
                    for j in range(0, len(answers)):
                        if str(answers[j]) == str(totalComp):
                            exists = True
                    # if the answer was allready in the answers list it will skip appending it to the answers list and not print the result
                    if exists == False:
                        #Makes a templist for a reason that i cant remember, esentially i couldnt get an item to simply append to the answers list
                        #instead it forwhatever reason always shared the same memory space. After making a new list and appending it instead it actually worked
                        TempList = []

                        for items in range(0, len(totalComp)):
                            TempList.append(totalComp[items])

                        #adds the computed answer into the answers list
                        answers += [TempList]

                        #outputs the answers
                        print(f"these numbers: {str(totalComp)}added up to {str(total)}.")
                    #resets exists to false so that by default it is false
                    exists = False

        # starts asking questions about creating and handling files
        export = input("Do you want to export results into a text file? (Y/N)")
        if export == "Y" or export == "y":
            default = input("Do you want to use default file location and name? (Y/N)")

            locationfromuser = ""
            filenamefromuser = ""

            if export == "N" or export == "n":
                locationfromuser = input("Enter a location for your txt file: EX(D:\windows folders\Downloads\) :")
                filenamefromuser = input("Enter the name you want for you text file: EX(banan) becomes banan.txt: ")

            print(archie.Create_File(locationfromuser, filenamefromuser, answers, mewant))
            print(archie.Write_File(answers))

        exit()

    elif x == "stop":
        print("stopping!")
        exit()

