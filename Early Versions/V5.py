#Modules are imported
import time
import random

#Functions are defined

def create_question():
    try:
        questionsCount=int(input("how many questions would you like to create?"))
        for x in range(questionsCount):
            print("")
            print("now editing question",x,". all changes later on will be for question",x)
            inputQuestion=input("enter a question")
            questions.append(inputQuestion)
            print("")
            inputAnswer1=input("enter an answer")
            answer1.append(inputAnswer1)
            print("")
            inputAnswer2=input("enter an answer")
            answer2.append(inputAnswer2)
            print("")
            inputAnswer3=input("enter an answer")
            answer3.append(inputAnswer3)
            print("")
            inputAnswer4=input("enter an answer")
            answer4.append(inputAnswer4)
            print("")
            correctAns=int(input("enter which answer number was the correct answer to the question"))
            while correctAns>4 or correctAns<1:
                print("Please enter a value between 1 and 4, this value represents which of the 4 possible answers provided, is correct.")
                correctAns=int(input("enter which answer number was the correct answer to the question"))
            correctAnswer.append(correctAns)
            print("")
    except:
        print("Your entry is invalid, returning to main menu...")
        

def edit_question():
    print("")
    listToEdit=int(input("which question number do you want to change"))
    print("")
    newQuestion=input("re enter question for question")
    print("")
    newAnswer1=input("re enter answer for answer 1 of question")
    print("")
    newAnswer2=input("re enter answer for answer 2 of question")
    print("")
    newAnswer3=input("re enter answer for answer 3 of question")
    print("")
    newAnswer4=input("re enter answer for answer 4 of question")
    print("")
    newCorrectAns=int(input("which answer number was the correct answer to the question"))
    print("...") 
    confirmation=int(input("Are you sure you would like to make these changes? Press 1 to confirm"))
    if confirmation==1:
        questions[listToEdit]=newQuestion
        answer1[listToEdit]=newAnswer1
        answer2[listToEdit]=newAnswer2
        answer3[listToEdit]=newAnswer3
        answer4[listToEdit]=newAnswer4
        correctAnswer[listToEdit]=newCorrectAns
    else:
        print("cancelling question edit mode")

def preview_questions():
    previewQuestion=int(input("which question would you like to preview answers for?"))
    print("Question is '",questions[previewQuestion],"'",
          "\n Answers are: 1)",answer1[previewQuestion]+", 2)",answer2[previewQuestion]+", 3)",answer3[previewQuestion]+", 4)",answer4[previewQuestion],
          "\n Correct answer is answer",(correctAnswer[previewQuestion])+")")
            


def play_game1(highscore):
    try:
        playerCount=input("Press 1 for 1 player, or any other key for 2 players :")
        if playerCount==("1"):
            correct=0
            incorrect=0
            totalPoints=0
            questionsAsked=[]
            print(highscore)
            for x in range(0,(len(questions))):
                questionToAsk=random.randint(0,len(questions)-1)
                while questionToAsk in questionsAsked:
                    questionToAsk=random.randint(0,len(questions)-1)
                questionsAsked.append(questionToAsk)
                print(questions[questionToAsk])
                print(correctAnswer[questionToAsk])
                time.sleep(1)
                print("answer 1: ",answer1[questionToAsk])
                print("answer 2: ",answer2[questionToAsk])
                print("answer 3: ",answer3[questionToAsk])
                print("answer 4: ",answer4[questionToAsk])
                usersAnswer=input("which answer is correct (1,2,3 or 4)?")
                if usersAnswer==(correctAnswer[questionToAsk]) or usersAnswer in (correctAnswer[questionToAsk]):
                                totalPoints+=1
                                correct+=1
                else:
                                print("wrong. the correct answer was",correctAnswer[questionToAsk])
                                incorrect+=1
                print("you have",totalPoints,"points")
            print(""
                  "CONGRATULATIONS")
            print("You finished with",totalPoints,"points!!!")
            print("you got",correct,"correct and",incorrect,"incorrect")
            try:
                highscore=int(highscore)
                if totalPoints>highscore:
                        highscore=totalPoints
                        print("THIS IS YOUR NEW HIGH SCORE")
                else:
                        print("You didn't beat your highscore"
                              "but maybe next time!")
            except:
                print("No previous record has been recognized, which means THIS IS YOUR NEW HIGH SCORE")
                highscore=totalPoints
                
            return highscore
        
        else:
            player1points=0
            player2points=0
            questionsAsked=[]
            for x in range(0,len(questions)):
                questionToAsk=random.randint(0,len(questions)-1)
                while questionToAsk in questionsAsked:
                    questionToAsk=random.randint(0,len(questions)-1)
                questionsAsked.append(questionToAsk)
                if x%2==1:
                    print("PLAYER 1 TURN")
                    print("Get ready!")
                    time.sleep(1)
                    player1Answer=play_game2(questionToAsk)
                    if player1Answer:
                        player1points+=1
                        print("you have",player1points,"points")
                        print("")
                    else:
                        print("PLAYER 2 CAN STEAL!")
                        time.sleep(1)
                        player2Answer=play_game2(questionToAsk)
                        if player2Answer:
                            player2points+=1
                            print("Hooray, you got the steal")
                        else:
                            print("OOF, you lost the steal..")
                        
                else:
                    print("PLAYER 2 TURN")
                    print("Get ready!")
                    time.sleep(1)
                    player2Answer=play_game2(questionToAsk)
                    if player2Answer:
                        player2points+=1
                        print("you have",player2points,"points")
                        print("")
                    else:
                        print("PLAYER 1 CAN STEAL!")
                        time.sleep(1)
                        player1Answer=play_game2(questionToAsk)
                        if player1Answer:
                            player1points+=1
                            print("Hooray, you got the steal")
                        else:
                            print("OOF, you lost the steal..")
            print("\n"
                  "\n")
            print("G A M E")
            if player1points>player2points:
                print("PLAYER 1 WINS!")
            elif player2points>player1points:
                print("PLAYER 2 WINS!")
            else:
                print("Tie game...")
            print("Player 1 finished with",player1points,"points")
            print("Player 2 finished with",player2points,"points")
    except:
            print("There was a problem while attempting to run Kahoot, Play game mode. Try restarting program.")
        

            
                       
