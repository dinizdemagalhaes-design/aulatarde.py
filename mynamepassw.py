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

def enviar():
    email = entrada_email.get()
    senha = entrada_senha.get()

    label_resultado_email.config(text=f"Email: {email}")
    label_resultado_senha.config(text=f"Senha: {senha}")


janela = tk.Tk()
janela.title("Ler Entry")
janela.geometry("500x300")

# Frame superior
frame_topo = tk.Frame(janela, bg="lightgreen")
frame_topo.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.4)

# Label Email
label_email = tk.Label(frame_topo, text="Digite seu email:", bg="lightgreen")
label_email.place(relx=0.05, rely=0.2)

# Entry Email
entrada_email = tk.Entry(frame_topo)
entrada_email.place(relx=0.5, rely=0.2, relwidth=0.4)

# Label Senha
label_senha = tk.Label(frame_topo, text="Digite sua senha:", bg="lightgreen")
label_senha.place(relx=0.05, rely=0.5)

# Entry Senha
entrada_senha = tk.Entry(frame_topo, show="*")
entrada_senha.place(relx=0.5, rely=0.5, relwidth=0.4)

# Botão
botao = tk.Button(frame_topo, text="Submit", bg="darkgreen", fg="white", command=enviar)
botao.place(relx=0.3, rely=0.75, relwidth=0.4)

# Frame inferior
frame_baixo = tk.Frame(janela, bg="lightgreen")
frame_baixo.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)

# Resultado Email
label_resultado_email = tk.Label(frame_baixo, text="Email:", bg="lightgreen")
label_resultado_email.place(relx=0.3, rely=0.2)

# Resultado Senha
label_resultado_senha = tk.Label(frame_baixo, text="Senha:", bg="lightgreen")
label_resultado_senha.place(relx=0.3, rely=0.5)

janela.mainloop()
