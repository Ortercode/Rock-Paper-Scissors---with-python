import random
# Python Woooo
# Rock, Paper, Scissors with rude computer
# A variation of Rock Paper Scissors

# Rock Paper scissors but computer learns
# How to beat you as you play 



# Based on random int computer picks a number



#while(usrChoice != 'r' or usrChoice != 's' or usrChoice != 'p'):
#      usrChoice = input("Enter correctly. ")


    


def check_who_wins(choice, computerChoice):
        if(choice == 'r'):
            userChoice = "rock"
            if(computerChoice == 'p'):
                compChoice = "paper"
                print("You chose: ", userChoice)
                print("Computer chose: ", compChoice)
                print("Computer Won ! ")
                go_again()
            else:
                compChoice = "scissors"
                print("You chose:  ", userChoice)
                print("Computer chose: ", compChoice)
                print("You Won !")
                go_again()
        elif(choice == 'p'):
            userChoice = "paper"
            if(computerChoice == 's'):
                compChoice = "scissors"
                print("You chose: ", userChoice)
                print("Computer chose: ", compChoice)
                print("Computer Won ! ")
                go_again()
            else:
                compChoice = "rock"
                print("You chose: ", userChoice)
                print("Computer chose: ", compChoice)
                print("You won !")
                go_again()
        else:
            userChoice = "scissors"
            if(computerChoice == 'r'):
                compChoice = "rock"
                print("You chose: ", userChoice)
                print("Computer chose: ", compChoice)
                print("Computer Won !")
                go_again()
            if(computerChoice == 'p'):
                compChoice = "paper"
                print("You chose: ", userChoice)
                print("Computer chose: ", compChoice)
                print("You won !")
                go_again()
                
            
        
          
   
def check_if_draw (choice, computerChoice):
        if(choice == 'r'):
            userChoice = "rock"
        if(choice == 'p'):
            userChoice = "paper"
        if(choice == 's'):
            userChoice = "scissors"
            
            #Computer's coice 
        if(computerChoice == 'r'):
            compChoice = "rock"
        if(computerChoice == 'p'):
            compChoice = "paper"
        if(computerChoice == 's'):
            compChoice = "scissors"
            
            
        if(choice == computerChoice):
            print("You chose :", userChoice)
            print("Computer Chose : ", compChoice)
            print("Draw :0")
            go_again()
        else:
            check_who_wins (choice, computerChoice)
            
            go_again()
 
          
        
        
def validate_input(choice, computerChoice):
    wrongChoices = 0
    if(choice == 'r' ):
        check_who_wins(choice, computerChoice)
    elif(choice == 'p'):
        check_who_wins(choice, computerChoice)
    elif(choice == 's'):
        check_who_wins(choice, computerChoice)
    elif(choice == 'end'):
        print("bye")
    else:
        while(choice != 'r ' or choice != 's' or choice != 'p' or choice != "end"):
            wrongChoices += 1
            choice3 = input("Enter correctly ")
            choice2 = choice3.lower()
            if(wrongChoices > 5):
                print("")
                print("Hey man I'm a computer I don't get paid for this shit. Would you like to play or not ? ")
                print("")
           #     endMe = input("If not, just press any key to stop ")
           #     print("Bye")
           #     break
              
                wrongChoices = 0
                
                
            if(choice2 == 'r' or choice2 == 's' or choice2 == 'p'):
                wrongChoices = 0
                break
        choice = choice2.lower()
        print("")
        check_who_wins(choice, computerChoice)
    

def explain_game():    
    
    choices = ['r', 'p', 's']

    randomNumber = random.randint(0, 2)
    compChoice = choices[randomNumber]
    print("Rock, Paper, Scissors - with slightly rude computer ")
    print("___________________________________________")
    print(" ")
    print("'r' for Rock")
    print("'p' for Paper")
    print("'s' for Scissors")
    
    choice1 = input("I've already made my choice.  It's your turn ")
    
    choice = choice1.lower()
    
    computerChoice = choices[randomNumber]
    print("")
    validate_input(choice, computerChoice)
   
    
        
def go_again():
    print("")
    numberOfFailedInputs = 0
    print(" ")
    print("************************")
    print("Would you like to go again ?")
    answer1 = input("y/n ( yes or no ) ")
    answer = answer1.lower()
    print("")
    print("************************")
    print("")
    if(answer == 'y'):
        print("")
        explain_game()
    elif(answer == 'n'):
        print("Goodbye :)")
        #compChoice = choices[randomNumber]
    else:
        if(answer != 'y' or answer != 'n' or answer != 'end'):
            while(answer != 'y' or answer != 'n'):
                answer2 = input("enter correctly ")
                numberOfFailedInputs += 1 
                if(numberOfFailedInputs > 5):
                    print("I give up")
                    print("")
                    endMeNow = input("Just press a random key to end this program ")
                    break
                    answer = 'end'
                if(answer2 == 'y' or answer2 == 'n'):
                    answer = answer2
                    break
        
            
         
            if(answer == 'y'):
                print(" ")
                explain_game()
            else:
                print("goddbye")
                print("")
                endMe = input("Enter any key to exit ")
            
         
                   
                    
     
explain_game()




# Python - Define functions first then call them
# First functions to be called - below 



#Thank you God