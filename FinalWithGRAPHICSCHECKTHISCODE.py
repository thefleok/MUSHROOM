"""
Names: Leo Jergovic and Kamran Murray
Class: ATCS
Assignment: Final Project Code

This project is a game that is played by a user through the shell and
external graphics built into the python language (most notably the
functionalities of tkinter, with the occasional help of turtle graphics).
This game allows users to select a game mode and answer math question,
receiving a correct or false result and being treated accordingly by the
game. The user is booted out when answering a question wrong, and the
difficulty of the game increases as the range of the numbers being asked
to perform operations on steadily rises in increments of 1 per correct answer.
"""

import tkinter as tk # for fundamental graphics in this program (abbbreviated tk)
import random #for random selection in numbber ranges
from functools import partial # for use with tkinter to split up methods
import turtle # for trolls

def main(): # main - runs the code, starts the game, emits an immediate choice
    root = tk.Tk()
    w = tk.Label(root, width = 90, height = 25, text = """WELCOME TO THE CHOCOROOM GAME.
This is a game not for the faint of heart. You will choose
between the following game modes and determine if you are a
legend:""", font = "Times 20", fg = "black", bg = "yellow") # adjusting parameters of text/box size
    w.pack() # following buttons are options for player game modes
    button1 = tk.Button(root, text="Addition", fg="blue", font = "Times 15", command=addition)
    button1.pack()
    button2 = tk.Button(root, text="Subtraction", fg="green", font = "Times 15", command=subtraction)
    button2.pack()
    button3 = tk.Button(root, text="Multiplication", fg="orange", font = "Times 15", command=multiplication)
    button3.pack()
    button4 = tk.Button(root, text="Division", fg="brown", font = "Times 15", command=division)
    button4.pack()
    button5 = tk.Button(root, text="Exponent", fg="black", font = "Times 15", command=exponent)
    button5.pack()
    button6 = tk.Button(root, text="QUIT", fg="red", font = "Times 15", command=root.destroy)
    button6.pack() # users allowed to quit game by exiting main loop for tkinter
    root.mainloop()

def addition(): # addition method jumpstarts addition and sends to sub method trueaddition
    root = tk.Tk()
    w = tk.Label(root, width = 60, height = 15, text = """Please find your way to the shell. EPONENTS
    Ready to start?
    """, font = "Times 30", fg = "white", bg = "teal")
    w.pack()
    onetrueaddition = partial(trueaddition, 1)
    button1 = tk.Button(root, text="Ready!", fg="blue", command=onetrueaddition)
    button1.pack()
    root.mainloop()

def trueaddition(END): # takes in level (END number) of current player
    y = 1
    end = END
    while (y == 1): # keep game looping
        first = random.randint(0, end)
        second = random.randint(0, end)
        answer = first + second
        print (first, " + ", second, " ?")
        madeit = False
        x = input()
        if x == str(answer):
            if end % 3 == 0: # % 3 changes colors of congratulatory statement, adding variety and interest
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "yellow", bg = "green")
                w.pack()
                truetrueaddition = partial(trueaddition, end + 1)
                button1 = tk.Button(root, text="Next Question!", fg="blue", command=truetrueaddition)
                button1.pack()
                root.mainloop()
                end = end + 1
            elif end % 3 == 1:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "black", bg = "pink")
                w.pack()
                truetrueaddition = partial(trueaddition, end + 1)
                button1 = tk.Button(root, text="Next Question!", fg="blue", command=truetrueaddition)
                button1.pack()
                root.mainloop()
                end = end + 1
            elif end % 3 == 2:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "purple", bg = "grey")
                w.pack()
                truetrueaddition = partial(trueaddition, end + 1)
                button1 = tk.Button(root, text="Next question!", fg="blue", command=truetrueaddition)
                button1.pack()
                root.mainloop()
                end = end + 1

        else:
            # not even gonna lie found this smiley face code online and had to use it all credit where credits due
            smiles = turtle.Turtle()
            smiles = turtle.Turtle()
            smiles.penup()
            smiles.goto(-75,150)
            smiles.pendown()
            smiles.circle(10)
            # this is not no work, as we had to flip values for smile to make frowny face
            smiles.penup()
            smiles.goto(75,150)
            smiles.pendown()
            smiles.circle(10)
            smiles.penup()
            smiles.goto(0,50)
            smiles.pendown()
            smiles.circle(-100,90)

            smiles.penup()
            smiles.setheading(180)
            smiles.goto(0,50)
            smiles.pendown()
            smiles.circle(100,90)
            print ('FINAL SCORE: ' + str(end - 1))
            print ("Failure. You lose.")
            exit()

