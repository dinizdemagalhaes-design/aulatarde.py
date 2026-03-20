import tkinter as tk

root = tk.Tk()
root.title("Ler entry")
root.geometry("600x300")

#Estrutura ler senha
#Variáveis nome e senha
name_var = tk.StringVar
passw_var = tk.StringVar

#Definir função o nome e a senha
def submit():
    name = name_var.get()
    password = passw_var.get()

    print("The name is:" , name)
    print("The password is:", password)

    name_var.set('')
    passw_var.set('')

#Criando o Label para usar o nome e senha
name_label = tk.Label(root, text="Digite o seu e-mail",bg="lightgreen", font=("calibre", 10 , "normal"))
name_label.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.4)

#Entrada nome
name_entry = tk.Entry(root, textvariable=name_var,bg="lightgreen", font=("calibre", 10,  "normal" ))
name_entry.place(relx=0, rely=0.3, relheight=0.5)
#Label senha
passw_label=tk.Label(root, text="Senha", bg="light green", font=("calibre", 10, "normal"))
passw_label.place(relx=0.1, rely=0.5)
#Entrada senha
passw_entry = tk.Entry(root, textvariable=passw_var, bg="lightgreen", font=("calibre", 10, "normal"))
passw_entry.place( relwidth=0.1, relheight=0.5)
#Botão
sub_btn = tk.Button(root, text="Submit", command=submit)
sub_btn.place(relx=0.1, rely=0.75)


root.mainloop()





correct

import tkinter as tk

root = tk.Tk()
root.title("Ler entry")
root.geometry("600x300")

#Estrutura ler senha
#Variáveis nome e senha
name_var = tk.StringVar
passw_var = tk.StringVar

#Definir função o nome e a senha
def submit():
    name = name_var.get()
    password = passw_var.get()

    print("The name is:" , name)
    print("The password is:", password)

    name_var.set('')
    passw_var.set('')

#Criando o Label para usar o nome e senha
name_label = tk.Label(root, text="Digite o seu e-mail",bg="lightgreen", font=("calibre", 10 , "normal"))
name_label.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.4)

#Entrada nome
name_entry = tk.Entry(root, textvariable=name_var,bg="lightgreen", font=("calibre", 10,  "normal" ))
name_entry.place(relx=0, rely=0.3, relheight=0.5)
#Label senha
passw_label=tk.Label(root, text="Senha", bg="light green", font=("calibre", 10, "normal"))
passw_label.place(relx=0.1, rely=0.5)
#Entrada senha
passw_entry = tk.Entry(root, textvariable=passw_var, bg="lightgreen", font=("calibre", 10, "normal"))
passw_entry.place( relwidth=0.1, relheight=0.5)
#Botão
sub_btn = tk.Button(root, text="Submit", command=submit)
sub_btn.place(relx=0.1, rely=0.75)


root.mainloop()



