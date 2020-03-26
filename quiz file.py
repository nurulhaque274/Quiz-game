import tkinter
from tkinter import *
import random
import tkinter.messagebox

Questions = [
    "How many Keywords are there in C Programming language?",
    "Which of the following functions takes A console Input in Python?",
    "Which of the following is the capital of India?",
    "Which of The Following is must to Execute a Python Code?",
    "The Taj Mahal is located in?",
    "The append Method adds value to the list at the?",
    "Which of the following is not a costal city of india?",
    "Which of The following is executed in browser(client side)?",
    "Which of the following keyword is used to create a function in Python?",
    "To Declare a Global variable in python we use the keyword?",
]

Answers = [
    ["23","32","33","43",],
    ["get()","input()","gets()","scan()",],
    ["Mumbai","Delhi","Chennai","Lucknow",],
    ["TURBO C","Py Interpreter","Notepad","IDLE",],
    ["Patna","Delhi","Benaras","Agra",],
    ["custom location","end","center","beginning",],
    ["Bengluru","Kochin","Mumbai","vishakhapatnam",],
    ["perl","css","python","java",],
    ["function","void","fun","def",],
    ["all","var","let","global",],
]

Correct_Answers = [1,1,1,3,3,1,0,2,2,3]

user_answer = []



#here we use random function
indexes = []

#Gen function is not predefined function  we use coding
def gen():
    global indexes

#loop is used for whenever value of index is not less than 5
    while(len(indexes) < 5):
        x = random.randint(0,9)
#here if loop is used for the value of indexes can not repeat again
        if x in indexes:
            continue
        else:
            indexes.append(x)


def Result(score):
    labelQuestions.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    labelresulttext = Label(
        root,
        font = ("Consolas",24),
    )
    labelresulttext.pack(pady=(50,10))
    if score >= 20:
        labelresulttext.configure(text="You Are Excellent !!")
    elif score >= 15 and score < 20 :
        labelresulttext.configure(text="GOOD JOB !!")
    else:
        labelresulttext.configure(text="You Should Work Hard !!")
        

    

#this function for calculate marks
def calculate():
    global indexes,user_answer,Correct_Answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == Correct_Answers[i]:
#score is used for mark and 5 is the marks of each questions
            score += 5
        x += 1

    print("score :- " +str(score),"/ 25")
    Result(score)
    

#here we added pop result
    tkinter.messagebox.showinfo("Final Result",score)



ques = 1
def selected():
    global radiovar,user_answer
    global labelQuestions,r1,r2,r3,r4
    global ques
#get is used to fetch a value from  radiobutton which value user enter
    x = radiovar.get()
    user_answer.append(x)
#if radivar is not write here so previous value of answer are show
    radiovar.set(-1)
    if ques < 5:
        labelQuestions.config(text=Questions[indexes[ques]])
        r1['text'] = Answers[indexes[ques]][0]
        r2['text'] = Answers[indexes[ques]][1]
        r3['text'] = Answers[indexes[ques]][2]
        r4['text'] = Answers[indexes[ques]][3]
        ques += 1
    else:
        print(indexes)
        print(user_answer)
        
        
        calculate()
    








def StartQuiz():
    global labelQuestions,r1,r2,r3,r4
    labelQuestions = Label(
        root,
        text = Questions[indexes[0]],
        font = ("Consolas",24),
        width = 500,
        justify = ("center"),
        background = "#ffffff",
#wraplength means if the size of word is above the 400 hundred then word starts newlines  
        wraplength = 400,
    )
    labelQuestions.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
#-1 is used for there is no default value occure during if press radiobutton
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = Answers[indexes[0]][0],
        font = ("Times",16),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = Answers[indexes[0]][1],
        font = ("Times",16),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = Answers[indexes[0]][2],
        font = ("Times",16),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = Answers[indexes[0]][3],
        font = ("Times",16),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)
    
    
    
        




        
    
def StartIspressed():

#destroy is used for delete front page and go to next page
    
    labelimage.destroy()     
    labeltext.destroy()
    labelinstruction.destroy()
    labelRules.destroy()
    btnStart.destroy()
#here gen is used to call the functins
    gen()

#StartQuiz is used for call function
    StartQuiz()     

root = tkinter.Tk()
root.title("Quiz")
root.geometry("700x600")

#(#ffffff) is used for white color photo background

root.config(background="#ffffff")  
 
#resizable is used for do not minimize or maximize the window
root.resizable(0,0)
image1 = PhotoImage(file="acedamy.png")

#this label is used for adding Logo
labelimage = Label(
    root,
    image = image1,
    background = "#ffffff",
)
labelimage.pack()   

#this label is used for application name
labeltext = Label(
    root,
    text = "Quiz Application",
    font=("Comic sabs MS",18,"bold"),
    background = "#ffffff",
)
labeltext.pack()

image2 = PhotoImage(file ="start1.png")

#this is used for start button
btnStart = Button(
    root,
    image = image2,

#relief & border is used for trim the white portion of start button
    
    relief = FLAT,          
    border = 0,
    background = "#ffffff",
    command = StartIspressed,
)

btnStart.pack()

#for instruction
labelinstruction = Label(
    root,
    text = "Click Start Once You Are Ready",
    background = "#ffffff",
    font = ("Consolas",20),

#justify is used for to start instructions at the center
    
    justify = "center",            
)

labelinstruction.pack()

#this for Rules of Quiz

labelRules = Label(
    root,
    text = "This Quiz Contains 10 Questions \nOnce you Choose The Option That Will be Your Final Choice.",
    width = 100,
    height = 40,
    background = "#ffffff",
    font = ("Times",16),
    
)

labelRules.pack()


root.mainloop()
