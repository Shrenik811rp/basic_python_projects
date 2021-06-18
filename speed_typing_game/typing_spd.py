from tkinter import*

root= Tk()

'''dimension of window : 800x 400
window opens at coordinates:x=400 y=100'''
root.geometry('800x600+400+100')


root.configure(bg='black')
root.title("typing speed")

#replace tkinter symbol with random icon
root.iconbitmap('icon.ico')


"""text labels"""


font_label = Label(root,text="Typing speed game",font = ('verdana',30,"bold"),bg="black",fg="blue")

font_label.place(x=200,y=0)


word_label= Label(root,text="Mango",font = ('times new roman',40,"italic bold"),bg="black",fg="blue")

word_label.place(x=330,y=200)

"""end textlabels"""

"""input"""

word_entry = Entry(root, font= ('arial',20,"bold"),bd=5,justify='center')
word_entry.place(x=250,y=300)

#focus_set() ->we sont have to click on input to type
#we start typing automatically without clicking blank input box
word_entry.focus_set()
"""end input"""


#opens new main window and refreshes page continously in a loop
root.mainloop()