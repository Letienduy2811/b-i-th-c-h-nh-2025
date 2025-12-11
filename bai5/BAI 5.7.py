print("Sinh vien: LE HOANG VU")
print("Ma so SV : 245751030110084")
print("#############################")
import tkinter
import random

colors = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score = 0
timeleft = 30

def startGame(event):
    if timeleft == 30:
        countdown()
    nextColour()

def nextColour():
    global score
    global timeleft

    if timeleft > 0:

        e.focus_set()

        if e.get().lower() == colors[1].lower():
            global score
            score += 1

        e.delete(0, tkinter.END)

        random.shuffle(colors)

        label.config(fg=str(colors[1]), text=str(colors[0]))

        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1

        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)

# GUI
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")

instructions = tkinter.Label(root, text="Type in the colour of the words, not the text!",
                             font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Press Enter to start", font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

root.mainloop()
