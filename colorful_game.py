import tkinter 
import random 


colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
root = tkinter.Tk() 
#title 
root.title("COLORFUL GAME") 

#window size 
root.geometry("600x300") 

def main():
    
    
    global timeleft
    global score
    global scoreLabel
    global timeLabel
    global label
    global instructions
    global e
    score = 0
    timeleft = 60
    
    #instructions label 
    instructions = tkinter.Label(root, text = "Type the colour of the word, and not the word!",font = ('TimesnewRoman bold', 20))
    instructions.pack() 

    #score label 
    scoreLabel = tkinter.Label(root, text = "Press enter to start",font = ('TimesnewRoman', 15)) 
    scoreLabel.pack() 

    #time left label 
    timeLabel = tkinter.Label(root, text = "Time left: "+str(timeleft)+" seconds", font = ('TimesnewRoman', 15))
    timeLabel.pack() 

    #label for displaying the colours and word 
    label = tkinter.Label(root, font = ('TimesnewRoman bold', 50)) 
    label.pack() 

    #text entry box for typing in colours 
    e = tkinter.Entry(root,font=('TimesnewRoman', 15),width=15)
    
    # running the 'startGame' function when the enter key is pressed 
    root.bind('<Return>', startGame) 
    e.pack() 

    # set focus on the entry box 
    e.focus_set() 

    # start the GUI 
    root.mainloop()

    
    
def startGame(event):
        if timeleft == 60:
            # start the countdown timer.
            countdown()
            # run the function to choose the next colour. 
        nextColour() 

def startGame(event):
    if timeleft == 60:
        # start the countdown timer.
        countdown()
        # run the function to choose the next colour. 
    nextColour() 

def nextColour(): 
    global score 
    global timeleft
    
    if timeleft > 0: 
        # make the text entry box active.
        e.focus_set()
        
        if e.get().lower() == colours[1].lower():
            score += 1

        # clear the text entry box. 
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        # change the colour to type, by changing the text _and_ the colour to a random colour value 
        label.config(fg = str(colours[1]), text = str(colours[0]))
        # updating the score. 
        scoreLabel.config(text = "Score: " + str(score))
    
def countdown():
    global timeleft
    global score
    if timeleft > 0:
        timeleft -= 1
        # updating the time left label 
        timeLabel.config(text = "Time left: "+ str(timeleft))
        # run the function again after 1 second. 
        timeLabel.after(1000, countdown)
    else:
        # restarting the game again
        scoreLabel.destroy()
        instructions.destroy()
        timeLabel.destroy()
        label.destroy()
        e.destroy()
        main()

if __name__=="__main__":
    main()
