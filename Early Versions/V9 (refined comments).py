#Theveenan Nirmalan
#Started Dec. 2,2018
#Finished Jan. 18,2019
#Final Assignment Kahoot



#Test cases that were used to make sure no errors occur
# COMMON INPUT CASES:
# "abc", "1", "0"
#Variables tested with these cases: 'questionsCount', 'correctAns', 'retry', 'listToEdit', 'usersAnswer', 'selectMode', 'continuation'
#                                   'questionsPreview'

# EXTREME INPUT CASES:
# "(blank)", " (space)", "-2", "ctrl"+"c"
#Variables tested with these cases: 'inputQuestion', 'questionsCount', 'correctAns', 'inputAnswer', 'listToEdit', 'retry', 'listToEdit',
#                                   'playerCount', 'usersAnswer, 'selectMode', 'continuation', 'questionsPreview'




#MODULES ARE IMPORTED
import time
import random


#FUNCTIONS ARE DEFINED

#This function is used to create questions that will be asked for the 'play game' mode.
def create_question():
    try:
        #User enters how many questions they want to create. A loop asking for all necessary inputs will run that many times.
        questionsCount=int(input("\n How many questions would you like to create?"))
        for x in range(questionsCount):
            #As data is inputted for each question, the data is appended to the list they belong to. Each question is organized by index for this program.
            print("\n Now editing question :",x,". all changes later on will be for question :",x)
            print("\n NOTE: REMEMBER THE ABOVE NUMBER, IT WILL BE YOUR QUESTINON REFERRAL INDEX"
                  "\n If you forget your question referral index number, you can still see all the questions and their indexes in the 'preview menu'\n")
            inputQuestion=input("Enter a question:")
            allLists[0].append(inputQuestion)
            print("\n You will now enter 4 possible answers for the above question. Make sure one of them is correct, because you will enter which one is correct after. \n")
            #Loop runs 4 times, asking the user to enter an answer. The answer is then added to its respective list index, within the 'allLists' list.
            for x in range(1,5):
                print("")
                inputAnswer=input("Enter a possible answer:")
                allLists[x].append(inputAnswer)

            correctAns=int(input("enter which answer number was the correct answer to the question"))
            while correctAns>4 or correctAns<1:
                #The user must enter a number from 1-4 to signify which of the 4 entered answers is the correct one. 
                print("Please enter a value between 1 and 4, this value represents which of the 4 possible answers provided, is correct.")
                correctAns=int(input("enter which answer number was the correct answer to the question"))
            allLists[5].append(correctAns)
            print("")
    except:
        print("Your entry is invalid, returning to main menu...")
        
#This function asks the user which question they want to edit,(by index referral) and then allows them to redfine all data for that index for each list. 
def edit_question():
    try:
        listToEdit=int(input("Which question number do you want to change? (Enter referral index for that question)"))
        #'newData' is a list that holds user entered data from this function until the user confirms they want to make these changes active
        newData=[]
        newQuestion=input("\n Enter NEW question for question")
        newData.append(newQuestion)
        print("You will now enter 4 possibe answers for this question. MAKE SURE one of them is correct and the rest are wrong.\n"
              "You will be prompted to select which possible answer is the correct answer to the question afterwards.")
        #Loop runs 4 times, so user can re-enter the 4 possible answers for the question
        for y in range(1,5):
              print("\n Creating new answer for answer",y)
              newQuestion=input("Enter NEW possible answer")
              newData.append(newQuestion)

        newCorrectAnswer=int(input("Which answer number was the correct answer to the question"))
        newData.append(newCorrectAnswer)
        confirmation=int(input("Are you sure you would like to make these changes? Press 1 to confirm :"))
        if confirmation==1:
            #If the user confirmed the changes made, this loop will redefine the indexes in each list with the new data provided.
            for x in range(6):
                allLists[x][listToEdit]=newData[x]

        else:
            print("cancelling question edit mode")
    #This except is for incase the user enters wrong data, they have the option to retry or return to main menu
    except:
        print("Your entries were invalid, you may have entered a letter or space where a number was required, or you entered a non existent question referral index.")
        retry=input("To retry press 1. Press any other key to return to main menu")
        #Input is 'string' data type so that all input is allowed and no error happens if the user enters a letter or blank.(Removes the need for extra 'try & except')
        if retry=="1":
            edit_question()
        else:
            print("\n Returning to main menu \n")


