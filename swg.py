import random
from tkinter import *
#Window
root = Tk()
root.geometry('700x700')
root.configure(bg='black')
root.resizable(0,0)
root.title("Snake Water Gun - by Astin")
Label(root,text = "\n"+"Welcome"+'\n'+"To Play"+"\n"+"Snake,Water,Gun "+"\n"+"Don't worry the"+'\n'+"Computer won't"+"\n"+"cheat with tricks"+"\n"+"Choose wisely"+"\n"+":-)"+"\n"+"\n"+"\n"+"\n"+"When the space"+"\n"+" to see the"+"\n"+" results end"+"\n"+"End this page"+"\n"+"And"+"\n"+"Restart"+"\n"+"Happy Gaming"+"\n"+":-)"+"\n"+"\n", font = ('Bitstream Charter', 20, 'bold') ,fg = 'Black', bg = "yellow").place(bordermode='inside')
def snake():
    user_action = "snake"
    possible_actions = ["snake", "water", "gun"]
    computer_action = random.choice(possible_actions)
    if user_action == computer_action:
        label11 =Label(root,text = "Both players selected snake. It's a tie!", font = ('Bitstream Charter', 15, 'bold') ,fg = 'white', bg = "black")
        label11.pack()
    elif user_action == "snake":
        if computer_action == "water":
            label12 =Label(root,text = "Snake swims and bites Computer! You win!", font = ('Bitstream Charter', 15, 'bold') ,fg = 'light green', bg = "black")
            label12.pack()
        else:
            label13 =Label(root,text = "Snake is dead! You lost!", font = ('Bitstream Charter', 15, 'bold') ,fg = 'red', bg = "black")
            label13.pack()
def water():
    user_action = "water"
    possible_actions = ["snake", "water", "gun"]
    computer_action = random.choice(possible_actions)
    if user_action == computer_action:
        label21 =Label(root,text = "Both players selected water. It's a tie!", font = ('Bitstream Charter', 15, 'bold') ,fg = 'white', bg = "black")
        label21.pack()
    elif user_action == "water":
        if computer_action == "snake":
            label22 =Label(root,text = "Snake swims and bites you! You lost!", font = ('Bitstream Charter', 15, 'bold') ,fg = 'red', bg = "black")
            label22.pack()
        else:
            label23 =Label(root,text = "Gun drowned! You win!", font = ('Bitstream Charter', 15, 'bold') ,fg = 'light green', bg = "black")
            label23.pack()
def gun():
    user_action = "gun"
    possible_actions = ["snake", "water", "gun"]
    computer_action = random.choice(possible_actions)
    if user_action == computer_action:
        label31 =Label(root,text = "Both players selected gun. It's a tie!", font = ('Bitstream Charter', 15, 'bold') ,fg = 'white', bg = "black")
        label31.pack()
    elif user_action == "gun":
        if computer_action == "snake":
            label32 =Label(root,text = "Snake is dead! You win!", font = ('Bitstream Charter', 15, 'bold') ,fg = 'light green', bg = "black")
            label32.pack()
        else:
            label33 =Label(root,text = "Gun drowned! You lost!", font = ('Bitstream Charter', 15, 'bold') ,fg = 'red', bg = "black")
            label33.pack()
button1 = Button(root,text = 'Snake', font = ('Bitstream Charter', 15, 'bold') ,fg = 'indigo', bg = 'white', command= snake).pack(side=LEFT)
button2 = Button(root,text = 'Water', font = ('Bitstream Charter', 15, 'bold') ,fg = 'blue', bg = 'white', command= water).pack(side=LEFT)
button3 = Button(root,text = 'Gun', font = ('Bitstream Charter', 15, 'bold') ,fg = 'grey', bg = 'white', command= gun).pack(side=LEFT)  
def end():
    root.destroy()
Button(root,text = 'End', font = ('Bitstream Charter', 15, 'bold') ,fg = 'black', bg = 'white',command=end).pack(side=BOTTOM)
root.mainloop()
