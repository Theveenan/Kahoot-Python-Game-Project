import time

#fucntions are defined

def create_question():
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
        correctAnswer.append(correctAns)
        print("")
        

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
    print("Question is",questions[previewQuestion],"answers are",answer1[previewQuestion],answer2[previewQuestion],answer3[previewQuestion],answer4[previewQuestion],"correct answer is answer",correctAnswer[previewQuestion])

def play_game():
    correct=0
    incorrect=0
    totalPoints=0
    print(questions)
    for x in range(0,(len(questions))):
        print(questions[x])
        print(correctAnswer[x])
        time.sleep(3)
        print("answer 1: ",answer1[x])
        print("answer 2: ",answer2[x])
        print("answer 3: ",answer3[x])
        print("answer 4: ",answer4[x])
        usersAnswer=input("which answer is correct (1,2,3 or 4)?")
        intUserAnswer=int(usersAnswer)
        if usersAnswer==(correctAnswer[x]) or usersAnswer in (correctAnswer[x]):
                        totalPoints+=1
                        correct+=1
        else:
                        print("wrong. the correct answer was",correctAnswer[x])
                        incorrect+=1
        print("you have",totalPoints,"points")
    print(""
          "CONGRATULATIONS")
    print("You finished with",totalPoints,"points!!!")
    print("you got",correct,"correct and",incorrect,"incorrect")
    try:
        if totalPoints>highscore:
            highscore=totalPoints
            print("THIS IS YOUR NEW HIGH SCORE")
        else:
            print("You didn't beat your highscore"
                  "but maybe next time!")
    except:
        print("No previous record has been recognized, which means THIS IS YOUR NEW HIGH SCORE")
                        
def save_game():
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
    except:
        print("(no highscore has been found so no highscore will be saved)")
    savedFile.close
    

#this function isnt allowing lists to be carried outside the function so i just copied the entire function below in the select mode section
def load_game():
    savedFile=open("gameSaveFile.txt","r")
    fileLines=savedFile.readlines()
    fileQuestions=fileLines[0].replace("[","").replace("]","").replace("'","").replace(", ",",")
    answers1=fileLines[1].replace("[","").replace("]","").replace("'","").replace(", ",",")
    answers2=fileLines[2].replace("[","").replace("]","").replace("'","").replace(", ",",")
    answers3=fileLines[3].replace("[","").replace("]","").replace("'","").replace(", ",",")
    answers4=fileLines[4].replace("[","").replace("]","").replace("'","").replace(", ",",")
    correctAnswers=fileLines[5].replace("[","").replace("]","").replace("'","").replace(" ","").replace(", ",",")
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
    savedFile.close
    return nquestions,nanswer1,nanswer2,nanswer3,nanswer4,ncorrectAnswer
    
    
    

#list is defined

questions=[]
answer1=[]
answer2=[]
answer3=[]
answer4=[]
correctAnswer=[]


#main program
continuation=1
while continuation==1:
    try:
        selectMode=int(input("what would you like to do?\n Press 1 to create questions, \n Press 2 to edit questions, \n Press 3 to preview questions, \n Press 4 to play game, \n Press 5 for save file, \n Press 6 for load game, \n Or press any other key to power off"))
        if selectMode==1:
            create_question()
        elif selectMode==2:
            edit_question()
        elif selectMode==3:
            preview_questions()
        elif selectMode==4:
            play_game()
        elif selectMode==5:
            save_game()
        elif selectMode==6:
            questions,answer1,answer2,answer3,answer4,correctAnswer=load_game()
        else:
            print("unvailable function")
    except:
        print("Error")
        continuation=int(input("are you sure you want to exit kahoot? press 1 for no, or any other key for yes"))
        
           


