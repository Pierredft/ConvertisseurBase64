"""
Convertisseur de Lettre, chiffres et symboles en ASCII
Version 1.0
Auteur : Pierre Defauquet
Date : 2023-10-15
"""

import tkinter as tk
from tkinter import ttk, messagebox

class ConvertApp:
    """
    Classe principale de l'application
    Elle va contenir toute la logique de l'interface et de la conversion
    """

    def __init__(self, root):
        """
        Constructeur : se lance automatiquement quand crée l'objet
        root = fenêtre principale de l'application
        """
        self.root = root
        self.root.title("Convertisseur Lettre, Chiffre et Symbole -> ASCII")
        self.root.geometry("800x450")
        self.root.resizable(False, False) # Ne pas redimensionner la fenêtre

        # Configuration du style
        self.setup_style()
        # Création de l'interface
        self.create_widgets()

    def setup_style(self):
        """
        Configure l'apparence de l'application
        """
        # Configuration de la couleur de fond
        self.root.configure(bg='#f0f0f0')
        # Style pour les boutons
        style = ttk.Style()
        style.configure('Custom.TButton',
                        font=('Arial',12, 'bold'),
                        padding=(10,5))
    
    def create_widgets(self):
        """
        Crée tous les éléments de l'interface graphique
        """
        # === TITRE PRINCIPAL ===
        title_label = tk.Label(
            self.root,
            text="🔤 Convertisseur Lettre -> ASCII",
            font=('Arial', 16, 'bold'),
            bg="#F0F0F0",
            fg='#333333'
        )
        title_label.pack(pady=20)

        # === FRAME PRINCIPAL (conteneur pour organiser les éléments) ===
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(pady=10, padx=20, fill='both', expand=True)

        # === LABEL + CHAMP DE SAISIE ===
        input_label = tk.Label(
            main_frame,
            text="Entrez une lettre :",
            font=('Arial', 12),
            bg='#f0f0f0'
        )
        input_label.pack(pady=(0,5))

        # Champ de saisie avec validation
        self.letter_var = tk.StringVar()
        self.letter_entry = tk.Entry(
            main_frame,
            textvariable=self.letter_var,
            font=('Arial', 14),
            width=10,
            justify='center',
            validate='key', # Validation en temps réel
            validatecommand=(self.root.register(self.validate_input), '%P')
        )
        self.letter_entry.pack(pady=5)
        self.letter_entry.focus() # Met le focus sur le champ de saisie

        # === BOUTON CONVERTIR ===
        convert_button = ttk.Button(
            main_frame,
            text="🔄 Convertir",
            style='Custom.TButton',
            command=self.convert_letter
        )
        convert_button.pack(pady=15)

        # === ZONE DE RÉSULTAT ===
        result_label = tk.Label (
            main_frame,
            text='Résultat :',
            font=('Arial', 12),
            bg='#f0f0f0'
        )
        result_label.pack(pady=(10, 5))

        # Frame pour le resultat avec bordure
        result_frame = tk.Frame(
            main_frame,
            bg='white',
            relief='ridge',
            borderwidth=2,
            height=80 # Hauteur augmentée pour 2 lignes de texte
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
            wraplength=300, # Permet le retour à la ligne
            justify='center'
        )
        self.result_label.pack()

        # === BOUTON EFFACER ===
        clear_button = ttk.Button(
            main_frame,
            text="🗑️ Effacer",
            command=self.clear_input
        )
        clear_button.pack(pady=10)
    
        # === INFO ASCII ===
        info_label = tk.Label(
            main_frame,
            text="💡 ASCII : American Standard Code for Information Interchange",
            font=('Arial', 9),
            bg='#f0f0f0',
            fg='#888888'
        )
        info_label.pack(side='bottom', pady=(20, 0))

    def validate_input(self, value):
        """
        Fonction de validation étendue :
        Accepte lettres, chiffres et symboles courants (1 carctère max)
        """
        # Si c'est vide, on accepte
        if value == "":
            return True
        
        # Si c'est plus d'un caractère, on refuse
        if len(value) > 1:
            return False
        
        # Si c'est un seul caractère, on vérifie qu'il est autorisé
        if len(value) == 1:
            char = value[0]
            #Lettres (A-Z, a-z)
            if char.isalpha():
                return True

            # Chiffres (0-9)
            if char.isdigit():
                return True
            
            # Symboles courants
            allowed_symbols = r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
            if char in allowed_symbols:
                return True
        # Dans tous les autres cas, on refuse
        return False
    
    def convert_letter(self):
        """
        Fonction principale de conversion (étendue)
        Gère lettres, chiffres et symboles
        """
        character = self.letter_var.get().strip()

        # Vérification si le champ est vide
        if not character:
            messagebox.showwarning(
                "Attention",
                "Veuillez saisir un caractère avant de convertir !"
            )
            self.letter_entry.focus()
            return
        
        # Conversion ASCII (fonction ord() de Python)
        ascii_code = ord(character)

        # Détermination de la catégorie du caractère
        if character.isalpha():
            if character.isupper():
                category = "lettre majuscule"
            else:
                category = "lettre minuscule"
        elif character.isdigit():
            category = "chiffre"
        else:
            category = "symbole"

        # Affichage du résultat avec infos détaillées
        self.result_label.config(
            text=f"'{character}' -> {ascii_code}\n(lettre {category})",
            fg='#2c5aa0',
            font=('Arial', 12, 'bold')
        )

        # Message de confirmation dans la console (utile pour le débogage)
        print(f"Conversion effectuée : {character} = {ascii_code} ({category})")

    def clear_input(self):
        """
        Remet à zéro l'application
        """
        self.letter_var.set("") # Vide le champ de saisie
        self.result_label.config(
            text="Aucune conversion effectuée",
            fg='#666666'
        )
        self.letter_entry.focus() # Remet le focus sur le champ

# === POINT D'ENTRÉE DE L'APPLICATION ===
if __name__ == "__main__":
    """Ce code ne s'exécute que si on lance directement ce fichier
    (pas si on l'importe dans un autre fichier)
    """
    # Création de la fenêtre principale
    root = tk.Tk()
    # Création de la fenêtre principale
    app = ConvertApp(root)
    # Lancement de la boucle d'événements
    root.mainloop()
    print("Application fermée. Merci d'avoir utilisé le convertisseur !")