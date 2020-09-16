from tkinter import *
#ddd


root = Tk()
root.title('tetete')
root.geometry('860x480')

label_frame = LabelFrame(root)
label_1 = LabelFrame(root,text='Wpisz numer dokumentu do poprawy.')
label_1.pack(fill='x',padx=10,pady=10,ipadx=10,ipady=5)

def destr():
	label_frame.destroy()

def clik_1(master):
	global label_frame
	destr()
	label_frame = LabelFrame(root, text="Zmiana!! kontrachenta na dokumecie.",bd=2)
	label_frame.pack(fill='x',expand="yes")
	label = Label(label_frame, text=master)
	label.pack()
	label_fr = LabelFrame(label_frame,text='eee')
	label_fr.pack(fill='both',expand="yes",padx=150,pady=50)
	nr_dok = Label(label_fr,text='Numer dokumentu')
	nr_dok.grid(row=0,padx=50,pady=10,sticky=W)
	nr_kon = Label(label_fr,text='Numer kontrachenta')
	nr_kon.grid(row=1,padx=50,pady=10)
	kwota = Label(label_fr,text='Kwota dokumentu')
	kwota.grid(row=2,padx=50,pady=10,sticky=W)
	p_nr_dok = Entry(label_fr,text='Numer dokumentu',state=DISABLED)
	p_nr_dok.grid(row=0,column=1,padx=50,pady=10,sticky=W)
	p_nr_kon = Entry(label_fr,text='Numer kontrachenta')
	p_nr_kon.grid(row=1,column=1,padx=50,pady=10)
	p_kwota = Entry(label_fr,text='Kwota dokumentu')
	p_kwota.grid(row=2,column=1,padx=50,pady=10,sticky=W)
	
	but_popraw = Button(label_fr,text='POPRAW')
	but_popraw.grid(row=2,column=2,padx=5,pady=5,ipadx=5,ipady=5)
	but_anuluj = Button(label_fr,text='ANULUJ',command=destr)
	but_anuluj.grid(row=4,column=2,padx=5,pady=5,ipadx=8,ipady=5)

my_but1 = Button(label_1, text='Popraw kontrachenta na FM' , command=lambda: clik_1('Zmiana na FM lub RM'))
my_but2 = Button(label_1, text='Popraw kontrachenta na KW' , command=lambda: clik_1('Zmiana na KW lub KP'))
nr_1 = Entry(label_1)
nr_2 = Entry(label_1)
my_but1.grid(row=0,column=0,padx=10,pady=10)
nr_1.grid(row=0,column=1)
nr_2.grid(row=1,column=1)
my_but2.grid(row=1,column=0,padx=10,pady=10)


root.mainloop()
