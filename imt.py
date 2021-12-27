from tkinter import *

def calculation():
	try:
		height = float(height_entry.get())/100
		weight = float(weight_entry.get())
		imt = weight/(height*height)
		imt_text = "{0:.2f}".format(imt)
		text_imt = "Индекс массы тела равен:\n{}".format(imt_text)
		if imt<18.5:
			othet.configure(text=text_imt, bg='lightblue')
		elif imt<24.9:
			othet.configure(text=text_imt, bg='lightgreen')
		elif imt<29.9:
			othet.configure(text=text_imt, bg='yellow')
		else:
			othet.configure(text=text_imt, bg='orange')
	except Exception as e:
		error = 'ERROR: \n\n{}'.format(e)
		othet.configure(text=error, bg='red')

root = Tk()
root.title('Индекс массы тела')
root.configure(bg='lightgray')
root.geometry('565x280+500+300')
root.resizable(width=False, height=False)


table = LabelFrame(text="")
table.grid(row=1, column=0, columnspan=5)

table_11 = Label(table, text="<18.5", font='bold', width=13, height=2, bg="lightblue")
table_11.grid(row=0, column=0, padx=(20, 5), pady=(20, 5))
table_12 = Label(table, text="НЕДОСТАТОК \nВЕСА", width=13, height=2)
table_12.grid(row=1, column=0, padx=(20, 5))

table_21 = Label(table, text="18.5-24.9", font='bold', width=13, height=2, bg="lightgreen")
table_21.grid(row=0, column=1, padx=5, pady=(20, 5))
table_22 = Label(table, text="НОРМАЛЬНЫЙ \nВЕС", width=13, height=2)
table_22.grid(row=1, column=1, padx=5)

table_31 = Label(table, text="25-25.9", font='bold', width=13, height=2, bg="yellow")
table_31.grid(row=0, column=2, padx=5, pady=(20, 5))
table_32 = Label(table, text="ИЗБЫТОЧНЫЙ \nВЕС", width=13, height=2)
table_32.grid(row=1, column=2, padx=5)

table_41 = Label(table, text=">35", font='bold', width=13, height=2, bg="orange")
table_41.grid(row=0, column=3, padx=(5,20), pady=(20, 5))
table_42 = Label(table, text="ОЖИРЕНИЕ", width=13, height=2)
table_42.grid(row=1, column=3, padx=(5,20))


height_text = Label(text="РОСТ", font='bold', width=8, height=1, bg="white")
height_text.grid(row=0, column=0)
height_entry = Entry(text="5", font='bold', width=8, bg="white")
height_entry.grid(row=0, column=1, pady=20)

calculate = Button(width=12, height=1, activebackground='Yellow',
	           bg='gold', text="Вычислить", font='bold', command=calculation)
calculate.grid(row=0, column=2, padx = 20)

weight_text = Label(text="ВЕС", font='bold', width=8, height=1, bg="white")
weight_text.grid(row=0, column=3)
weight_entry = Entry(text="55", font='bold', width=8, bg="white")
weight_entry.grid(row=0, column=4, pady=20)

othet = Label(text='', font='bold', width=62, height=6, bg='gray')
othet.grid(row=2, column=0, columnspan=5)

root.mainloop()