'''Dice rolling simulator'''
import tkinter
from PIL import Image,ImageTk
import random

'''Basic setup'''
#building the window for the game
#initializing the tkinter to create window
dice_window = tkinter.Tk()

#window dimensions and placement position
dice_window.geometry('500x500+400+100')
dice_window.title("Dice game")

'''Window interface'''

#blank line on top for padding
spacing = tkinter.Label(dice_window,text="")
#push it into the window
spacing.pack()

'''labels'''
heading = tkinter.Label(dice_window,text="Dice game",fg="blue",bg='white',font='sans-serif')
heading.pack()

#images
dice_face = ['1.png','2.png','3.png','4.png','5.png','6.png']

#generate random image from the list of dice faces

dice_img = ImageTk.PhotoImage(Image.open(random.choice(dice_face)))

#label for placing image of dice face

dice_face_label = tkinter.Label(dice_window,image=dice_img)
dice_face_label.image = dice_img

#pack widget into window
dice_face_label.pack(expand=False)

'''end of labels'''

#rolling dice function
def roll_dice():
	dice_Image = ImageTk.PhotoImage(Image.open(random.choice(dice_face)))

	#update image
	dice_face_label.configure(image=dice_Image)

	dice_face_label.image = dice_Image

#adding button
button = tkinter.Button(dice_window,text="ROll doce",fg='blue',command=roll_dice)

#place button on window
button.pack(expand=True)
'''End of interface'''



#call the window continously refreshing
dice_window.mainloop()


print("working\n")