import tkinter as tk
from interface import carregar_arquivo, converter_texto

#interface
janela = tk.Tk()
janela.title("Conversor de Texto para Áudio")
janela.geometry("600x500")

entrada_texto = tk.Text(janela, wrap=tk.WORD, height=15)
entrada_texto.pack(pady=10, padx=10)

#Botão para carregar
btn_carregar = tk.Button(janela, text="Carregar Arquivo .txt", command=lambda: carregar_arquivo(entrada_texto))
btn_carregar.pack(pady=5)

#voz
voz_var = tk.StringVar(value="feminina")
frame_voz = tk.Frame(janela)
tk.Label(frame_voz, text="Voz: ").pack(side=tk.LEFT)
tk.Radiobutton(frame_voz, text="Feminina", variable=voz_var, value="feminina").pack(side=tk.LEFT)
tk.Radiobutton(frame_voz, text="Masculina", variable=voz_var, value="masculina").pack(side=tk.LEFT)
frame_voz.pack(pady=5)


#Velocidade
vel_var = tk.DoubleVar(value=1.0)
frame_vel = tk.Frame(janela)
tk.Radiobutton(frame_vel, text="Normal", variable=vel_var, value=1.0).pack(side=tk.LEFT)
tk.Radiobutton(frame_vel, text="1.5x (Rápida)", variable=vel_var, value=1.5).pack(side=tk.LEFT)
tk.Radiobutton(frame_vel, text="0.7x (Lenta)", variable=vel_var, value=0.7).pack(side=tk.LEFT)
frame_vel.pack(pady=5)

#Formato
formato_var = tk.StringVar(value="mp3")
frame_fmt = tk.Frame(janela)
tk.Label(frame_fmt, text="Formato: ").pack(side=tk.LEFT)
tk.Radiobutton(frame_fmt, text=".mp3", variable=formato_var, value="mp3").pack(side=tk.LEFT)
tk.Radiobutton(frame_fmt, text=".wav", variable=formato_var, value="wav").pack(side=tk.LEFT)
frame_fmt.pack(pady=5)

#Botão para converter
btn_converter = tk.Button(
    janela,
    text="Converter e Salvar Áudio",
    command=lambda: converter_texto(
        entrada_texto.get("1.0", tk.END),
        voz_var.get(),
        vel_var.get(),
        formato_var.get()
    ),
    bg="#4CAF50", fg="white"
)
btn_converter.pack(pady=15)

janela.mainloop()
