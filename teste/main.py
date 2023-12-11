# from tkinter import *

# janela = Tk()
# label = Label(janela, text='Menu Principal')
# label.pack()


# def criar_usuario():
#     global janela
#     janela.destroy()
#     janela = Tk() 
#     label = Label(janela, text='Criar Usuario')
#     label.pack()
#     janela.geometry("600x600+250+50")
#     menu_bt = Button(janela, text='Voltar/Menur',command=menu)
#     menu_bt.pack()


# def editar_usuario():
#     global janela
#     janela.destroy()
#     janela = Tk() 
#     label = Label(janela, text='Editar Usuario')
#     label.pack()
#     janela.geometry("600x600+250+50")
#     menu_bt = Button(janela, text='Voltar/Menur',command=menu)
#     menu_bt.pack()


# def menu():
#     global janela
#     janela.destroy()
#     janela = Tk()

#     label = Label(janela, text='Menu Principal')
#     label.pack()

#     menu_bt_criar = Button(janela, text='Criar Usuario',command=criar_usuario)
#     menu_bt_edituser = Button(janela, text='Editar Usuario',command=editar_usuario)

#     menu_bt_criar.place(x=30,y=100)
#     menu_bt_edituser.place(x=30,y=130)

#     janela.geometry("600x600+250+50")
#     janela.title("Menu Principal")

#     janela.mainloop()


# menu_bt_criar = Button(janela, text='Criar Usuario',command=criar_usuario)
# menu_bt_edituser = Button(janela, text='Editar Usuario',command=editar_usuario)

# menu_bt_criar.place(x=30,y=100)
# menu_bt_edituser.place(x=30,y=130)

# janela.geometry("600x600+250+50")
# janela.title("Menu Principal")

# janela.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200')

# define columns
columns = ('Album', 'Cantor', 'Ano', 'Lancamento?')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('Album', text='Album')
tree.heading('Cantor', text='Cantor')
tree.heading('Ano', text='Ano')
tree.heading('Lancamento?', text='Lancamento?')

# generate sample data
contacts = []
for n in range(1, 100):
    contacts.append((f'first {n}', f'last {n}', f'Ano{n}@example.com'))

# add data to the treeview
for contact in contacts:
    tree.insert('', tk.END, values=contact)


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()