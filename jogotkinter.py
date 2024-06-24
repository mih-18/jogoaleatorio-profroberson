import tkinter as tk
from tkinter import messagebox
import random

class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação")
        
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 10
        self.tentativas_usadas = 0
        
        self.label = tk.Label(root, text="Tente adivinhar o número entre 1 e 100.")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.button = tk.Button(root, text="Adivinhar", command=self.adivinhar)
        self.button.pack()
        
        self.tentativas_label = tk.Label(root, text=f"Tentativas restantes: {self.tentativas}")
        self.tentativas_label.pack()

    def adivinhar(self):
        try:
            palpite = int(self.entry.get())
        except ValueError:
            messagebox.showwarning("Entrada inválida", "Por favor, insira um número válido.")
            return
        
        self.tentativas_usadas += 1
        self.tentativas -= 1
        
        if palpite == self.numero_secreto:
            messagebox.showinfo("Parabéns!", f"Você adivinhou o número {self.numero_secreto} em {self.tentativas_usadas} tentativas.")
            self.resetar_jogo()
        elif palpite < self.numero_secreto:
            messagebox.showinfo("Muito baixo!", "Seu palpite foi muito baixo.")
        else:
            messagebox.showinfo("Muito alto!", "Seu palpite foi muito alto.")
        
        if self.tentativas == 0:
            messagebox.showinfo("Fim de jogo", f"Você não conseguiu adivinhar o número. O número correto era {self.numero_secreto}.")
            self.resetar_jogo()
        
        self.tentativas_label.config(text=f"Tentativas restantes: {self.tentativas}")
        self.entry.delete(0, tk.END)
    
    def resetar_jogo(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 10
        self.tentativas_usadas = 0
        self.tentativas_label.config(text=f"Tentativas restantes: {self.tentativas}")

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoAdivinhacao(root)
    root.mainloop()
