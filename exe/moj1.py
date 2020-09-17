from tkinter import *
import fdb

#ddd
#con = fdb.connect(dsn='bison:/temp/test.db', user='sysdba', password='pass')

# Or, equivalently:


root = Tk()
root.title('tetete')
root.geometry('860x480')

label_frame = LabelFrame(root)
label_1 = LabelFrame(root,text='Wpisz numer dokumentu do poprawy.')
label_1.pack(fill='x',padx=10,pady=10,ipadx=10,ipady=5)

def connekt():
	global cur
	global con
	con = fdb.connect(
    host='127.0.0.1', database='C:/Hermes/HERM.GDB',
    user='sysdba', password='masterkey')
	cur = con.cursor()
def select(num):
	global cc
	if num == 1:
		numer = nr_1.get()
		SELECT = ("select dokument,kon,winien from mat_oew where dokument="+"'"+ numer +"'")
	if num == 2:
		numer = nr_2.get()
		SELECT = ("select dokument,kon,winien from mat_wpl where dokument="+"'"+ numer +"'")
	cur.execute(SELECT)
	cc = cur.fetchall()

def destr():
	
	label_frame.destroy()
	
def update(num):
	global cc
	connekt()
	if num == 1:
		numer = ("'"+p_nr_dok.get()+"'")
		kon = p_nr_kon.get()
		update = ("update mat_oew set kon="+ kon +"  where dokument=" + numer)
	if num == 2:
		numer = ("'"+p_nr_dok.get()+"'")
		kon = p_nr_kon.get()
		update = ("update mat_wpl set kon="+ kon +"  where dokument=" + numer)
	
	cur.execute(update)
	con.commit()
	con.close()

def tworz_frame(master,numm):
	global label_frame
	global p_nr_dok
	global p_nr_kon
	global p_kwota
	global nr_dok
	global cc
	connekt()
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
	p_nr_dok = Entry(label_fr,text='Numer dokumentu')
	p_nr_dok.grid(row=0,column=1,padx=50,pady=10,sticky=W)
	p_nr_dok.delete(0,'end')
	p_nr_kon = Entry(label_fr,text='Numer kontrachenta')
	p_nr_kon.grid(row=1,column=1,padx=50,pady=10)
	p_nr_kon.delete(0,'end')
	p_kwota = Entry(label_fr,text='Kwota dokumentu')
	p_kwota.grid(row=2,column=1,padx=50,pady=10,sticky=W)
	p_kwota.delete(0,'end')
	but_popraw = Button(label_fr,text='POPRAW',command=lambda: update(numm))
	but_popraw.grid(row=2,column=2,padx=5,pady=5,ipadx=5,ipady=5)
	but_anuluj = Button(label_fr,text='ANULUJ',command=destr)
	but_anuluj.grid(row=4,column=2,padx=5,pady=5,ipadx=8,ipady=5)


def clik_1(master,przy):
	
	if przy == 1:
		connekt()
		select(przy)
		tworz_frame(master,przy)
		for row in cc:
			p_nr_dok.insert(0,row[0])
			p_nr_kon.insert(0,row[1])
			p_kwota.insert(0,row[2])
			con.close()
	if przy == 2:
		connekt()
		select(przy)
		tworz_frame(master,przy)
		for row in cc:
			p_nr_dok.insert(0,row[0])
			p_nr_kon.insert(0,row[1])
			p_kwota.insert(0,row[2])
			con.close()

my_but1 = Button(label_1, text='Popraw kontrachenta na FM' , command=lambda: clik_1('Zmiana na FM lub RM', 1))
my_but2 = Button(label_1, text='Popraw kontrachenta na KW' , command=lambda: clik_1('Zmiana na KW lub KP', 2))
nr_1 = Entry(label_1)

nr_2 = Entry(label_1)
my_but1.grid(row=0,column=0,padx=10,pady=10)
nr_1.grid(row=0,column=1)
nr_2.grid(row=1,column=1)
my_but2.grid(row=1,column=0,padx=10,pady=10)


root.mainloop()
