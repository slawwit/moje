from tkinter import *


root = Tk()
root.title('Kombinet')
root.geometry('480x400')
frame_1 = Frame(root)
frame_1.grid(row=1)
def clik_but1():
	toplab = Toplevel()
	toplab.withdraw()


def clik_but2():
	return
label_1 = Label(root,text='Wybierz w jakim dokumęcie zmienić kontrachęta?')
label_1.grid(row=0,column=1,columnspan=2,ipadx=10,ipady=10,padx=10,pady=10)
label_2 = Label(root,text='NR Faktury:')
label_3 = Label(root,text='NR    KW  :')
label_2.grid(row=1,column=0,sticky=W,padx=4,pady=4)
label_3.grid(row=2,column=0,sticky=W,padx=4,pady=4)
pole_1 = Entry(root,text='ddd')
pole_2 = Entry(root,text='dewrf')
pole_1.grid(row=1,column=1)
pole_2.grid(row=2,column=1)
but1 = Button(root,text='Zmiana na fakturze FM',command=clik_but1,)
but2 = Button(root,text='Zmiana na KW',command=clik_but2)
but1.grid(row=1,column=2,pady=10)
but2.grid(row=2,column=2,ipadx=22)

root.mainloop()