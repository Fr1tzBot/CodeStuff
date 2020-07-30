import tkinter

stuff = ("uno", "dos", "tres")

root = tkinter.Tk()

root.title("MusicDownloader")

def readAll():
    title.value = title.entry.get()
    artist.value = artist.entry.get()

class intro:
    row = 0
    version = 1.7
    label = tkinter.Label(root, text="Music Downloader Version " + str(version))
intro.label.grid(column=0, row=intro.row)
blank = tkinter.Label(root, text="")
blank.grid(column=0, row = intro.row+1)

class title:
    value = ""
    row = 2
    label = tkinter.Label(root, text="Title:")
    entry = tkinter.Entry(root,width=30)

title.label.grid(column=0, row=title.row)
title.entry.grid(column=0, row=title.row+1)

class artist:
    value = ""
    row = 4
    label = tkinter.Label(root, text="Artist:")
    entry = tkinter.Entry(root, width = 30)

artist.label.grid(column=0, row=artist.row)
artist.entry.grid(column=0, row=artist.row+1)

blank = tkinter.Label(root, text="")
blank.grid(column=0, row=artist.row+3)

nextButton = tkinter.Button(root, text="Enter", command=readAll)
nextButton.grid(column=0, row=artist.row+4)

class radioButtons:
    row = 9
    radio1 = tkinter.Radiobutton(root,text=stuff[0], value=1)
    radio2 = tkinter.Radiobutton(root,text=stuff[1], value=2)
    radio3 = tkinter.Radiobutton(root,text=stuff[2], value=3)

radioButtons.radio1.grid(column=0, row=radioButtons.row)
radioButtons.radio2.grid(column=0, row=radioButtons.row+1)
radioButtons.radio3.grid(column=0, row=radioButtons.row+2)

root.mainloop()