import tkinter as tk
from tkinter import messagebox
import Analyseur_lexical
import Analyseur_syntaxique
import interpreter

def execute_AnaLex():
    text = input_text.get("1.0", "end-1c")  # Récupère le texte de l'entrée

    result, error = Analyseur_lexical.run('<stdin>', text)

    if error:
        messagebox.showerror("Erreur", error.as_string())
    else:
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result)
        result_text.config(state=tk.DISABLED)


def execute_AnaSynt():
    text = input_text.get("1.0", "end-1c")  # Récupère le texte de l'entrée
    result, error = Analyseur_syntaxique.run('<stdin>', text)
    if error:
        messagebox.showerror("Erreur", error.as_string())
    else:
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result)
        result_text.config(state=tk.DISABLED)


def execute_interpreter():
    text = input_text.get("1.0", "end-1c")  # Récupère le texte de l'entrée

    result, error = interpreter.run('<stdin>', text)

    if error:
        messagebox.showerror("Erreur", error.as_string())
    else:
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result)
        result_text.config(state=tk.DISABLED)

        
# Crée la fenêtre principale
window = tk.Tk()
window.title("Micro-Compilateur Hatimique")

# Crée une étiquette pour le titre
title_label = tk.Label(window, text="Micro-Compilateur Hatimique", font=("Helvetica", 16))
title_label.pack(pady=10)

# Crée une zone de texte pour l'entrée
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="Entrée:", font=("Helvetica", 12))
input_label.pack(side=tk.LEFT)

input_text = tk.Text(input_frame, height=5, width=30)
input_text.pack(side=tk.LEFT)



analyze_lex_button = tk.Button(window, text="Analyse Lex", font=("Helvetica", 12), command=execute_AnaLex)
analyze_lex_button.pack(side=tk.LEFT, padx=5, pady=4)

analyze_synt_button = tk.Button(window, text="Analyse Synt", font=("Helvetica", 12), command=execute_AnaSynt)
analyze_synt_button.pack(side=tk.LEFT, padx=5, pady=10)

interpreter_button = tk.Button(window, text="Interpreter", font=("Helvetica", 12), command=execute_interpreter)
interpreter_button.pack(side=tk.LEFT, padx=5, pady=10)


# Crée une zone de texte pour afficher le résultat
result_frame = tk.Frame(window)
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, text="Résultat:", font=("Helvetica", 12))
result_label.pack()

result_text = tk.Text(result_frame, height=5, width=30)
result_text.config(state=tk.DISABLED)
result_text.pack()

# Lance la boucle principale de l'interface graphique
window.mainloop()