def subtraction(): # rest of methods are lowkey the same w different numbers
    root = tk.Tk()
    w = tk.Label(root, width = 60, height = 15, text = """Please find your way to the shell.
    Ready to start?
    """, font = "Times 16", fg = "white", bg = "teal")
    w.pack()
    onetruesubtraction = partial(truesubtraction, 1)
    button1 = tk.Button(root, text="Ready!", fg="blue", command=onetruesubtraction)
    button1.pack()
    root.mainloop()

def truesubtraction(END):
    y = 1
    end = END
    while (y == 1):
        first = random.randint(0, end)
        second = random.randint(0, end)
        answer = first - second
        print (first, " - ", second, " ?")
        madeit = False
        x = input()
        if x == str(answer):
            if end % 3 == 0:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "yellow", bg = "green")
                w.pack()
                truetruesubtraction = partial(truesubtraction, end + 1)
                button1 = tk.Button(root, text="Next Question!", fg="blue", command=truetruesubtraction)
                button1.pack()
                root.mainloop()
                end = end + 1
            elif end % 3 == 1:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "black", bg = "pink")
                w.pack()
                truetruesubtraction = partial(truesubtraction, end + 1)
                button1 = tk.Button(root, text="Next Question!", fg="blue", command=truetruesubtraction)
                button1.pack()
                root.mainloop()
                end = end + 1
            elif end % 3 == 2:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "purple", bg = "grey")
                w.pack()
                truetruesubtraction = partial(truesubtraction, end + 1)
                button1 = tk.Button(root, text="Next question!", fg="blue", command=truetruesubtraction)
                button1.pack()
                root.mainloop()
                end = end + 1
        else:
            smiles = turtle.Turtle()
            smiles = turtle.Turtle()
            smiles.penup()
            smiles.goto(-75,150)
            smiles.pendown()
            smiles.circle(10)     #eye one

            smiles.penup()
            smiles.goto(75,150)
            smiles.pendown()
            smiles.circle(10)
            smiles.penup()
            smiles.goto(0,50)
            smiles.pendown()
            smiles.circle(-100,90)

            smiles.penup()
            smiles.setheading(180)
            smiles.goto(0,50)
            smiles.pendown()
            smiles.circle(100,90)
            print ('FINAL SCORE: ' + str(end - 1))
            print ("Failure. You lose.")
            exit()

def multiplication():
    root = tk.Tk()
    w = tk.Label(root, width = 60, height = 15, text = """Please find your way to the shell.
    Ready to start?
    """, font = "Times 16", fg = "white", bg = "teal")
    w.pack()
    onetruemult = partial(truemult, 1)
    button1 = tk.Button(root, text="Ready!", fg="blue", command=onetruemult)
    button1.pack()
    root.mainloop()

def truemult(END):
    y = 1
    end = END
    while (y == 1):
        first = random.randint(0, end)
        second = random.randint(0, end)
        answer = first * second
        print (first, " * ", second, " ?")
        madeit = False
        x = input()
        if x == str(answer):
            if end % 3 == 0:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "yellow", bg = "green")
                w.pack()
                truetruemult = partial(truemult, end + 1)
                button1 = tk.Button(root, text="Next Question!", fg="blue", command=truetruemult)
                button1.pack()
                root.mainloop()
                end = end + 1
            elif end % 3 == 1:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "black", bg = "pink")
                w.pack()
                truetruemult = partial(truemult, end + 1)
                button1 = tk.Button(root, text="Next Question!", fg="blue", command=truetruemult)
                button1.pack()
                root.mainloop()
                end = end + 1
            elif end % 3 == 2:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "purple", bg = "grey")
                w.pack()
                truetruemult = partial(truemult, end + 1)
                button1 = tk.Button(root, text="Next question!", fg="blue", command=truetruemult)
                button1.pack()
                root.mainloop()
                end = end + 1
        else:
            smiles = turtle.Turtle()
            smiles = turtle.Turtle()
            smiles.penup()
            smiles.goto(-75,150)
            smiles.pendown()
            smiles.circle(10)     #eye one

            smiles.penup()
            smiles.goto(75,150)
            smiles.pendown()
            smiles.circle(10)
            smiles.penup()
            smiles.goto(0,50)
            smiles.pendown()
            smiles.circle(-100,90)

            smiles.penup()
            smiles.setheading(180)
            smiles.goto(0,50)
            smiles.pendown()
            smiles.circle(100,90)
            print ('FINAL SCORE: ' + str(end - 1))
            print ("Failure. You lose.")
            exit()

