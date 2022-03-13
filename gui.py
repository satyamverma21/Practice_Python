#1 { .mainloop()  } hold the gui ,until u manually close it
#2 GUI START FROM HERE
#3 
# WEIGITS AND ATTRIBUTE PLACING IN WINDOW
# LEBEL IS A WEIGHT ,THAT DON'T INTERECT WITH USER
#---------------------------------------------------------------------------------------------------

# root = Tk() == basic GUI
# .mainloop( ) == hold basic GUI
# .geometry("WxH") == initial size of screen, w - width , h - height
# .minsize(W,H) == limit minimum size / lock minimum size
# .maxsize(W,H) == limit maximum size / lock maximum size

# remove hashtags , if u want to run particular

#------------------------------------[ //1// Basic GUI / INITIAL,MAX,MIN SIZE / TEXT(LABEL) ]---------------------------------------------------------

#from tkinter import *


#root = Tk() # create a basic gui

#root.geometry("1000x500")  # initial size 
#root.maxsize(1080,600)  # lock max size
#root.minsize(200,100)   # lock min size

#sj = Label(text="my first GUI")
#sj.pack()


#root.mainloop()

#---------------------------------------------------[displaying images]---------------------------------------------------------------------------

#from tkinter import *
#from PIL import Image , ImageTk # Help in image rendering

#root = Tk()
#root.geometry("600x500")

#photo =PhotoImage(file="20210831_160621.png") these line not support
#sj_label = Label(image=photo)  these line not support

#image = Image.open("20210831_160621.png")
#photo = ImageTk.PhotoImage(image)

#sj_label=Label(image=photo)
#sj_label.pack()

#root.mainloop()

#-----------------------------------------[label options / pack options ]---------------------------------------------------------------

#***********************[ label(options) ]

#1   text= add the text 
#2   bd = background
#3   fg = foreground
#4   font = sets the font , 1# font=("italic",19,"bold") ,#2 font=("italic 19 bold")
#5   padx = x padding
#6   pady = y padding
#7   relief = border style = SUNKEN , RAISED , GROOVE ,RIDGE
#8   borderwidth

#**********************************


#***********************[ pack(options) ]
# ANCHOR = NW ,EW ,S { directions}
# side = top , botton , left , right
# fill = streach
# padx = border
# pady = border


from tkinter import *

root = Tk()

root.geometry("700x400")
root.title("my first GUI") 
title_label = Label(text="""The above members help support the Python ecosystem
 organizing Python events and conferences, starting Python communities in local regions,
 Python more accessible around the world. To learn more about the new Fellow members, 
 check out their links above.""",
 bg="red",fg="green",padx=23 ,pady=44,font=("italic 5 bold"),borderwidth=7,relief=SUNKEN)

#title_label.pack(side = BOTTOM,anchor="nw",fill = X )
title_label.pack(side = LEFT,fill = X , padx=100, pady=50 )

root.mainloop()































