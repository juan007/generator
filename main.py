# Title: Generator
# Author: Juan Roldan

import random

#user input function
def getUserInput():
    #flag used to validate user input
    validated = False

    #make variables global(they all start as strings)
    numCompliments = ""
    compliment = ""
    numAdjectives = ""

    while(validated == False):
        numCompliments = input("\nPlease enter number of compliments to generate: ")
        #Validate number of compliments input, digit higher than 1
        if(numCompliments.isdigit() and int(numCompliments)>=1):
            numCompliments = int(numCompliments)
            validated = True

            compliment = input("Please enter person's name: ")
            #Validate compliment input, different to empty string
            if(compliment!=""):
                validated = True
                
                numAdjectives = input("Please enter number of adjectives: ") 
                #Validate number of adjectives input, digit between 1 and 3
                if(numAdjectives.isdigit() and int(numAdjectives)>=1 and int(numAdjectives)<=3):
                    numAdjectives = int(numAdjectives)
                    validated = True
                else:
                    print("Error: The number of adjectives must be a whole number between 1 and 3")
                    validated = False

            else:
                print("Error: The Person's name cannot be empty")
                validated = False
        else:
            print("Error: The number of compliment must be a whole number higher than 0")
            validated = False
        
            
    return numCompliments, compliment, numAdjectives

#function that generates 1 random adjective
def getAdjective():
    randomNumber = random.randint(1,10) 
    
    #return Random adjective
    if(randomNumber==1):
        return "Nice";
    elif(randomNumber==2):
        return "Smart"
    elif(randomNumber==3):
        return "Grateful"
    elif(randomNumber==4):
        return "Colorful"
    elif(randomNumber==5):
        return "Beautiful"
    elif(randomNumber==6):
        return "Trustworthy"
    elif(randomNumber==7):
        return "Admirable"
    elif(randomNumber==8):
        return "Intelligent"
    elif(randomNumber==9):
        return "Cool"
    elif(randomNumber==10):
        return "Awesome"

#function that generates 1 random noun
def getNoun():
    randomNumber = random.randint(1,6) 
    
    #return Random noun
    if(randomNumber==1):
        return "Person!"
    elif(randomNumber==2):
        return "Individual!"
    elif(randomNumber==3):
        return "Creature!"
    elif(randomNumber==4):
        return "Charecter!"
    elif(randomNumber==5):
        return "Human!"
    elif(randomNumber==6):
        return "Memeber of society!"

#Get Adjective(s) string
def getAdjectiveString(numAdjectives):
    strAdjective=""
    
    #compose adjective string with the random adjectives
    for n in range(0,numAdjectives):
        strAdjective += getAdjective()+" "
    
    return strAdjective

#Function that outputs the compliments
def printCompliments(numCompliments,compliment,numAdjectives):
    #print the number of compliments the user asked for
    for n in range(0,numCompliments):
        print(compliment.upper(),"is a",getAdjectiveString(numAdjectives)+getNoun().upper())

def main():
    #variable value that will never change
    flag=0
    #while loop will go on since flag never changes
    while(flag==0):
        numCompliments,compliment,numAdjectives = getUserInput()
        
        #output result
        printCompliments(numCompliments,compliment,numAdjectives)
main()
