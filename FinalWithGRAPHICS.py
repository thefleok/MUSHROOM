import tkinter as tk
import random
from functools import partial
import turtle
import decimal
def main():
    root = tk.Tk()
    w = tk.Label(root, width = 60, height = 15, text = """WELCOME TO THE CHOCOROOM GAME.
This is a game not for the faint of heart. You will choose
between the following game modes and determine if you are a
legend:""", font = "Times 16", fg = "black", bg = "yellow")
    w.pack()
    button1 = tk.Button(root, text="Addition", fg="blue", command=addition)
    button1.pack()
    button2 = tk.Button(root, text="Subtraction", fg="green", command=subtraction)
    button2.pack()
    button3 = tk.Button(root, text="Multiplication", fg="orange", command=multiplication)
    button3.pack()
    button4 = tk.Button(root, text="Division", fg="brown", command=division)
    button4.pack()
    button5 = tk.Button(root, text="Exponent", fg="black", command=addition)
    button5.pack()
    button6 = tk.Button(root, text="QUIT", fg="red", command=root.destroy)
    button6.pack()
    root.mainloop()

def addition():
    root = tk.Tk()
    w = tk.Label(root, width = 60, height = 15, text = """Please find your way to the shell.
    Ready to start?
    """, font = "Times 16", fg = "black", bg = "yellow")
    w.pack()
    onetrueaddition = partial(trueaddition, 1)
    button1 = tk.Button(root, text="Ready!", fg="blue", command=onetrueaddition)
    button1.pack()
    root.mainloop()
def trueaddition(END):
    y = 1
    end = END
    while (y == 1):
        first = random.randint(0, end)
        second = random.randint(0, end)
        answer = first + second
        print (first, " + ", second, " ?")
        madeit = False
        x = input()
        if x == str(answer):
            if end % 3 == 0:
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
def subtraction():
    root = tk.Tk()
    w = tk.Label(root, width = 60, height = 15, text = """Please find your way to the shell.
    Ready to start?
    """, font = "Times 16", fg = "black", bg = "yellow")
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
    """, font = "Times 16", fg = "black", bg = "yellow")
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
    """, font = "Times 16", fg = "black", bg = "yellow")
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
        answer = decimal.Decimal(first) / decimal.Decimal(second)
        print (first, " / ", second, " ?")
        madeit = False
        x = input()
        if x.isdigit():
            if int(x) - int(answer) <= 0.25:
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
    print("try hard pisser")

main()