def play_game2(questionIndex):
    
            print(questions[questionIndex])
            print(correctAnswer[questionIndex])
            time.sleep(1)
            print("answer 1: ",answer1[questionIndex])
            print("answer 2: ",answer2[questionIndex])
            print("answer 3: ",answer3[questionIndex])
            print("answer 4: ",answer4[questionIndex])
            usersAnswer=input("which answer is correct (1,2,3 or 4)?")
            if usersAnswer==(correctAnswer[questionIndex]) or usersAnswer in (correctAnswer[questionIndex]):
                print("")
                print("YAY CORRECT")
                return True
            else:
                print("")
                print("Wrong. the correct answer was",correctAnswer[questionIndex])
                return False
        
     
        
        
                        
def save_game():
    try:
        saveQuestions=str(questions)
        saveAnswer1=str(answer1)
        saveAnswer2=str(answer2)
        saveAnswer3=str(answer3)
        saveAnswer4=str(answer4)
        saveCorrectAnswer=str(correctAnswer)
        savedFile=open("gameSaveFile.txt","w")
        savedFile.write(saveQuestions)
        savedFile.write("\n")
        savedFile.write(saveAnswer1)
        savedFile.write("\n")
        savedFile.write(saveAnswer2)
        savedFile.write("\n")
        savedFile.write(saveAnswer3)
        savedFile.write("\n")
        savedFile.write(saveAnswer4)
        savedFile.write("\n")
        savedFile.write(saveCorrectAnswer)
        savedFile.write("\n")
        try:
            saveHighscore=str(highscore)
            savedFile.write(saveHighscore)
            savedFile.write("\n")
            print("File saved, recover this same game data next time through 'load game' option")
        except:
            print("(no highscore has been found so no highscore will be saved)")
        savedFile.close
    except:
        print("There was a problem trying to save your file, returning to main menu..")
    

#this function isnt allowing lists to be carried outside the function so i just copied the entire function below in the select mode section
def load_game():
    try:
        savedFile=open("gameSaveFile.txt","r")
        fileLines=savedFile.readlines()
        fileQuestions=fileLines[0].replace("[","").replace("]","").replace("'","").replace(", ",",").replace("\n","")
        answers1=fileLines[1].replace("[","").replace("]","").replace("'","").replace(", ",",").replace("\n","")
        answers2=fileLines[2].replace("[","").replace("]","").replace("'","").replace(", ",",").replace("\n","")
        answers3=fileLines[3].replace("[","").replace("]","").replace("'","").replace(", ",",").replace("\n","")
        answers4=fileLines[4].replace("[","").replace("]","").replace("'","").replace(", ",",").replace("\n","")
        correctAnswers=fileLines[5].replace("[","").replace("]","").replace("'","").replace(" ","").replace(", ",",").replace("\n","")
        highscore=fileLines[6]
        print(fileQuestions)
        print(answers1)
        print(answers2)
        print(answers3)
        print(answers4)
        print(correctAnswers)
        nquestions=fileQuestions.split(",")
        nanswer1=answers1.split(",")
        nanswer2=answers2.split(",")
        nanswer3=answers3.split(",")
        nanswer4=answers4.split(",")
        ncorrectAnswer=correctAnswers.split(",")
        print("File loaded, save game data next time through 'save game' option")
        
            
        savedFile.close
        return nquestions,nanswer1,nanswer2,nanswer3,nanswer4,ncorrectAnswer,highscore
    except:
        print("No save files could be found, please try again another time when data has been saved from different sessions")
    
    

#list is defined

questions=["what is name","what is age","what is the time"]
answer1=["bob","15","12:00"]
answer2=["bobby","99","time to sleep"]
answer3=["Goofy","1","time to get a watch"]
answer4=["Theveenan","16","daytime"]
correctAnswer=["4","4","2"]
highscore=0



#main program
continuation="1"
print("KAHOOT \n \n \n")
while continuation=="1":
    try:
        print("Welcome to Kahoot! Main Menu")
        selectMode=int(input("What would you like to do?\n Press 1 to create questions, \n Press 2 to edit questions, \n Press 3 to preview questions, \n Press 4 to play game, \n Press 5 for save file, \n Press 6 for load game, \n Or press any other key to power off"))
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
            questions,answer1,answer2,answer3,answer4,correctAnswer,highscore=load_game()
        else:
            print("unvailable function")
    except:
        continuation=input("Are you sure you want to exit kahoot? press 1 for no, or any other key for yes")
        
print("Powering off...")        
           