#This function allows the user to view stored questions and their indexes, for the purpose of referral.
def preview_questions():
    try:
        print("\n\nIf you want to see only one question and all its data, press 1. \n"
              "If you would like to view all questions and their referral indexes, press any other key. \n")
        questionsPreview=input(" : ")
        #This 'elif' block is here because the user can decide to view one sepecific question or all of them. 
        if questionsPreview=="1":
            previewQuestion=int(input("which question would you like to preview answers for?"))
            print("\n\nQuestion is: '",allLists[0][previewQuestion],"'",
                  "\n Answers: 1)",allLists[1][previewQuestion]+", 2)",allLists[2][previewQuestion]+", 3)",allLists[3][previewQuestion]+", 4)",
                  allLists[4][previewQuestion],"\n Correct answer is answer:",(allLists[5][previewQuestion])+")\n\n")
        else:
            for x in range(0,len(allLists[0])):
                print(x,"is referral index for, '"+(allLists[0][x])+"'")
            print("Those are all the questions stored, you can create more in the 'Create Questions' menu")
            
    except:

        print("Your entries were invalid, you may have entered a letter or space where a number was required, or you entered a non existent question referral index.")
        #If the user enters something invalid, they have the option to return to the main menu or restart
        retry=input("To retry press 1. Press any other key to return to main menu")
        if retry=="1":
            preview_questions()
        else:
            print("\n"
                  "Returning to main menu"
                  "\n")
            

#This function runs the quiz game mode and processes all points systems and game play mechanics
def play_game1(highscore):
    try:
        #Input is 'string' data type so that all input is allowed and no error happens if the user enters a letter or blank.(Removes the need for extra 'try & except')
        playerCount=input("Press 1 for 1 player, or any other key for 2 players :")
        #All the code for this 'if' statement, is for 1 player quiz mode
        if playerCount==("1"):
            correct=0
            incorrect=0
            totalPoints=0
            questionsAsked=[]
            #Loop runs for length of questions list so that all questions are asked at least once and only once.
            for x in range(0,(len(allLists[0]))):
                #Random 'questionIndex' created to randomly choose which question to ask
                questionIndex=random.randint(0,len(allLists[0])-1)
                while questionIndex in questionsAsked:
                    questionIndex=random.randint(0,len(allLists[0])-1)
                questionsAsked.append(questionIndex)
                #'play_game2' function is called, which will ask the question and take the user answer input and determine if correct or wrong. Boolean is returned
                playerAnswer=play_game2(questionIndex,playerCount)
                if playerAnswer:
                                totalPoints+=1
                                correct+=1
                else:
                                incorrect+=1
                print("you have",totalPoints,"points")
            print("\n CONGRATULATIONS \n You finished with",totalPoints,"points!!! \n You got",correct,"correct and",incorrect,"incorrect \n\n")
            
            try:
                highscore=int(highscore)
                if totalPoints>highscore:
                        highscore=totalPoints
                        print("THIS IS YOUR NEW HIGH SCORE")
                        return highscore
                else:
                        print("You didn't beat your highscore"
                              "but maybe next time!")
            except:
                print("No previous record has been recognized, which means THIS IS YOUR NEW HIGH SCORE \n\n")
                highscore=totalPoints
                
            return highscore
        #All the code under this 'else' statement is for 2 player quiz mode
        else:
            player1points=0
            player2points=0
            questionsAsked=[]
            #Loop will as many times as length of questions list so every question is answered
            for x in range(0,len(allLists[0])):
                #Random number(index) is chosen, this random number will decide which question is asked. This way, the questions are in random order
                questionToAsk=random.randint(0,len(allLists[0])-1)
                while questionToAsk in questionsAsked:
                    questionToAsk=random.randint(0,len(allLists[0])-1)
                questionsAsked.append(questionToAsk)
                #This 'elif' block is just a way of alternating turns between players
                if x%2==1:
                    print("\nGET READY PLAYER 1!\n")
                    time.sleep(1)
                    #This function will ask the question and return boolean depending if the user got it right or wrong.
                    player1Answer=play_game2(questionToAsk,playerCount)
                    if player1Answer:
                        player1points+=1
                        print("\n Player 1 has",player1points,"points\n")
                    #This 'else' statement is used if the player gets the question wrong, the other player can steal the question. 
                    else:
                        print("\n\n YOU CAN STEAL THE POINT PLAYER 2!")
                        time.sleep(1)
                        player2Answer=play_game2(questionToAsk,playerCount)
                        if player2Answer:
                            player2points+=1
                            print("Yay for player 2, you stole the point! \n")
                        else:
                            print("OOF, better luck next time player 2.. \n")
                        
                else:
                    print("\nPLAYER 2 TURN!\nLets go!\n")
                    time.sleep(1)
                    player2Answer=play_game2(questionToAsk,playerCount)
                    if player2Answer:
                        player2points+=1
                        print("\n Player 2 has",player2points,"points\n")
                    else:
                        print("\n\n PLAYER 1 CAN STEAL!")
                        time.sleep(1)
                        player1Answer=play_game2(questionToAsk,playerCount)
                        if player1Answer:
                            player1points+=1
                            print("Hooray for player 1, you got the steal! \n")
                        else:
                            print("Aww, sorry player 1 but you lost the steal... \n")
                            
    #Once the loop of questions breaks, this code will show points and who won the game    
            print("\n\n\n\n\n G A M E")
            if player1points>player2points:
                print("PLAYER 1 WINS!")
            elif player2points>player1points:
                print("PLAYER 2 WINS!")
            else:
                print("Tie game...")
            print("\n Player 1 finished with",player1points,"points")
            print("Player 2 finished with",player2points,"points")
    except:
            print("There was a problem while attempting to run Kahoot, Play game mode. Try restarting program.")
        

            

