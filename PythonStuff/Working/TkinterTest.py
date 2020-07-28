from tkinter import *

window = Tk()

window.title("MusicDownloader")

window.geometry('250x350')
window.bind('<Return>', exit)

#Row One:
def readTitle():
    print(title.entry.get())

class title:
    row = 0
    label = Label(window, text="Title:")
    entry = Entry(window,width=15)
    button = Button(window, text="", command=readTitle)

title.label.grid(column=0, row=title.row)
title.entry.grid(column=1, row=title.row)
title.button.grid(column=2, row=title.row)

#Row Two:
def readArtist():
    print(artist.entry.get())
class artist:
    row = 3
    label = Label(window, text="Artist:")
    entry = Entry(window, width = 15)
    button = Button(window, text="", command=readArtist)

artist.label.grid(column=0, row=artist.row)
artist.entry.grid(column=1, row=artist.row)
artist.button.grid(column=2, row=artist.row)

window.mainloop()