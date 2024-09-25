import customtkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
import database


# Fonction pour ajouter un employé
def add_employee():
    employee_id = id_entry.get()
    employee_name = name_entry.get()
    employee_role = role_entry.get()
    employee_gender = gender_options.get()
    employee_status = status_entry.get()

    if not (employee_id and employee_name and employee_role and employee_gender and employee_status):
           messagebox.showerror('Error','Enter All filds')
    elif database.id_exists(employee_id):
         messagebox.showerror('Error','Id already exists')
    else:
         database.insert_employees(employee_id, employee_name, employee_role, employee_gender, employee_status)
         add_to_treeview()
         messagebox.showerror('Success','Data been inserted')
         


# Fonction pour réinitialiser le formulaire
#def clear_form(*clicked):
def clear_form(*clicked):
    if clicked :
         tree.selection_remove(tree.focus())
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    role_entry.delete(0, END)
    gender_options.set('Male')
    status_entry.delete(0, END)

def display_data(event):
     select_item = tree.focus()
     if select_item:
          row = tree.item(select_item)['values']
          clear_form()
          id_entry.insert(0,row[0])
          name_entry.insert(0,row[1])
          role_entry.insert(0,row[2])
          Variable1.set(row[3])
          status_entry.insert(0,row[4])
     else:
          pass

# Fonction pour mettre à jour un employé
def update_employee():
    select_item = tree.focus
    if not select_item:
        messagebox.showerror("errors","selectionner une ")
    else: 
       id = id_entry.get() 
       name = name_entry.get()
       role = role_entry.get()
       gender = Variable1.get()
       status = status_entry.get()
       database.update_employees(name,role,gender,status,id)
       add_to_treeview()
       clear_form()
       messagebox.showinfo("Update", "Employee updated successfully!")
 

# Fonction pour supprimer un employé
def delete_employee():
    select_item = tree.focus
    if not select_item:
         messagebox.showerror("errors","selectionner une ")
    else: 
      id = id_entry.get() 
      database.delete_employees(id)
      add_to_treeview()
      clear_form()
      messagebox.showinfo("Delete", "Employee deleted successfully!")

app = customtkinter.CTk()
app.title('Employee Management System')
app.geometry('900x420')
app.config(bg='#161c25')
app.resizable(False, False)



font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 10, 'bold')

def add_to_treeview():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)

# ID Label and Entry
id_label = customtkinter.CTkLabel(app, font=font1, text='ID:', text_color='#fff', bg_color='#161C25')
id_label.place(x=20, y=20)

id_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
id_entry.place(x=100, y=20)

# Name Label and Entry
name_label = customtkinter.CTkLabel(app, font=font1, text='Name:', text_color='#fff', bg_color='#161C25')
name_label.place(x=20, y=80)

name_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
name_entry.place(x=100, y=80)

# Role Label and Entry
role_label = customtkinter.CTkLabel(app, font=font1, text='Role:', text_color='#fff', bg_color='#161C25')
role_label.place(x=20, y=140)

role_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
role_entry.place(x=100, y=140)

# Gender Label and ComboBox
gender_label = customtkinter.CTkLabel(app, font=font1, text='Gender:', text_color='#fff', bg_color='#161C25')
gender_label.place(x=20, y=200)

option = ['Male', 'Female']
Variable1 = StringVar()

gender_options = customtkinter.CTkComboBox(app, font=font1, text_color='#000', fg_color='#fff', dropdown_hover_color='#0C9295', button_color='#0C9295', button_hover_color='#0C9295', border_color='#0C9295', width=180, variable=Variable1, values=option, state='readonly')
gender_options.set('Male')
gender_options.place(x=100, y=200)

# Status Label and Entry
status_label = customtkinter.CTkLabel(app, font=font1, text='Status:', text_color='#fff', bg_color='#161C25')
status_label.place(x=20, y=260)

status_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
status_entry.place(x=100, y=260)

# Add Employee Button
add_button = customtkinter.CTkButton(app, font=font1, text_color='#fff', text='Add Employee', fg_color='#05A312', hover_color='#00850B', bg_color='#161C25', cursor='hand2', corner_radius=15, width=260, command=add_employee)
add_button.place(x=20, y=310)

# New Employee Button
clear_button = customtkinter.CTkButton(app, font=font1, text_color='#fff', text='New Employee', fg_color='#161C25', hover_color='#FF5002', bg_color='#161C25', border_color='#F15704', border_width=2, cursor='hand2', corner_radius=15, width=260, command=lambda:clear_form(True))
clear_button.place(x=20, y=360)

# Update Employee Button
update_button = customtkinter.CTkButton(app, font=font1, text_color='#fff', text='Update Employee', fg_color='#161C25', hover_color='#FF5002', bg_color='#161C25', border_color='#F15704', border_width=2, cursor='hand2', corner_radius=15, width=260, command=update_employee)
update_button.place(x=300, y=360)

# Delete Employee Button
delete_button = customtkinter.CTkButton(app, font=font1, text_color='#fff', text='Delete Employee', fg_color='#E40404', hover_color='#AE0000', bg_color='#161C25', border_color='#E40404', border_width=2, cursor='hand2', corner_radius=15, width=260, command=delete_employee)
delete_button.place(x=580, y=360)

style = ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview', font=font2, foreground='#fff', background='#1A1A1A', fieldbackground='#1A1A1A')
style.map('Treeview', background=[('selected', '#1A8FeD')])

tree = ttk.Treeview(app, height=15)

# Configuration des colonnes
tree['columns'] = ('ID', 'Name', 'Role', 'Gender', 'Status')
tree.column('#0', width=0, stretch=NO)  # Cache la première colonne inutilisée
tree.column('ID', anchor=CENTER, width=100)
tree.column('Name', anchor=CENTER, width=120)
tree.column('Role', anchor=CENTER, width=120)
tree.column('Gender', anchor=CENTER, width=100)
tree.column('Status', anchor=CENTER, width=120)

# Définition des en-têtes de colonnes
tree.heading('ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Role', text='Role', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Status', text='Status', anchor=CENTER)

# Placement du tableau
tree.place(x=300, y=20)
tree.bind('<ButtonRelease>', display_data)
add_to_treeview()


app.mainloop()