def division():
    root = tk.Tk()
    w = tk.Label(root, width = 60, height = 15, text = """Please find your way to the shell.
    Ready to start?
    """, font = "Times 16", fg = "white", bg = "teal")
    w.pack()
    onetrued = partial(trued, 1)
    button1 = tk.Button(root, text="Ready!", fg="blue", command=onetrued)
    button1.pack()
    root.mainloop()

def trued(END):
    y = 1
    end = END
    while (y == 1):
        first = random.randint(1, end)
        second = random.randint(1, end)
        answer = first / (second * 1.0)
        print (first, " / ", second, " ?")
        madeit = False
        x = input()
        if float(x) - float(answer) <= 0.1:
            if end % 3 == 0:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "yellow", bg = "green")
                w.pack()
                truetrued = partial(trued, end + 1)
                button1 = tk.Button(root, text="Next Question!", fg="blue", command=truetrued)
                button1.pack()
                root.mainloop()
                end = end + 1
            elif end % 3 == 1:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "black", bg = "pink")
                w.pack()
                truetrued = partial(trued, end + 1)
                button1 = tk.Button(root, text="Next Question!", fg="blue", command=truetrued)
                button1.pack()
                root.mainloop()
                end = end + 1
            elif end % 3 == 2:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "purple", bg = "grey")
                w.pack()
                truetrued = partial(trued, end + 1)
                button1 = tk.Button(root, text="Next question!", fg="blue", command=truetrued)
                button1.pack()
                root.mainloop()
                end = end + 1

        else:

            smiles = turtle.Turtle()
            smiles = turtle.Turtle()
            smiles.penup()
            smiles.goto(-75,150)
            smiles.pendown()
            smiles.circle(10)     #eye one

            smiles.penup()
            smiles.goto(75,150)
            smiles.pendown()
            smiles.circle(10)
            smiles.penup()
            smiles.goto(0,50)
            smiles.pendown()
            smiles.circle(-100,90)

            smiles.penup()
            smiles.setheading(180)
            smiles.goto(0,50)
            smiles.pendown()
            smiles.circle(100,90)
            print ('FINAL SCORE: ' + str(end - 1))
            print ("Failure. You lose.")
            exit()

def exponent():
    root = tk.Tk()
    w = tk.Label(root, width = 60, height = 15, text = """Please find your way to the shell.
    Ready to start?
    """, font = "Times 16", fg = "white", bg = "teal")
    w.pack()
    onetrueex = partial(trueex, 1)
    button1 = tk.Button(root, text="Ready!", fg="blue", command=onetrueex)
    button1.pack()
    root.mainloop()

def trueex(END):
    y = 1
    end = END
    while (y == 1):
        first = random.randint(0, end)
        second = random.randint(0, end)
        answer = first ** second
        print (first, " ^ ", second, " ?")
        madeit = False
        x = input()
        if x == str(answer):
            if end % 3 == 0:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "yellow", bg = "green")
                w.pack()
                truetrueex = partial(trueex, end + 1)
                button1 = tk.Button(root, text="Next Question!", fg="blue", command=truetrueex)
                button1.pack()
                root.mainloop()
                end = end + 1
            elif end % 3 == 1:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "black", bg = "pink")
                w.pack()
                truetrueex = partial(trueex, end + 1)
                button1 = tk.Button(root, text="Next Question!", fg="blue", command=truetrueex)
                button1.pack()
                root.mainloop()
                end = end + 1
            elif end % 3 == 2:
                root = tk.Tk()
                w = tk.Label(root, width = 20, height = 5, text = "CORRECT", font = "Times 30", fg = "purple", bg = "grey")
                w.pack()
                truetrueex = partial(trueex, end + 1)
                button1 = tk.Button(root, text="Next question!", fg="blue", command=truetrueex)
                button1.pack()
                root.mainloop()
                end = end + 1

        else:

            smiles = turtle.Turtle()
            smiles = turtle.Turtle()
            smiles.penup()
            smiles.goto(-75,150)
            smiles.pendown()
            smiles.circle(10)     #eye one

            smiles.penup()
            smiles.goto(75,150)
            smiles.pendown()
            smiles.circle(10)
            smiles.penup()
            smiles.goto(0,50)
            smiles.pendown()
            smiles.circle(-100,90)

            smiles.penup()
            smiles.setheading(180)
            smiles.goto(0,50)
            smiles.pendown()
            smiles.circle(100,90)
            print ('FINAL SCORE: ' + str(end - 1))
            print ("Failure. You lose.")
            exit()

main()
