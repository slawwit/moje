
from tkinter import *
import fdb
import sqlite3
from tkinter import messagebox
from PIL import ImageTk,Image

def connekt():
	global cur
	global con
	global con_ok
	con_ok = ''
	try:
		con = fdb.connect(
    	host=host, database=database,
    	user='sysdba', password='masterkey')
		cur = con.cursor()
		con_ok = 1
	except fdb.fbcore.DatabaseError as e:
		messagebox.showwarning("Błąd w połączeniu z bazą",("Wprowadź poprawną ścieżkę lokalizacji bazy!!\n",e))


def select(num):
	global cc
	if num == 1:
		numer = nr_1.get()
		SELECT = ("select dokument,kon,winien from mat_oew where dokument="+"'"+ numer +"'")
	if num == 2:
		numer = nr_2.get()
		SELECT = ("select dokument,kon,winien,ma from mat_wpl where dokument="+"'"+ numer +"'")
	cur.execute(SELECT)
	cc = cur.fetchall()
	con.commit()
	if cc == []:
		messagebox.showwarning("Błąd wyszukiwania!!!",("Taki dokument nie istnieje,\nWpisz poprawny numer dokumentu."))


	
	

def destr():
	
	label_frame.destroy()
	my_but1.config(state=ACTIVE)
	my_but2.config(state=ACTIVE)

def destr2():
	top.destroy()
	
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
	if p_kwota.get() != '0.0':
		messagebox.showwarning("Niespełniony warunek!!","Musisz najpierw wyzerować dokument!!!")
	else:
		try:
			cur.execute(update)
		except fdb.fbcore.DatabaseError as e:
			messagebox.showwarning("Błąd kontrachenta!",("Brak kontrachenta o tym numerze,\nWprowadź numer istniejącego kontrachenta !!\n",e))


		con.commit()
	con.close()
	destr()


def tworz_frame(master,numm):
	global label_frame
	global p_nr_dok
	global p_nr_kon
	global p_kwota
	global nr_dok
	global cc
	destr()
	popup()
	label_frame = LabelFrame(root, text="Zmiana!! kontrachenta na dokumecie.",bd=2)
	label_frame.pack(fill='x',expand="yes")
	label = Label(label_frame, text=master)
	label.pack()
	label_fr = LabelFrame(label_frame,text='')
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
	my_but1.config(state=DISABLED)
	my_but2.config(state=DISABLED)
#dddddd
def clik_1(master,arg):
	connekt()
	if con_ok == 1:
		if arg == 1:
			if nr_1.get() == '':
				popup1()
			else:
				if_doc(master,arg)
			
		if arg == 2:
			if nr_2.get() == '':
				popup1()
			else:
				if_doc(master,arg)

def if_doc(master,arg):
	select(arg)
	
	if cc != []:
		tworz_frame(master,arg)
		for row in cc:
			p_nr_dok.insert(0,row[0])
			p_nr_kon.insert(0,row[1])
			dd = row[0]
			ddd = dd[0]+dd[1]
			if ddd == 'KP':
				p_kwota.insert(0,row[3])
			else:
				p_kwota.insert(0,row[2])
			con.close()
			p_nr_dok.config(state=DISABLED)
			p_kwota.config(state=DISABLED)


def zakoncz():
	connekt()
	con.close()
	root.quit()

def lok_zatw():
	global host
	global database
	global host_p
	global lokal_p
		#host = host_p.get()
	#database = lokal_p.get()
	conn =sqlite3.connect('lokalizacja.db')
	c = conn.cursor()

	rec_id = 1
	c.execute("""UPDATE lolalizacion SET 
		host= :host,
		lokalizacja= :loc
		WHERE oid = :oid""",
		{
		'host': host_p.get(),
		'loc': lokal_p.get(),
		'oid': rec_id
		})
	conn.commit()
	host = host_p.get()	
	database = lokal_p.get()
	connekt()
	if con_ok == 1:
		top.destroy()
	

def local_base():
	global host_p
	global lokal_p
	global top
	top = Toplevel(root)
	top.transient([root])
	top.title('Zmiana lokalizacji bazy.')
	top.geometry('500x200+320+320')
	
	lab_1 = Label(top,text="Host")
	lab_2 = Label(top,text='Lokalizacja')
	but_zatw = Button(top,text="Zatwierź",command=lok_zatw)
	but_anul = Button(top,text="Anuluj",command=lambda: top.destroy())
	host_p = Entry(top,)
	lokal_p = Entry(top,width=50)
	
	lab_1.grid(row=0,column=0,padx=20,pady=10,sticky=W)
	lab_2.grid(row=1,column=0,padx=20,pady=10,sticky=W)
	host_p.grid(row=0,column=1,pady=10,sticky=W)
	lokal_p.grid(row=1,column=1,pady=10)
	but_zatw.grid(row=3,column=1,ipadx=9,ipady=7,padx=10,pady=10,sticky=E)
	but_anul.grid(row=3,column=2,ipadx=9,ipady=7)
	con_sqlite(2)


def popup():
	messagebox.showwarning("Zastanów się!!!!","Uwaga bądź ostrożny !!!")


def popup1():
	messagebox.showinfo("Info","Wpisz numer dokumentu!")


def con_sqlite(arg1):
	global host
	global database
	conn =sqlite3.connect('lokalizacja.db')
	c = conn.cursor()
	#c.execute("""CREATE TABLE lolalizacion (host text, lokalizacja text)""")
	#conn.commit()
	c.execute("SELECT * FROM lolalizacion WHERE oid = 1")
	records = c.fetchall()
	if arg1 == 1:
		for record in records:
			host = record[0]
			database = record[1]
	if arg1 == 2:
		for record in records:
			host_p.insert(0, record[0])
			lokal_p.insert(0, record[1])



root = Tk()
root.title('Watkemik')
root.geometry('860x480+120+120')
root.iconbitmap('watkem.ico')

host = ''
database = ''

menu = Menu(root)
menuinne = Menu(menu,tearoff=0)
menuinne.add_command(label="Lokalzacja bazy",command=local_base)
menuinne.add_separator()
menuinne.add_command(label="Koniec",command=zakoncz)
menu.add_cascade(label="Inne", menu=menuinne)
root.config(menu=menu)

label_frame = LabelFrame(root)
label_1 = LabelFrame(root,text='Wpisz numer dokumentu do poprawy.')
label_1.pack(fill='x',padx=10,pady=10,ipadx=10,ipady=5)

my_but1 = Button(label_1, text='Popraw kontrachenta na FM lub RM' , command=lambda: clik_1('Zmiana na FM lub RM', 1))
my_but2 = Button(label_1, text='Popraw kontrachenta na KW lub KP' , command=lambda: clik_1('Zmiana na KW lub KP', 2))
nr_1 = Entry(label_1)
nr_2 = Entry(label_1)

my_but1.grid(row=0,column=0,padx=10,pady=10)
my_but2.grid(row=1,column=0,padx=10,pady=10)
nr_1.grid(row=0,column=1)
nr_2.grid(row=1,column=1)

con_sqlite(1)

root.mainloop()