#This function is only called from the 'play_game1' function. This function exists so that this code isn't repeated.
#This function passes in an index to determine which question to ask & it passes in the playercount variable. It returns boolean depending if user is correct/incorrect.
def play_game2(questionIndex,playerAmount):
    try:
                #This print statement prints the question.
                print(allLists[0][questionIndex])
                print(allLists[5][questionIndex])
                time.sleep(2)
                #This for loop runs 4 times and prints a possible answer each time. (It's in loop to reduce code)
                for x in range(1,5):
                    print("?-",allLists[x][questionIndex])
                usersAnswer=input("which answer is correct (1,2,3 or 4)?")
                if usersAnswer==(allLists[5][questionIndex]):
                    print("")
                    print("YAY CORRECT")
                    return True
                else:
                    #This 'elif' block is here because if 2 players, the game won't give away the correct answer. (because steals are available if they get it wrong)
                    if playerAmount=="1":
                        print("\n Wrong. the correct answer was",allLists[5][questionIndex])
                    else:
                        print("\n Wrong.")
                    return False
    except:
        print("A problem occured while running Kahoot, try recreating your questions and play again")
        
     
        
        
#This function writes text lines to a text file on the computer, each list within the this program will be written as its own line                        
def save_game():
    try:

        savedFile=open("gameSaveFile.txt","w")
        #This loop will run 6 times and write each of the 6 lists as its own line within the text file.
        for x in range(6):
            listToSave=str(allLists[x])
            savedFile.write(listToSave)
            savedFile.write("\n")
        try:
            #This try-and-except runs to try and save the 'highscore' value. It may be non-existent and that is why it in a try and except for no possible errors. 
            saveHighscore=str(highscore)
            savedFile.write(saveHighscore)
            savedFile.write("\n")
            print("\n\nFile saved, recover this same game data next time through 'load game' option\n")
        except:
            print("(No highscore has been found so no highscore will be saved)\n\n")
        savedFile.close
    except:
        print("There was a problem trying to save your file. Your entered data may have been invalid. Returning to main menu..")
    

#This function reads text lines from a saved file on the computer, each line is saved to its own list.
def load_game():
    try:
        savedFile=open("gameSaveFile.txt","r")
        fileLines=savedFile.readlines()
        #'newAllLists' will store each line from the text file as a list within itself. ('newAllLists' is 2 dimensional list)
        newAllLists=[]
        #This loop will run 6 times to read each of the 6 lines and save each line as its own list. (6 lists)
        for x in range(6):
            #The process for reading the text file, is adding a blank element to the list, so it is an existent index.
            newAllLists.append("")
            newAllLists[x]=fileLines[x].replace("[","").replace("]","").replace("'","").replace(", ",",").replace("\n","")
            #The program will then redefine this index with a line from the text file. Unecessary items such as brackets and spaces are removed from this long string.
            newAllLists[x]=newAllLists[x].split(",")
            #The string is then split up into a list, by dividing the string into a new list index at each comma
            print(allLists[x])
        highscore=fileLines[6]
        print("\n File loaded, save game data next time through 'save game' option")
        savedFile.close
        return newAllLists,highscore
    
    except:
        #If no files were stored on the computer, this message is displayed
        print("\n\n No save files could be found, please try again another time when data has been saved from different sessions \n")


