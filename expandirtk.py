import tkinter as tk


'''Estrutura do projeto'''
root = tk.Tk()
root.title("Esstrutura base")
root.geometry("600x400")

'''Linhas da janela para aumentar'''
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

'''Colunas da janela para aumentar'''
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=3)

'''Criar Frame esquerdo'''
frame_esquerdo = tk.Frame(root, bg="ligthblue")
frame_esquerdo.grid(row=0, column=0, rowspan=2, sticky="nsew")

'''Criar texto esquerdo'''
label_esquerdo = tk.Label(frame_esquerdo, text="Frame Esquerdo")
label_esquerdo.pack(expand=True)

'''Criar frame direito'''
frame_centro = tk.Frame(root, bg="lightgreen")
frame_centro.grid(row=0,column=1, sticky="nsew")

'''Criar texto do frame direito'''
label_centro = tk.Label(frame_centro, text= "Frame direito")
label_centro.pack(expand=True)

'''Criar frame inferior direito'''
frame_inferior = tk.Frame(root, bg="yelow")
frame_inferior.grid(row=1, column=1, sticky="nsew")

'''Texto inferior direito'''
label_inferior = tk.Label(frame_inferior, text="Frame Inferior")
label_inferior.pack(expand=True)


root.mainloop
