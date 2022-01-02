import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox 
from tkinter import colorchooser
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import tkinter.messagebox

root = tk.Tk()

root.geometry('300x300')
root.title('Создание нового окна')

def createWin():
	def newWin():
		get = com.get()
		print(get)
		if get == 'Colorchooser':
			newWin = tk.Tk()

			newWin.geometry('300x300')
			newWin.title('TextEditor')
			WinSettings.destroy()
			root.destroy()


			def btnFunc():
				entry.config(state="normal")
				entry.delete(1,tk.END)

				s = colorchooser.askcolor()
				
				print(s[1])

				if s[1][0] in '#':
					entry.delete(0)

				color.configure(bg=s[1])
				entry.delete(1,tk.END)
				entry.insert(1,s[1])

				entry.config(state="readonly")

			lbl = tk.Label(newWin,text='HEX', justify='center')

			entry = tk.Entry(newWin,justify='center', bg='#a0a0a0')

			btn = tk.Button(newWin,text = 'Выберите цвет', bg='#fff', command=btnFunc,justify='center',width=20)

			lbl1 = tk.Label(newWin,text='Цвет который получился', justify='center')

			color = tk.Label(newWin,width = 20, justify='center')
			entry.config(state="readonly")

			lbl.pack()
			entry.pack()
			btn.pack(pady=10)
			lbl1.pack()
			color.pack(pady=10)
		if get == 'TextEditor':
			WinSettings.destroy()
			root.destroy()

			newWin = tk.Tk()

			screen_w = 800#newWin.winfo_screenwidth()
			screen_h = 600#newWin.winfo_screenheight()

			w = screen_w-15
			h = screen_h-85

			resolution = str(w)+'x'+str(h)

			newWin.geometry(resolution)

			menu = Menu(newWin)

			def Open():
				filename1 = filedialog.askopenfilename()
				file1 = open(filename1, 'r', encoding='utf8')

				message_text.delete("1.0", tk.END)
				
				for l in file1:
					message_text.insert(tk.END, l)

				file1.close()
				fileopen = Label(text=str(filename1), bg='yellow')
				fileopen.grid(column=1, row=1)
				btn_cls = tk.Button(text="Х", command=lambda: btn_cls_func())
				btn_cls.grid(column=3, row=1)

				def btn_cls_func():
					win_ext = Tk()

					label_ext = tk.Label(win_ext, text='Вы действительно хотите выйти?')
					label_ext.pack()
					frame = Frame(win_ext)
					yes_ext = tk.Button(frame,text='Да', command=lambda:ext()).grid(padx=10, column=1, row=0 , pady=2 , sticky="nsew")
					no_ext = tk.Button(frame,text='Нет', command=lambda:win_ext.destroy()).grid( row=0, padx=10 , pady=2 , sticky="nsew")
					frame.pack()

					def ext():
						btn_cls.destroy()
						
						try:
							Save()
						except AttributeError as error_data:
							pass

						fileopen.destroy()
						win_ext.destroy()
						message_text.delete('1.0', tk.END)

			def Save():
				file = asksaveasfile(
					mode='w',
					defaultextension=".txt",
					filetypes=(("text", "*.txt"), ("Python", ".py"), ("All files", "*"))	
					)

				text_for_save = message_text.get("1.0", tk.END)
				file.write(text_for_save)

				file.close()


			new_item = Menu(menu)
			new_item.add_command(label='Открыть', command=lambda: Open())
			new_item.add_command(label='Сохранить', command=lambda: Save())
			new_item.add_command(label='Выйти', command=lambda: newWin.destroy())
			menu.add_cascade(label='Файл', menu=new_item)
			newWin.config(menu=menu)

			message_text = Text(bg='light cyan', fg='black')
			message_text.place(relx=.5, rely=.5, anchor="c", height=h-100, width=w-30)


	WinSettings = tk.Tk()
	WinSettings.geometry('560x300')
	WinSettings.title('Настройка нового окна')
	lblHigh = tk.Label(WinSettings, text='Настройки окна', font='Times 30')
	lblHigh.place(x=150, y=0)
	lbl = tk.Label(WinSettings, text='Функция окна', font='Times 15')
	lbl.place(x=10, y=50)
	com = Combobox(WinSettings, values=('Colorchooser','TextEditor'))
	com.place(x=300, y=50)
	btn = tk.Button(WinSettings, text="Создать окно", command=newWin)
	btn.place(x=450, y=50)


btnNewWin = tk.Button(root, text = 'Create new window', command=createWin)
btnNewWin.pack()

root.mainloop()