"""
Convertisseur Texte -> Base64
Application Python avec interface graphique Tkinter
Démonstration de toutes les étapes : Texte ASCII -> Binaire -> Groupes 6-bits -> Base64
Auteur : Pierre DEFAUQUET
Date : 23/07/2025
"""

# === IMPORTS ===
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import base64

class TextToBase64App:
    """
    Application de conversion de texte en Base64.
    Montre chaque étape du processus de conversion.
    """

    def __inti__(self, root):
        """
        Constructeur de l'application.
        """
        self.root = root
        self.root.title("Convertisseur Texte -> Base64")
        self.root.geometry("900x700")
        self.root.resizable(True, True)

        # Table Base64 (A-Z, a-z, 0-9, +, /)
        self.base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

        #Configuration dus tyle
        self.setup_styles()

        # Création de l'interface
        self.create_widgets()

    def setup_styles(self):
        """
        Configure l'apparence de l'application
        """
        self.root.configure(bg='#f8f9fa')

        #styles pour les boutons
        style = ttk.Style()
        style.configure('Convert.TButton',
                        font=('Arial', 12, 'bold'),
                        padding=(20, 10))
        style.configure('Action.TButton',
                        font=('Arial', 10),
                        padding=(8, 4))
        
    def create_widgets(self):
        """
        Crée tous les éléments de l'interface graphique.
        """
        # === TITRE PRINCIPAL ===
        title_label = tk.Label(
            self.root,
            text= "🔄 Convertisseur Texte -> Base64",
            font=('Arial', 16, 'bold'),
            bg='#f8f9fa',
            fg='#2c3e50'
        )
        title_label.pack(pady=15)

        # === FRAME PRINCIPALE ===
        main_frame = tk.Frame(self.root, bg='#f8f9fa')
        main_frame.pack(pady=5, padx=15, fill='both', expand=True)

        # === SECTION SAISIE ===
        input_frame = tk.LabelFrame(
            main_frame,
            text="📝 Texte d'entrée",
            font=('Arial', 11, 'bold'),
            bg='#f8f9fa',
            fg="#34495e",
            padx=10,
            pady=5
        )
        input_frame.pack(fill='x', pady=(0,10))

        self.text_input.pack(side='left', padx=(0, 10), pady=5)
        self.text_input.insert(0, "Bonjour le monde !")

        # === BOUTONS D'ACTION ===
        buttons_frame = tk.Frame(input_frame, bg='#f8f9fa')
        buttons_frame.pack(side='right', pady=5)

        convert_button = ttk.Button(
            buttons_frame,
            text="🔄 Convertir",
            style='Convert.TButton',
            command=self.convert_step_by_step
        )
        convert_button.pack(side='left', padx=2)

        clear_button = ttk.Button(
            buttons_frame,
            text="🗑️ Effacer",
            style='Action.TButton',
            command=self.clear_all
        )
        clear_button.pack(side='left', padx=2)

        example_button = ttk.Button(
            buttons_frame,
            text="📄 Exemple",
            style='Action.TButton',
            command=self.load_example
        )
        example_button.pack(side='left', padx=2)

        # === CRÉATION DU NOTEBOOK POUR LES ÉTAPES ===
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill='both', expand=True, pady=5)

        # === ÉTAPE 1 : TEXTE -> ASCII ===
        step1_frame = tk.Frame(notebook, bg='white')
        notebook.add(step1_frame, text="🔤 1. Texte -> ASCII")

        step1_title = tk.Label(
            step1_frame,
            text="📝 ÉTAPE 1 : Conversion Texte -> Codes ASCII",
            font=('Arial', 12, 'bold'),
            bg='white',
            fg='#e74c3c'
        )
        step1_title.pack(pady=10)

        self.step1_result = scrolledtext.ScrolledText(
            step1_frame,
            font=('Courier', 10),
            height=12,
            bg='#fdf2f2',
            fg='#2c3e50',
            state=tk.DISABLED
        )
        self.step1_result.pack(fill='both', expand=True, padx=10, pady=5)

        # === ÉTAPE 2 : ASCII -> BINAIRE ===
        step2_frame = tk.Frame(notebook, bg='white')
        notebook.add(step2_frame, text="🔢 2. ASCII -> BINAIRE")

        step2_title = tk.Label(
            step2_frame,
            text="🔢 ÉTAPE 2 : Conversion Codes ASCII -> Binaire (8 bits par caractère)",
            font=('Arial', 12, 'bold'),
            bg='white',
            fg='#f39c12'
        )
        step2_title.pack(pady=10)

        self.step2_result = scrolledtext.ScrolledText(
            step2_frame,
            font=('Courier', 10),
            height=12,
            bg='#fef9e7',
            fg='#2c3e50',
            state=tk.DISABLED
        )
        self.step2_result.pack(fill='both', expand=True, padx=10, pady=5)

        