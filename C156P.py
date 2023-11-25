from tkinter import*
from PIL import ImageTk, Image

root= Tk()
root.title("Endless Dice Game")
root.geometry("600x400")
root.configure(background="orange")

img = ImageTk.PhotoImage(Image.open("dice.jpg"))

Player1 = Label(root,text="Player 1", bg="red", fg="white")
Player1.place(relx=0.1, rely=0.3, anchor=CENTER)

Player2 = Label(root, text="Player 2", bg="red", fg="white")
Player2.place(relx=0.9, rely=0.3, anchor=CENTER)

Player1_score = Label(root, bg="royal blue", fg="white")
Player1_score.place(relx=0.1, rely=0.4, anchor=CENTER)

Player2_score = Label(root, bg="royal blue", fg="white")
Player2_score.place(relx=0.9, rely=0.4, anchor=CENTER)

random_dice = Label(root, bg="chocolate1", fg="white")
random_dice.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()