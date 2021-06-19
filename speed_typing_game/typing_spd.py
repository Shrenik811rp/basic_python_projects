#import for gui
from tkinter import*

#import for notification window
from tkinter import messagebox
# generate random numbers
import random

# perform math operation
import math

# create or initialize window
root= Tk()

'''dimension of window : 800x 400
window opens at coordinates:x=400 y=100'''
root.geometry('800x600+400+100')

#the bg for whole window in black
root.configure(bg='black')
#window title
root.title("Typing speed")

#replace tkinter symbol with random icon
root.iconbitmap('icon.ico')



"""variables"""
#variable for counting score
score_val = 0
#variable for counting time
time_val = 60
#count acts as index var for "text" array
count = 0

#empty string
slide = ''
#number of words you got wrong
wrong=0

words_per_min = 0

words=["Melon","Grapes","Mango","Apple","Orange","Pineapple","Television","Application","Laptop","Location","Accord","convince","financial","territory","undertake","assert","scheme","manifest","resource","contempt","plead","distinction","entertain","generate","constitute","property","policy","intend","commit"]
""""""


"""text labels"""

#function to create typing text
def word_slide():
    #declaring global variables
    global count,slide
    #string array which containes game name
    text = "Typing Speed Game"

    #if value of count becomes greater than value of text
    if(count>=len(text)):
        #set index to first alphabet
        count =0
        #start from empty string
        slide = ''
    #add each alphabet from text array based on index value count    
    slide += text[count] 
    #increase count
    count += 1
    font_label.configure(text=slide)
    #time after which loop will repeat
    font_label.after(150,word_slide)


#features of text heading
font_label = Label(root,text='',font = ('BankGothic Md BT',40,"bold"),bg="black",fg="red")
#call function to create sliding text heading
word_slide()

#shuffles the elements in the array so we get differnt words each time
random.shuffle(words)
#place at which text is placed in window
font_label.place(x=120,y=0)


word_label= Label(root,text=words[1],font = ('verdana',40,"bold"),bg="black",fg="blue")

word_label.place(x=330,y=250)


score_label = Label(root,text="Score",font = ('BankGothic Lt BT',30,"bold"),bg="black",fg="blue")
score_label.place(x=20,y=100)


score_label_count = Label(root,text=score_val,font = ('BankGothic Lt BT',30,"bold"),bg="black",fg="blue")
score_label_count.place(x=70,y=180)


time_left_label = Label(root,text="Time left",font = ('BankGothic Lt BT',30,"bold"),bg="black",fg="blue")
time_left_label.place(x=570,y=100)

time_left_label_count = Label(root,text=time_val,font = ('BankGothic Lt BT',30,"bold"),bg="black",fg="blue")
time_left_label_count.place(x=640,y=180)


instruction_label = Label(root,text="Type word and hit Enter",font = ('BankGothic Lt BT',20,"bold"),bg="black",fg="grey")
instruction_label.place(x=250,y=450)
"""end textlabels"""

"""input"""

word_entry = Entry(root, font= ('verdana',20,"bold"),bd=5,justify='center')
word_entry.place(x=250,y=350)

#focus_set() ->we sont have to click on input to type
#we start typing automatically without clicking blank input box
word_entry.focus_set()
"""end input"""


"""get data inputted"""
#when enter pressed the data entered is outputted
def game(event):
    global score_val,wrong,words_per_min

    if time_val == 60:
        #calling timer countdown function once enter pressed
        timer_func()
    instruction_label.configure(text=' ')
    if word_entry.get() == word_label['text']:
        print("Correct")
        score_val += 1
        score_label_count.configure(text=score_val)
        print(f"Score is {score_val}.")
    else:
        wrong +=1
        print("Wrong")
        print(f"wrong answers {wrong}")
    words_per_min += 1    
    #rearrange the words in the array so elements keep changing index   
    random.shuffle(words)  
    #display random words from array 
    word_label.configure(text=words[0])        
    #to clear output console
    word_entry.delete(0,END)
""""""

"""timer function"""

def timer_func():
    global time_val,score_val,wrong,words_per_min

    if time_val > 11:
        pass
    else:
        #when timer is less than 10 it changes to red
        time_left_label_count.configure(fg='red')    
    #countdown timer
    if time_val > 0:
        #decrement timer
        time_val -=1
        #display decrement operation
        time_left_label_count.configure(text=time_val)
        #rate at which decrement happens 1000ms that is 1s
        time_left_label_count.after(1000,timer_func)

    #once reached 0 display results    
    else:

        #display end results 
        instruction_label.configure(text="Correct words : {}\n Wrong words : {} \n Total Score : {}\n Words per min : {}\n Accuracy : {} %".format(score_val,wrong,score_val-wrong, math.floor((words_per_min/60)*100),math.floor(score_val/(words_per_min)*100) ))

        #reset the counter to blue when restart
        time_left_label_count.configure(fg='blue')

        #create a notification window to ask player to continue or quit
        notification_box = messagebox.askretrycancel("Notification window","To play again click \'Retry\'")  

        #if player wants to retry 
        if notification_box == True:
            #reset all variables
            score_val = 0
            #variable for counting time
            time_val = 60
            #count acts as index var for "text" array
            count = 0
            #number of words you got wrong
            wrong=0
            words_per_min = 0
            time_left_label_count.configure(text=time_val)
            word_label.configure(text=words[2])
            score_label_count.configure(text=score_val
            )
        #else close the window    
        else:
            root.destroy()

             
""""""
#the entered data is stored when "Return/ENter" key pressed
root.bind('<Return>',game)
#opens new main window and refreshes page continously in a loop
root.mainloop()