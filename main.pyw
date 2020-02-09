from tkinter import *
import pyperclip

FONT = 'Arial'
SIZE = 20

root = Tk()
root.resizable(width=False, height=False)
root.title('mOcKiNg SpOnGeBoB cOnVeRtEr')
root.geometry("600x150+30+30")

root.iconbitmap(r"E:/useful_stuff/img/logo.ico")

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

center(root)

label = Label(root, text='Your input:', width=15)
label.grid(row=0, column=0)
label.config(font=(FONT, SIZE))

content = StringVar()

box = Entry(root, textvariable=content, font=(FONT, SIZE))
box.grid(row=0, column=1)

label2 = Label(root, text='Output:', width=15)
label2.grid(row=2, column=0)
label2.config(font=(FONT, SIZE))

outputstr = StringVar()
output = Entry(root, textvariable= outputstr, font=(FONT, SIZE))
output.grid(row=2, column=1)
output.config(state=DISABLED)

def convert():
	switch = 1
	i = content.get()
	o = ''

	for ch in i:
		if ch.isalpha():
			switch ^= 1
			if switch == 1:
				o = o + ch.upper()
			else:
				o = o + ch
		else:
			o = o + ch
	pyperclip.copy(o)
	outputstr.set(o)

test = Button(root, text='Convert & Copy to Clipboard', command=convert, font=(FONT, SIZE-5))
test.grid(row=3, column=1)

instruction = Label(root, text='(You can also press Enter)', font=(FONT, SIZE >> 1))
instruction.grid(row=4, column=1)

credit = Label(root, text='Made by @omgursocute with love <3', font=(FONT, SIZE >> 1))
credit.grid(row=4, column=0)

root.bind('<Return>', lambda x: convert())
box.focus()
root.mainloop()