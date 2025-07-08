import tkinter as tk
from tkinter import filedialog, messagebox
from MotorDeVoz import criar_engine
#Função para escolher arquivo .txt
def carregar_arquivo(entrada_texto):
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt")])
    if caminho:
        with open(caminho, 'r', encoding='utf-8') as f:
            entrada_texto.delete("1.0", tk.END)
            entrada_texto.insert(tk.END, f.read())
#Converter texto em áudio
def converter_texto(texto, voz_tipo, velocidade, formato):
    if not texto.strip():
        messagebox.showwarning("Aviso", "Digite ou carregue o texto.")
        return

    engine = criar_engine(voz_tipo, velocidade)
    arquivo = filedialog.asksaveasfilename(defaultextension=f".{formato}", filetypes=[(f"Áudio (*.{formato})", f"*.{formato}")])

    if arquivo:
        engine.save_to_file(texto, arquivo)
        engine.runAndWait()
        messagebox.showinfo("Sucesso",f"Áudio salvov como {arquivo}")  