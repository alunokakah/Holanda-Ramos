import pyttsx3
import tkinter as tk
from tkinter import filedialog

# Função para inicializar o motor de voz
def inicializar_motor():
    engine = pyttsx3.init()
    
    # Personalizar a voz
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Escolher uma voz feminina (opcional)
    
    # Personalizar a velocidade da voz (padrão é 200)
    engine.setProperty('rate', 150)  # 150 palavras por minuto
    
    # Personalizar o volume (0.0 a 1.0)
    engine.setProperty('volume', 1.0)  # Volume máximo
    return engine

# Função para falar o texto
def falar(texto):
    engine = inicializar_motor()
    engine.say(texto)
    engine.runAndWait()

# Função para ler o texto inserido pelo usuário
def ler_texto():
    texto = texto_entry.get("1.0", tk.END).strip()  # Obtém o texto da caixa de texto
    if texto:
        falar(texto)
    else:
        resultado_label.config(text="Por favor, insira um texto para ler.")

# Função para carregar um arquivo de texto
def carregar_arquivo():
    arquivo_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if arquivo_path:
        with open(arquivo_path, "r") as file:
            texto = file.read()
            texto_entry.delete("1.0", tk.END)
            texto_entry.insert(tk.END, texto)

# Configurando a janela principal
root = tk.Tk()
root.title("Leitor de Texto em Voz Alta")

# Rótulo de instrução
instrucoes_label = tk.Label(root, text="Digite ou carregue um texto para ser lido:", font=("Arial", 12))
instrucoes_label.pack(pady=10)

# Caixa de texto para inserção de texto manual
texto_entry = tk.Text(root, height=10, width=50)
texto_entry.pack(padx=10, pady=10)

# Botão para ler o texto
ler_button = tk.Button(root, text="Ler Texto", command=ler_texto, width=20, height=2)
ler_button.pack(pady=5)

# Botão para carregar arquivo
carregar_button = tk.Button(root, text="Carregar Arquivo", command=carregar_arquivo, width=20, height=2)
carregar_button.pack(pady=5)

# Rótulo para mostrar resultados
resultado_label = tk.Label(root, text="", font=("Arial", 10))
resultado_label.pack(pady=10)

# Iniciando a interface gráfica
root.mainloop()