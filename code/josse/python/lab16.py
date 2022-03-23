
# def win_logic():
#     if button1["text"] == button2["text"] == button3["text"]:
#         print("row 1 win")
#     elif button4["text"] == button5["text"] == button6["text"]:
#         print("you win")

#     elif button7["text"] == button8["text"] == button9["text"]:
#         print("you win")

#     elif button1["text"] == button4["text"] == button7["text"]:
#         print("you win")

#     elif button2["text"] == button5["text"] == button8["text"]:
#         print("you win")

#     elif button3["text"] == button6["text"] == button9["text"]:
#         print("you win")

#     elif button1["text"] == button5["text"] == button9["text"]:
#         print("you win")
#     elif button3["text"] == button5["text"] == button7["text"]:
#         print("you win")


# from tkinter import *
# from tkinter import ttk

# root = Tk()
# root.title("josse perez")

# frm = ttk.Frame(root, padding=200)
# frm.grid()
# ttk.Label(frm, text="Random Photo Generator").grid(column=100, row=800)
# ttk.Button(frm, text="Click here for random picture",
#            command=image).grid(column=100, row=900)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=100, row=2000)
# root.mainloop()

# --------------------------------------------------------------------------------------------
from tkinter import *
import tkinter
import image
import random

# user_token = random.choice(["X", "O"])

# myFont = font.Font(family='Comic-sans')

# photo = PhotoImage(file=r"")
# def token(nums):

# def winner(result):
#     if button1 == button2 == button3 == player.token:
#             return player.token
#     elif button4 == button5 == button6 == player.token:
#             return player.token
#     elif button == button == button == player.token:
#             return player.token
#     elif button == button == button == player.token:
#         return player.token
#     elif button == button == button == player.token:
#         return player.token
#     else:
# return None


def win_logic():
    if button1["text"] == button2["text"] == button3["text"] != '':
        print("row 1 win")
    elif button4["text"] == button5["text"] == button6["text"] != '':
        print("you win")

    elif button7["text"] == button8["text"] == button9["text"] != '':
        print("you win")

    elif button1["text"] == button4["text"] == button7["text"] != '':
        print("you win")

    elif button2["text"] == button5["text"] == button8["text"] != '':
        print("you win")

    elif button3["text"] == button6["text"] == button9["text"] != '':
        print("you win")

    elif button1["text"] == button5["text"] == button9["text"] != '':
        print("you win")
    elif button3["text"] == button5["text"] == button7["text"] != '':
        print("you win")


# Function created for game logic
# user_token = " "


# X variable determins turn.
x = 1
player_1 = []
player_2 = []


def game(button):

    global x, user_token
    global player_1, player_2

    if button == 1:
        if x % 2 == 0:
            user_token = 'X'
            player_1.append(button)
            print(player_1)

        else:
            user_token = 'O'
            player_2.append(button)
            print(player_2)

        button1.config(text=user_token)
        x = x+1

    if button == 2:
        if x % 2 == 0:
            user_token = 'X'
            player_1.append(button)
            print(player_1)

        else:
            user_token = 'O'
            player_2.append(button)
            print(player_2)

        button2.config(text=user_token)
        x = x+1

    if button == 3:
        if x % 2 == 0:
            user_token = 'X'
            player_1.append(button)
            print(player_1)

        else:
            user_token = 'O'
            player_2.append(button)
            print(player_2)

        button3.config(text=user_token)
        x = x+1

    if button == 4:
        if x % 2 == 0:
            user_token = 'X'
            player_1.append(button)
            print(player_1)

        else:
            user_token = 'O'
            player_2.append(button)
            print(player_2)

        button4.config(text=user_token)
        x = x+1

    if button == 5:
        if x % 2 == 0:
            user_token = 'X'
            player_1.append(button)
            print(player_1)

        else:
            user_token = 'O'
            player_2.append(button)
            print(player_2)

        button5.config(text=user_token)
        x = x+1

    if button == 6:
        if x % 2 == 0:
            user_token = 'X'
            player_1.append(button)
            print(player_1)

        else:
            user_token = 'O'
            player_2.append(button)
            print(player_2)

        button6.config(text=user_token)
        x = x+1

    if button == 7:
        if x % 2 == 0:
            user_token = 'X'
            player_1.append(button)
            print(player_1)

        else:
            user_token = 'O'
            player_2.append(button)
            print(player_2)

        button7.config(text=user_token)
        x = x+1

    if button == 8:
        if x % 2 == 0:
            user_token = 'X'
            player_1.append(button)
            print(player_1)

        else:
            user_token = 'O'
            player_2.append(button)
            print(player_2)

        button8.config(text=user_token)
        x = x+1

    if button == 9:
        if x % 2 == 0:
            user_token = 'X'
            player_1.append(button)
            print(player_1)

        else:
            user_token = 'O'
            player_2.append(button)
            print(player_2)

        button9.config(text=user_token)
        x = x+1
    win_logic()
    print(f'"{button1["text"]}"')


root = Tk()
root.title("josse perez 'python mini-capstone'")

# label variable creates the header on tkinter
label1 = Label(text="player 1: x", font="times 20", bg="black", fg="red")
label1.grid(row=0, column=1)

label2 = Label(text="player 2 : o", font="times 20", bg="black", fg="blue")
label2.grid(row=0, column=2)

# # label3 = Label(text="Winner: ", font="times 20", bg="black",
#                fg="gold",)
# label3.grid(row=0, column=3)

# Each button is a square on the Grid
button1 = Button(root, width=20, height=10, command=lambda: game(1))
button1.grid(row=1, column=1,)

button2 = Button(root, width=20, height=10, command=lambda: game(2))
button2.grid(row=1, column=2)

button3 = Button(root, width=20, height=10, command=lambda: game(3))
button3.grid(row=1, column=3)

button4 = Button(root, width=20, height=10, command=lambda: game(4))
button4.grid(row=4, column=1)

button5 = Button(root, width=20, height=10, command=lambda: game(5))
button5.grid(row=4, column=2)

button6 = Button(root, width=20, height=10, command=lambda: game(6))
button6.grid(row=4, column=3)

button7 = Button(root, width=20, height=10, command=lambda: game(7))
button7.grid(row=8, column=1)

button8 = Button(root, width=20, height=10, command=lambda: game(8))
button8.grid(row=8, column=2)

button9 = Button(root, width=20, height=10, command=lambda: game(9))
button9.grid(row=8, column=3)

quit = Button(root, text="Quit", command=root.destroy).grid(column=3, row=0,)

# Mainloop is continuously checking for any changes
root.mainloop()
