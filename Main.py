import os
from tkinter import *
from tkinter import font
import random
import time

#find the parent folder with seasons folders
path = os.path.dirname(os.path.realpath(__file__))

#create the window
window = Tk()
window.title('Random Video File Picker')
window.geometry('1000x200')

#create a font
myFont = font.Font(family='Roboto', size=20)

#create a file label
file_label = Label(window, text='', font=myFont, fg="black")
file_label.grid(column=0, row=0)

#create a countdown label
count_label = Label(window, text='', font=myFont, fg="red")
count_label.grid(column=0, row=1)

#the function for the button
def pick_file():
    #list all the folders in the parent folder
    folders = [x[0] for x in os.walk(path)]
    #remove the parent folder from the list
    folders.remove(path)
    #pick a random folder from the list
    folder = random.choice(folders)
    #list the video files in the folder
    files = [f for f in os.listdir(folder) if f.endswith('.mkv')]
    #pick a random file from the list
    file = random.choice(files)
    #update the file label
    file_label.configure(text='File: ' + file)
    #start the countdown
    for i in range(5, 0, -1):
        count_label.configure(text='Opening in: ' + str(i))
        #pause for 1 second
        time.sleep(1)
        #update the window
        window.update()
    #open the file
    os.startfile(os.path.join(folder, file))

#create the button
btn = Button(window, text='Pick File', font=myFont, command=pick_file)
btn.place(relx=0.5, rely=0.7, anchor='center')

#run the window
window.mainloop()