#This function only prints instructions for the user to read
def instructions():
    print("\n\n\nINSTRUCTIONS\n Kahoot is a competitive quiz game. One person can quiz themself against the computer or 2 players can go head to head.\n"
          "The questions are pre-defined by a user, and can be saved to the computer if wanted. (Regularly saving is advised) \n"
          "Questions that were saved previously can be loaded as well. \n"
          "You can edit and preview questions that are stored for use. \n"
          "Every single question has a 'referral index'. This index is given to you when you first create the question.\n"
          "This referral index is what you will use in the program to reference this question if you ever want to preview or edit it.\n"
          "If you forget a question's referral index, DONT WORRY, just go to the 'preview questions' menu and you will have the option to view all questions and indexes.\n"
          "\nWhen you go to the 'Play game' mode, you can select to play 1 player or 2 players:\n"
          "If you play 1 player mode, you will be asked questions and have to try to answer them correctly be entering which answer number is correct\n"
          "For example, if you think the 2nd shown answer is the correct answer to the question, press '2' and 'enter'\n"
          "At the end, you will be told your highscore and how many you got correct and incorrect\n"
          "If  you play 1 player mode, the screen will tell which player's turn it is to go. You must decide who will be player 1 and player 2\n"
          "If it is your turn, you will read the question and enter the number of the answer you think is correct. \n"
          "For example, if you think hte 3rd shown answer is the correct answer to the question, press '3' and 'enter' \n"
          "If you get the question wrong, the other player can take the steal. Which means they can do the same question right after.\n"
          "If they get it right, they get the point. If they get it wrong, there is no consequence and it goes back to their turn. \n"
          "This goes until the game is over and one of the players is declared winner! \n\n\n")

    
#This function is created as a tool to prevent the user from trying to crash the program. It is only used at the end of the main program when the user quits. 
def infinite_loop():
          
    while True:
        try:
            time.sleep(1)
        except:
            infinite_loop()
    


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                   IMPORTANT NOTE FOR PROGRAM READERS
#
#This program uses 2 dimensional lists. (Lists within lists)
#The main list used in this program is called 'allLists'
#This list contains the other 6 lists for: questions, 1st answer, 2nd answer, 3rd answer, 4th answer, and correct answer.
#Each of these 6 lists are used VERY PROMINENTLY in the program, and each of them is their own index WITHIN the 'allLists' list.
#Therefore, it is MANDATORY that before you read or edit any program details, you must KNOW EACH list index within the 'allLists' list, and what that list is used for.

#allLists[0]= QUESTIONS LIST
#allLists[1]= ANSWER 1 LIST
#allLists[2]= ANSWER 2 LIST
#allLists[3]= ANSWER 3 LIST
#allLists[4]= ANSWER 4 LIST
#allLists[5]= CORRECT ANSWER LIST

#Each of these index's list, has their own elements which are used by the program to print out things such as questions and answers.
#
#
#     Below is some fake code. This code can help you visualize how this 2 dimensional list is used in the program
#
### questions=["what is name","what is age","what is the time"]
### answer1=["bob","15","12:00"]
### answer2=["bobby","99","time to sleep"]
### answer3=["Goofy","1","time to get a watch"]
### answer4=["Theveenan","16","daytime"]
### correctAnswer=["4","4","2"]
### allLists=[]
### allLists.append(questions)
### allLists.append(answer1)
### allLists.append(answer2)
### allLists.append(answer3)
### allLists.append(answer4)
### allLists.append(correctAnswer)
#
#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------



#LISTS AND VARIABLES ARE DEFINED
allLists=[["what is name","what is age","what is the time"],["bob","15","12:00"],["bobby","99","time to sleep"],["Goofy","1","time to get a watch"],
          ["Theveenan","16","daytime"],["4","4","2"]]
highscore=0



#MAIN PROGRAM
#
#
#All functions (game pages) are called from this main menu.
continuation="1"
print("\n\n\n KAHOOT \n\n FULLSCREEN IS ADVISED\n")

while continuation=="1":
    #'continuation' allows the program to run, if user redefines it (which means they wanted to exit), the program will close
     try:
        for x in range(40):
            print("_",end="")
        print("\n\n Welcome to Kahoot! Main Menu")
        selectMode=int(input("\n What would you like to do?\n Press 1 to Create Questions\n Press 2 to Edit Questions"
                             "\n Press 3 to Preview Questions\n Press 4 to Play Game \n Press 5 for Save File \n Press 6 for Load Game"
                             "\n Press 7 for Instructions  <-(Start here if you're new)\n\n  Or press any other key to Power Off\n\n:"))
        if selectMode==1:
            create_question()
        elif selectMode==2:
            edit_question()
        elif selectMode==3:
            preview_questions()
        elif selectMode==4:
            highscore=play_game1(highscore)
        elif selectMode==5:
            save_game()
        elif selectMode==6:
            allLists,highscore=load_game()
        elif selectMode==7:
          instructions()
        else:
            print("Unvailable function")
     except:
         try: 
            continuation=input("Are you sure you want to exit kahoot? press 1 for no, or any other key for yes")
         except:
             continuation="0"
        
print("\n\n Powering off...")

#This infinite function is called so that errors cannot occur if user tries to (ex. 'ctrl'+'c')
infinite_loop()
          
        

           


