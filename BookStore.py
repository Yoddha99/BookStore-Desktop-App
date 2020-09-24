"""
A program that stores book info: 
title, author
year, isbn

user can: 
                view all records
 LISTBOX        search an entry
           s    add entry
           c    update entry
           r    delete 
           o    close
           l
           l
"""

from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window = Tk()

window.wm_title("BookStore")

window['bg'] = '#9566ed'

l1 = Label( window, text="Title", background="#9566ed", fg='white', font='Helvetica 10 bold')

l1.grid(row=0,column=0)

l2 = Label( window, text="Author", background="#9566ed", fg='white', font='Helvetica 10 bold')
l2.grid(row=0,column=2)

l3 = Label( window, text="Year", background="#9566ed", fg='white', font='Helvetica 10 bold')
l3.grid(row=1,column=0)

l4 = Label( window, text="ISBN", background="#9566ed", fg='white', font='Helvetica 10 bold')
l4.grid(row=1,column=2)



title_text = StringVar()
e1 = Entry(window, textvariable = title_text, fg='black', bg='#9566ed', relief='groove', font = "Helvetica 12")
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text, fg='black', bg='#9566ed', relief='groove', font = "Helvetica 12")
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text, fg='black', bg='#9566ed', relief='groove', font = "Helvetica 12")
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text, fg='black', bg='#9566ed', relief='groove', font = "Helvetica 12")
e4.grid(row = 1, column = 3)



list1 = Listbox(window, height = 8, width=32, font="Helvetica 10")
list1.grid(row = 2, column = 0, rowspan = 7, columnspan = 2, padx = '9')

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 7)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width = 14, bg='#b9f054', fg="blue" , font='Helvetica 9', command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text="Search Entry", width = 14, bg='#b9f054', fg="blue", font='Helvetica 9', command=search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text="Add Entry", width = 14, bg='#b9f054', fg="blue", font='Helvetica 9', command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text="Update Selected", width = 14, bg='#b9f054', fg="blue", font='Helvetica 9', command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text="Delete Selected", width = 14, bg='#b9f054', fg="blue", font='Helvetica 9', command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text="Close", width = 14, bg='#b9f054', fg="blue", font='Helvetica 9', command=window.destroy)
b6.grid(row = 7, column = 3)



window.mainloop()