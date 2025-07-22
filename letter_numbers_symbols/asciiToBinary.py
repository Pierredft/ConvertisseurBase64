"""
Convertisseur ASCII -> Binaire
Application Python avec interface graphique Tkinter
Auteur : Pierre Defauquet
Date : 2023-10-15
version : 1.0
"""

# === IMPORTS ===
import tkinter as tk
from tkinter import ttk, messagebox

class ASCIIToBinaryApp:
    """ 
    Application de conversion ASCII vers Binaire
    Prend un code ASCII (0-127) et le convertit en binaire
    """

    def __inti__(self, root):
        """
        Constructeur de l'application ASCII -> Binaire
        """
        self.root = root
        self.root.title("Convertisseur ASCII -> Binaire")
        self.root.geometry("450x350")
        self.root.resizable(False, False) # Ne pas redimensionner la fenêtre

        # Configuration du style
        self.setup_styles()
        # Création de l'interface
        self.create_widgets()

    def setup_styles(self):
        """ 
        Crée tous les éléments de l'interface graphique
        """
        # === TITRE PRINCIPAL ===
        title_label = tk.Label(
            self.root,
            text="🔤 Convertisseur ASCII -> Binaire",
            font=('Arial', 18, 'bold'),
            bg="#F0F0F0",
            fg='#333333'
        )
        title_label.pack(pady=20)

        # === FRAME PRINCIPAL ===
        main_frame = tk.Frame(self.root, bg='#f5f5f5')
        main_frame.pack(pady=10, padx=30, fill='both', expand=True)

        # === SECTION SAISIE ASCII ===
        input_section = tk.Frame(main_frame, bg='#f5f5f5')
        input_section.pack(pady=10, fill='x')

        input_label = tk.Label(
            input_section,
            text="Entrez un code ASCII (0-127) : ",
            font=('Arial', 12, 'bold'),
            bg='#f5f5f5',
            fg='#34495e'
        )
        input_label.pack(pady=(0, 8))

        # champ de saisie avec validation
        self.ascii_var = tk.StringVar()
        self.ascii_entry = tk.Entry(
            input_section,
            textvariable=self.ascii_var,
            font=('Arial', 14),
            width=15,
            justify='center',
            validate='key',
            validatecommand=(self.root.register(self.validate_ascii_input), '%P')
        )
        self.ascii_entry.pack(pady=5)
        self.ascii_entry.focus()

        # Info sur la plage valide
        info_range = tk.Label(
            input_section,
            text="💡 Plage valide : 0 à 127 (ASCII standard)",
            font=('Arial', 9),
            bg='#f5f5f5',
            fg='#7f8c8d'
        )
        info_range.pack(pady=(5,0))
