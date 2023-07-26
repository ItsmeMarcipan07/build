import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'C:\\Users\SESA732254\PycharmProjects\pythonProject1\\build\exe.win-amd64-3.10')
from tkinter import *


def clicked():
    lbl.configure(text="Button was clicked !!")  # change text on label
    window.destroy()  # destroy window


def get_value():
    lat = latitude.get()  # get value from Latitude var
    lon = longitude.get()  # get value from Longitude var
    return [lat, lon]  # return Latitude and Longitude values


window = Tk()  # create window with tkinter
window.title("Schneider Electric")  # set title
window.geometry('200x150')  # set geometry
window.configure(bg='#ffff99')  # set background
lbl = Label(window, text="Coordinates", bg='#ffff99')  # create label
lbl.grid(column=2, row=0)  # set label

latitude = StringVar()  # empty string var
longitude = StringVar()  # empty string var

lbl1 = Label(window, text="Enter Latitude", bg='#ffff99')  # create label
lbl1.grid(column=1, row=1)  # set label
txt1 = Entry(window, width=10, textvariable=latitude, bg='#ffff99')  # create entry
txt1.grid(column=2, row=1)  # set entry

lbl2 = Label(window, text="Enter Longitude", bg='#ffff99')  # create label
lbl2.grid(column=1, row=2)  # set label
txt2 = Entry(window, width=10, textvariable=longitude, bg='#ffff99')  # create entry
txt2.grid(column=2, row=2)  # set entry

btn = Button(window, text="Confirm", command=clicked, bg="#33cc33")  # create button
btn.grid(column=2, row=3)  # set button
window.mainloop()  # TODO starting window
