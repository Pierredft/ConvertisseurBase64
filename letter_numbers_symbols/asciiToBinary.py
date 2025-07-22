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

    def __init__(self, root):
        """
        Constructeur de l'application ASCII -> Binaire
        """
        self.root = root
        self.root.title("Convertisseur ASCII -> Binaire")
        self.root.geometry("800x600")
        self.root.resizable(False, False) # Ne pas redimensionner la fenêtre
        self.root.configure(bg="#F0F0F0")  # Couleur de fond

        # Configuration du style
        # self.setup_styles()
        # Création de l'interface
        self.create_widgets()

    def create_widgets(self):
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

        # === BOUTON CONVERTIR ===
        convert_button = ttk.Button(
            main_frame,
            text="🔄 Convertir en Binaire",
            style='Convert.TButton',
            command=self.convert_to_binary
        )
        convert_button.pack(pady=20)

        # === ZONE DE RÉSULTAT ===
        result_section = tk.Frame(main_frame, bg='#f5f5f5')
        result_section.pack(pady=10, fill='x')

        result_title = tk.Label(
            result_section,
            text="Résultat de la conversion :",
            font=('Arial', 12, 'bold'),
            bg='#f5f5f5',
            fg='#34495e',
        )
        result_title.pack(pady=(0,8))

        # Frame pour le résultat avec bordure
        result_frame = tk.Frame(
            result_section,
            bg='white',
            relief='solid',
            borderwidth=1,
        )
        result_frame.pack(pady=5, padx=10, fill='x', ipady=10)

        self.result_label = tk.Label(
            result_frame,
            text='Aucune conversion effectuée',
            font=('Arial', 14, 'bold'),
            bg='white',
            fg='#95a5a6',
            wraplength=350,
            justify='center'
        )
        self.result_label.pack(pady=15)

        # === SECTION DÉTAILS ===
        details_frame = tk.Frame(
            result_section,
            bg='#ecf0f1',
            relief='groove',
            borderwidth=1,
        )
        details_frame.pack(pady=(10, 0), padx=10, fill='x', ipady=8)

        self.details_label = tk.Label(
            details_frame,
            text="Les détails de conversion s'afficheront ici",
            font=('Arial', 10),
            bg='#ecf0f1',
            fg='#7f8c8d',
            wraplength=350,
            justify='left'
        )
        self.details_label.pack(pady=5)

        # === BOUTONS D'ACTION ===
        buttons_frame = tk.Frame(main_frame, bg='#f5f5f5')
        buttons_frame.pack(pady=15)

        clear_button = ttk.Button(
            buttons_frame,
            text="🗑️ Effacer",
            style='Clear.TButton',
            command=self.clear_all
        )
        clear_button.pack(side='left', padx=10)

        # Bouton bonus : exemples
        examples_button = ttk.Button(
            buttons_frame,
            text="📚 Exemples",
            style='Clear.TButton',
            command=self.show_examples
        )
        examples_button.pack(side='right', padx=10)

        # === INFO ASCII/BINAIRE ===
        footer_info = tk.Label(
            main_frame,
            text="💡 Le binaire représente les nombres en base 2 (seulement 0 et 1)",
            font=('Arial', 9),
            bg='#f5f5f5',
            fg='#95a5a6'
        )
        footer_info.pack(side='bottom', pady=(15, 0))

    def validate_ascii_input(self, value):
        """
        Fonction de validation pour les codes ASCII
        Accepte seulement les nombres de 0 à 127
        """

        #Si c'est vide, on accepte
        if value == "":
            return True
        
        # Vérifier que ce sont uniquement des chiffres
        if not value.isdigit():
            return False
        
        # Vérifier que la valeur est dasn la plage ASCII valide (0-127)
        try:
            ascii_value = int(value)
            if 0 <= ascii_value <= 127:
                return True
            else:
                return False
        except ValueError:
            return False
        
    def convert_to_binary(self):
        """
        Fonction principale de conversion ASCII -> Binaire
        """
        ascii_str = self.ascii_var.get().strip()

        # Vérification que quelque chose a été saisi
        if not ascii_str:
            messagebox.showwarning(
                "Attention",
                "Veuillez saisir un code ASCII avant de convertir !"
            )
            self.ascii_entry.focus()
            return
        
        #Conversion en entier
        ascii_code = int(ascii_str)

        # Conversion en binaire (sans le préfixe '0b')
        binary_result = bin(ascii_code)[2:] # [2:] enlève le '0b' du début

        # Formatage sur 8 bits (standard ASCII)
        binary_8bits = binary_result.zfill(8) # Complète avec des 0 à gauche

        # Déterminer le caractère correspondant (si imprimable)
        if 32 <= ascii_code <= 126:  # Plage des caractères imprimables
            character = chr(ascii_code)
            char_info = f"Caractère : '{character}'"
        else:
            char_info = "Caractère : [non imprimable]"

        # Affichage du résultat principal
        self.result_label.config(
            text=f"ASCII {ascii_code} → {binary_8bits}\n{char_info}",
            fg='#27ae60' # Vert pour le succès
        )

        #Affichage des détails pédagogiques
        details_text = (
            f"• Binaire brut : {binary_result}\n"
            f"• Binaire 8-bits : {binary_8bits}\n"
            f"• Méthode : Division successive par 2\n"
            f"• Vérification : {self.binary_to_decimal_explanation(binary_8bits)}"
        )

        self.details_label.config(
            text=details_text,
            fg='#34495e'
        )

        # Message de confirmation dans la console
        print(f"Conversion ASCII->Binaire : {ascii_code} -> {binary_8bits}")

    def binary_to_decimal_explanation(self, binary_str) :
        """
        Explique comment le binaire est converti en décimal
        """
        decimal_value = 0
        explanation_parts = []

        # Parcourir chaque bit de droite à gauche
        for i, bit in enumerate(reversed(binary_str)):
            if bit == '1':
                power_of2 = 2 ** i
                decimal_value += power_of2
                explanation_parts.append(f"{power_of2}")

        if explanation_parts:
            return f"{' + '.join(explanation_parts)} = {decimal_value}"
        else:
            return "0"
        
    def clear_all(self):
        """ 
        Remet à zéro l'application
        """

        self.ascii_var.set("")
        self.result_label.config(
            text="Aucune conversion effectuée",
            fg='#95a5a6'
        )
        self.details_label.config(
            text="Les détails de conversion s'afficheront ici",
            fg='#7f8c8d'
        )
        self.ascii_entry.focus()

    def show_examples(self):
        """
        Affiche une fenêtre avec des exemples de conversion
        """

        examples_window = tk.Toplevel(self.root)
        examples_window.title("Exemples de conversions ASCII → Binaire")
        examples_window.geometry("1000x800")
        examples_window.resizable(False, False)
        examples_window.configure(bg='#f8f9fa')

        # Titre
        title = tk.Label(
            examples_window,
            text="📚 Exemples de conversions",
            font=('Arial', 16, 'bold'),
            bg='#f8f9fa',
            fg='#2c3e50'
        )
        title.pack(pady=15)

        # Exemples
        examples_text = """
🔤 LETTRES :
• ASCII 65 → 01000001 → 'A'
• ASCII 97 → 01100001 → 'a'

🔢 CHIFFRES :
• ASCII 48 → 00110000 → '0'
• ASCII 57 → 00111001 → '9'

🔣 SYMBOLES :
• ASCII 33 → 00100001 → '!'
• ASCII 64 → 01000000 → '@'
• ASCII 32 → 00100000 → [ESPACE]

⚡ CARACTÈRES SPÉCIAUX :
• ASCII 10 → 00001010 → [SAUT DE LIGNE]
• ASCII 13 → 00001101 → [RETOUR CHARIOT]
• ASCII 127 → 01111111 → [DELETE]

💡 ASTUCE :
Le binaire se lit de droite à gauche avec les puissances de 2 :
128 64 32 16 8 4 2 1
        """

        examples_label = tk.Label(
            examples_window,
            text=examples_text,
            font=('Courier', 11),
            bg='#f8f9fa',
            fg='#2c3e50',
            justify='left'
        )
        examples_label.pack(pady=10, padx=20)

        # Bouton fermer
        close_button = ttk.Button(
            examples_window,
            text="Fermer",
            command=examples_window.destroy
        )
        close_button.pack(pady=15)

# === POINT D'ENTRÉE DE L'APPLICATION ===
if __name__ == "__main__":
    """
    Point d'entrée du programme
    """
    print("🚀 Lancement du convertisseur ASCII -> Binaire")

    # Création de la fenêtre principale
    root = tk.Tk()

    # Création de notre applciation
    app = ASCIIToBinaryApp(root)

    # Lancement de la boucle d'événements
    root.mainloop()

    print("✅ Application fermée. Merci d'avoir utilisé le convertisseur !")