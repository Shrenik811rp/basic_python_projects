from tkinter import*

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
#place at which text is placed in window
font_label.place(x=120,y=0)


word_label= Label(root,text="Mango",font = ('verdana',40,"bold"),bg="black",fg="blue")

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
instruction_label.place(x=250,y=400)
"""end textlabels"""

"""input"""

word_entry = Entry(root, font= ('verdana',20,"bold"),bd=5,justify='center')
word_entry.place(x=250,y=350)

#focus_set() ->we sont have to click on input to type
#we start typing automatically without clicking blank input box
word_entry.focus_set()
"""end input"""



#opens new main window and refreshes page continously in a loop
root.mainloop()