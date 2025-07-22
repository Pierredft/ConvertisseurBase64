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

        