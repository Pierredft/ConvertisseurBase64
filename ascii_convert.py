"""
VERSION ALTERNATIVE - Affichage flexible
Cette version adapte automatiquement la taille selon le contenu
"""

import tkinter as tk
from tkinter import ttk, messagebox

class ConvertApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertisseur Lettre -> ASCII")
        self.root.geometry("400x320")  # Légèrement plus haut
        self.root.resizable(False, False)

        self.setup_style()
        self.create_widgets()

    def setup_style(self):
        self.root.configure(bg='#f0f0f0')
        style = ttk.Style()
        style.configure('Custom.TButton',
                        font=('Arial',12, 'bold'),
                        padding=(10,5))
    
    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="🔤 Convertisseur Lettre -> ASCII",
            font=('Arial', 16, 'bold'),
            bg="#F0F0F0",
            fg='#333333'
        )
        title_label.pack(pady=20)

        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(pady=10, padx=20, fill='both', expand=True)

        input_label = tk.Label(
            main_frame,
            text="Entrez une lettre :",
            font=('Arial', 12),
            bg='#f0f0f0'
        )
        input_label.pack(pady=(0,5))

        self.letter_var = tk.StringVar()
        self.letter_entry = tk.Entry(
            main_frame,
            textvariable=self.letter_var,
            font=('Arial', 14),
            width=10,
            justify='center',
            validate='key',
            validatecommand=(self.root.register(self.validate_input), '%P')
        )
        self.letter_entry.pack(pady=5)
        self.letter_entry.focus()

        convert_button = ttk.Button(
            main_frame,
            text="🔄 Convertir",
            style='Custom.TButton',
            command=self.convert_letter
        )
        convert_button.pack(pady=15)

        result_label = tk.Label (
            main_frame,
            text='Résultat :',
            font=('Arial', 12),
            bg='#f0f0f0'
        )
        result_label.pack(pady=(10, 5))

        # VERSION FLEXIBLE - le frame s'adapte au contenu
        result_frame = tk.Frame(
            main_frame,
            bg='white',
            relief='ridge',
            borderwidth=2
        )
        result_frame.pack(pady=5, padx=20, fill='x')
        # PAS de pack_propagate(False) -> le frame s'adapte

        self.result_label = tk.Label(
            result_frame,
            text='Aucune conversion effectuée',
            font=('Arial', 12, 'bold'),
            bg='white',
            fg='#666666',
            pady=15,  # Padding généreux
            wraplength=300,
            justify='center'
        )
        self.result_label.pack()

        clear_button = ttk.Button(
            main_frame,
            text="🗑️ Effacer",
            command=self.clear_input
        )
        clear_button.pack(pady=10)

        info_label = tk.Label(
            main_frame,
            text="💡 ASCII : American Standard Code for Information Interchange",
            font=('Arial', 9),
            bg='#f0f0f0',
            fg='#888888'
        )
        info_label.pack(side='bottom', pady=(20, 0))

    def validate_input(self, value):
        if value == "":
            return True
        
        if len(value) > 1:  # CORRECTION du bug
            return False
        
        if len(value) == 1 and value.isalpha():
            return True
        
        return False
    
    def convert_letter(self):
        letter = self.letter_var.get().strip()

        if not letter:
            messagebox.showwarning(
                "Attention",
                "Veuillez saisir une lettre avant de convertir !"
            )
            self.letter_entry.focus()
            return
        
        ascii_code = ord(letter)

        if letter.isupper():
            category = "majuscule"
        else:
            category = "minuscule"

        # Affichage sur 2 lignes clairement séparées
        self.result_label.config(
            text=f"'{letter}' -> {ascii_code}\n(lettre {category})",
            fg='#2c5aa0',
            font=('Arial', 12, 'bold')
        )

        print(f"Conversion effectuée : {letter} = {ascii_code}")

    def clear_input(self):
        self.letter_var.set("")
        self.result_label.config(
            text="Aucune conversion effectuée",
            fg='#666666'
        )
        self.letter_entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = ConvertApp(root)
    root.mainloop()
    print("Application fermée. Merci d'avoir utilisé le convertisseur !")