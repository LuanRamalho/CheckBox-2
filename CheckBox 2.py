from tkinter import *
from tkinter import ttk

# Configuração principal da janela
root = Tk()
root.title("Opções Selecionadas")
root.geometry("400x300")
root.configure(bg="#f0f8ff")

# Variáveis para os checkboxes
valor_checks = [IntVar() for _ in range(10)]

# Função para exibir opções selecionadas
def mostrar_selecionados():
    selecionados = []
    for i, valor in enumerate(valor_checks):
        if valor.get() == 1:
            selecionados.append(f"Opção {i + 1}")
    label_resultado.config(text=", ".join(selecionados) if selecionados else "Nenhuma opção selecionada")

# Título
titulo = Label(root, text="Escolha suas opções:", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#4682b4")
titulo.pack(pady=10)

# Frame para organizar os checkboxes
frame_checks = Frame(root, bg="#f0f8ff")
frame_checks.pack()

# Criação dos checkboxes com loop
cores_opcoes = ["#ffa07a", "#98fb98", "#afeeee", "#dda0dd", "#ffdab9", "#87cefa", "#ffc0cb", "#f0e68c", "#e6e6fa", "#ffb6c1"]
for i in range(10):
    check = Checkbutton(
        frame_checks, 
        text=f"Opção {i + 1}", 
        variable=valor_checks[i], 
        onvalue=1, offvalue=0, 
        command=mostrar_selecionados,
        font=("Arial", 10),
        bg=cores_opcoes[i % len(cores_opcoes)], 
        activebackground=cores_opcoes[i % len(cores_opcoes)]
    )
    check.grid(row=i // 2, column=i % 2, sticky="w", padx=10, pady=5)

# Label para mostrar o resultado
label_resultado = Label(root, text="Nenhuma opção selecionada", font=("Arial", 12, "italic"), bg="#f0f8ff", fg="#2f4f4f")
label_resultado.pack(pady=20)

root.mainloop()
