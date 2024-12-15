#APP VER 1.0.0
#
#===APPLICATION OVERVIEW===
#An application that stores promising candidates for future recruiting needs.
#It displays a list filled with each candidates' attributes, including:
#1. Name
#2. Gender 
#3. Birth year
#4. Position
#5. Which department is the said position in
#6. Asked salary or salary range
#
#The user will be able to:
#1. View all entries/candidates.
#2. Search entries/candidates based on their attributes listed above.
#3. Add entries/candidates.
#4. Update selected entries/candidates.
#5. Delete selected entries/candidates.
#6. Close the application


from tkinter import *
import Recruiting_app_backend
import ttkbootstrap as ttk
from ttkbootstrap.constants import * 


def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        name_entry.delete(0,END)
        name_entry.insert(END,selected_tuple[1])
        gender_entry.delete(0,END)
        gender_entry.insert(END,selected_tuple[2])
        by_entry.delete(0,END)
        by_entry.insert(END,selected_tuple[3])
        pos_entry.delete(0,END)
        pos_entry.insert(END,selected_tuple[4])
        dept_entry.delete(0,END)
        dept_entry.insert(END,selected_tuple[5])
        salrange_entry.delete(0,END)
        salrange_entry.insert(END,selected_tuple[6])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in Recruiting_app_backend.view_entry():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in Recruiting_app_backend.search_entry(name_text.get(),gender_text.get(),by_text.get(),pos_text.get(),dept_text.get(),salrange_text.get()):
        list1.insert(END,row)

def add_command():
    Recruiting_app_backend.add_entry(name_text.get(),gender_text.get(),by_text.get(),pos_text.get(),dept_text.get(),salrange_text.get())
    list1.delete(0,END)
    #list1.insert(END,(name_text.get(),gender_text.get(),by_text.get(),pos_text.get(),dept_text.get(),salrange_text.get()))
    name_entry.delete(0,END)
    gender_entry.delete(0,END)
    by_entry.delete(0,END)
    pos_entry.delete(0,END)
    dept_entry.delete(0,END)
    salrange_entry.delete(0,END)
    for row in Recruiting_app_backend.view_entry():
        list1.insert(END, row)

def delete_command():
    Recruiting_app_backend.delete_entry(selected_tuple[0])
    list1.delete(0,END)
    name_entry.delete(0,END)
    gender_entry.delete(0,END)
    by_entry.delete(0,END)
    pos_entry.delete(0,END)
    dept_entry.delete(0,END)
    salrange_entry.delete(0,END)
    for row in Recruiting_app_backend.view_entry():
        list1.insert(END, row)

def update_command():
    Recruiting_app_backend.update_entry(selected_tuple[0],name_text.get(),gender_text.get(),by_text.get(),pos_text.get(),dept_text.get(),salrange_text.get())
    list1.delete(0,END)
    name_entry.delete(0,END)
    gender_entry.delete(0,END)
    by_entry.delete(0,END)
    pos_entry.delete(0,END)
    dept_entry.delete(0,END)
    salrange_entry.delete(0,END)
    for row in Recruiting_app_backend.view_entry():
        list1.insert(END, row)


theme = "darkly"
window = ttk.Window(themename=theme)
window.title("Recruitment App")

custom_font1 = ("Calibri", 11)
custom_font2 = ("Calibri", 11, "bold")

name_label = Label(window, text="Name", font=custom_font2)
name_label.grid(row=0, column=0, padx=(40,20), pady=(20,0))

name_text = StringVar()
name_entry = Entry(window, textvariable=name_text, font=custom_font1)
name_entry.grid(row=0, column=1, padx=(20,20), pady=(20,0))

gender_label = Label(window, text="Gender", font=custom_font2)
gender_label.grid(row=0, column=2, padx=(20,20), pady=(20,0))

gender_text = StringVar()
gender_entry = Entry(window, textvariable=gender_text, font=custom_font1)
gender_entry.grid(row=0, column=3, padx=(20,20), pady=(20,0))

by_label = Label(window, text="Birth Year", font=custom_font2)
by_label.grid(row=0, column=4, padx=(20,20), pady=(20,0))

by_text = StringVar()
by_entry = Entry(window, textvariable=by_text, font=custom_font1)
by_entry.grid(row=0, column=5, padx=(20,20), pady=(20,0))

pos_label = Label(window, text="Position", font=custom_font2)
pos_label.grid(row=1, column=0, padx=(40,20), pady=(10,0))

pos_text = StringVar()
pos_entry = Entry(window, textvariable=pos_text, font=custom_font1)
pos_entry.grid(row=1, column=1, padx=(20,20))

dept_label = Label(window, text="Department", font=custom_font2)
dept_label.grid(row=1, column=2, padx=(20,20))

dept_text = StringVar()
dept_entry = Entry(window, textvariable=dept_text, font=custom_font1)
dept_entry.grid(row=1, column=3, padx=(20,20))

salrange_label = Label(window, text="Salary Range", font=custom_font2)
salrange_label.grid(row=1, column=4, padx=(20,20))

salrange_text = StringVar()
salrange_entry = Entry(window, textvariable=salrange_text, font=custom_font1)
salrange_entry.grid(row=1, column=5, padx=(20,20))


view_button = ttk.Button(window, text="View All", width=14, bootstyle=PRIMARY,command=view_command)
view_button.grid(row=3, column=5, sticky='n', pady=(30,0))

search_button = ttk.Button(window, text="Search Entry", width=14, bootstyle=PRIMARY,command=search_command)
search_button.grid(row=4, column=5, sticky='n')

add_button = ttk.Button(window, text="Add Entry", width=14, bootstyle=PRIMARY,command=add_command)
add_button.grid(row=5, column=5, sticky='n')

update_button = ttk.Button(window, text="Update Selected", width=14, bootstyle=PRIMARY,command=update_command)
update_button.grid(row=6, column=5, sticky='n')

delete_button = ttk.Button(window, text="Delete Selected", width=14, bootstyle=PRIMARY, command=delete_command)
delete_button.grid(row=7, column=5, sticky='n')

close_button = ttk.Button(window, text="Close", width=14, bootstyle=DANGER, command=window.destroy)
close_button.grid(row=8, column=5, sticky='n', pady=(0,20))


list1=Listbox(window, height=15, width=80, font=custom_font1)
list1.grid(row=3, column=0, rowspan=6, columnspan=4,padx=(30,0),pady=(20,20))

sb1=Scrollbar(window)
sb1.grid(row=3, column=4, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)


#So that it immediately shows the list when user opens up the window.
for row in Recruiting_app_backend.view_entry():
        list1.insert(END, row)

window.mainloop()


#This application is a test project and im fully aware that some of the features can really be improved upon for its functionality and practicality.
#However, the main goal of this project is only to grasp my capabilities in python and postgresql so far.
#P.S.: Should probably use treeview and sqlite next time.
