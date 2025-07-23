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

        # === ÉTAPE 3 : REGROUPEMENT EN 6 BITS ===
        step3_frame = tk.Frame(notebook, bg='white')
        notebook.add(step3_frame, text=" ✂️ 3. Découpe en 6-bits")

        step3_title = tk.Label(
            step3_frame,
            text="✂️ ÉTAPE 3 : Regroupement du binaire en blocs de 6 bits",
            font=('Arial', 12, 'bold'),
            bg='white',
            fg='#27ae60'
        )
        step3_title.pack(pady=10)

        self.step3_result = scrolledtext.ScrolledText(
            step3_frame,
            font=('Courier', 10),
            height=12,
            bg='#dff9fb',
            fg='#2c3e50',
            state=tk.DISABLED
        )
        self.step3_result.pack(fill='both', expand=True, padx=10, pady=5)

        # === ÉTAPE 4 : 6-BITS -> BASE64 ===
        step4_frame = tk.Frame(notebook, bg='white')
        notebook.add(step4_frame, text="🎯 ÉTAPE 4: 6-bits -> Base64")

        step4_title = tk.Label(
            step4_frame,
            text="🎯 ÉTAPE 4 : Conversion des 6-bits en Caractères Base64",
            font=('Arial', 12, 'bold'),
            bg='white',
            fg='#8e44ad'
        )
        step4_title.pack(pady=10)

        self.step4_result.pack(fill='both' , expand=True, padx=10, pady=5)

        # == ÉTAPE 5 : RÉSULTAT FINAL ===  
        step5_frame = tk.Frame(notebook, bg='white')
        notebook.add(step5_frame, text="🏁 Résultat Final")

        step5_title = tk.label(
            step5_frame,
            text="🏁 RÉSULTAT FINAL : Texte Converti en Base64",
            font=('Arial', 12, 'bold'),
            bg='white',
            fg='#2980b9'
        )
        step5_title.pack(pady=20)

        # Cadre pour le resultat final
        result_frame = tk.Frame(
            step5_frame,
            bg='#f8f9fa',
            borderwidth=2
        )
        result_frame.pack(pady=20, padx=50, fill='x')

        self.final_result = tk.Label(
            result_frame,
            text="Le resultat Base64 apparaîtra ici",
            font=('Courier', 14, 'bold'),
            bg='#f8f9fa',
            fg='#2c3e50',
            pady=20,
            wraplength=600
        )
        self.final_result.pack()

        # Bouton copier
        copy_button = ttk.Button(
            step5_frame,
            text="📋 Copier le résultat",
            style='Action.TButton',
            command=self.copy_result
        )
        copy_button.pack(pady=10)

        # Vérification avec Python
        verify_frame = tk.LabelFrame(
            step5_frame,
            text="🔍 Vérification avec Pbase64.b64encode()",
            font=('Arial', 10, 'bold'),
            bg='white',
            fg="#34495e",
            padx=10,
            pady=10
        )
        verify_frame.pack(fill='x', padx=50, pady=20)

        self.verify_result = tk.Label(
            verify_frame,
            text='La vérification apparaîtra ici',
            font=('Courier', 11),
            bg='white',
            fg='#2c3e50',
        )
        self.verify_result.pack()

        # === INFO PIED DE PAGE ===
        footer_info = tk.Label(
            main_frame,
            text="💡 Astuce : Utilisez des espaces pour séparer les mots.",
            font=('Arial', 10),
            bg='#f8f9fa',
            fg='#7f8c8d'
        )
        footer_info.pack(pady=10)

    def convert_step_by_step(self):
        """
        Fonction principale qui effectue la conversion étape par étape
        """

        input_text = self.text_input.get().strip()

        if not input_text:
            messagebox.showwarning("Attention", "Veuillez saisir du texte !")
            return
        
        # Effacer les résultats précédents
        self.clear_results()

        print(f"🔄 Début conversion : '{input_text}")

        try:
            # === Étape 1 : TEXTE -> ASCII ===
            ascii_codes, step1_text = self.step1_text_to_ascii(input_text)

            # === Étape 2 : ASCII -> BINAIRE ===
            binary_string, step2_text = self.step2_ascii_to_binary(ascii_codes, input_text)

            # === Étape 3 : REGROUPEMENT EN 6 BITS ===
            six_bits_groups, step3_text = self.step3_group_6bits(binary_string)

            # === Étape 4 : 6-BITS -> BASE64 ===
            base64_chars, step4_text = self.step4_6bits_to_base64(six_bits_groups)

            # === Étape 5 : RÉSULTAT FINAL ===
            final_base64 = self.step5_final_result(base64_chars, input_text)

            # Affichage des résultats dasn chaque onglet
            self.display_step_result(self.step1_result, step1_text)
            self.display_step_result(self.step2_result, step2_text)
            self.display_step_result(self.step3_result, step3_text)
            self.display_step_result(self.step4_result, step4_text)

            print(f"✅ Conversion terminée : '{final_base64}'")
        
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la conversion : {str(e)}")

    def step1_texto_ascii(self, text):
        """
        Convertit chaque caractère en code ASCII
        """

        ascii_codes = []
        result_lines = [
            "📝 CONVERTION TEXTE -> ASCII",
            "="*50,
            f"Text d'entrée : '{text}'",
            f"CLongueur : {len(text)} caractères",
            "",
            "Conversion caractère par caractère :"
        ]

        for i, char in enumerate(text):
            ascii_code = ord(char)
            ascii_codes.append(ascii_code)
            
            # Formatage de l'affichage du caractère
            if char == ' ':
                display_char = '[ESPACE]'
            elif char.isprintable():
                display_char = f" '{char}'"
            else:
                display_char = f'[CTRL-{ascii_code}]'
            
            result_lines.append(f" POS {i+1:2d}: {display_char:10} -> ASCII {ascii_code:3d}")

            result_lines.extend([
                "",
                "📊 RÉSUMÉ :",
                f"Codes ASCII : {ascii_codes}"
            ])
            return ascii_codes, "\n".join(result_lines)
            
    def step2_ascii_to_binary(self, ascii_codes, original_text):
        """
        ÉTAPE 2 :Convertit les codes ASCII en binaire (8 bits chacun)
        """
        
        binary_parts = []
        result_lines = [
            "🔢 CONVERSION ASCII -> BINAIRE",
            "="*50,
            "Chaque code ASCII est converti en binaire sur 8 bits :",
            ""
        ]

        for i, ascii_code in enumerate(ascii_codes):
            binary = bin(ascii_code)[2:].zfill(8) # Convertion et padding sur 8 bits
            binary_parts.append(binary)

            char = original_text[i]
            display_char = '[ESPACE]' if char == ' ' else f"'{char}"

            result_lines.append(f" {display_char:10} -> ASCII {ascii_code:3d} -> {binary}")

        # Concaténation de tous les bits
        binary_string = ''.join(binary_parts)

        result_lines.extend([
            "",
            "⛓️‍💥 CONCATÉNATION DE TOUS LES BITS :",
            f"Longueur totale : {len(binary_string)} bits",
            "",
            "Binaire complet :"
        ])

        # Affichage du binaire par groupes de 8 pour la lisibilité
        for i in range(0, len(binary_string), 40):
            chunk = binary_string[i:i+40]
            # Ajouter des espaces tous les 8 bits
            formatted_chunk = ' '.join(chunk[j:j+8] for j in range(0, len(chunk), 8))
            result_lines.append(f" {formatted_chunk}")

        return binary_string,  "\n".join(result_lines)
    
    def step3_group_6bits(self, binary_string):
        """
        ÉTAPE 3 : Regroupe le binaire en blocs de 6 bits
        """

        result_lines = [
            "✂️ REGROUPEMENT EN 6 BITS",
            "="*50,
            "Base64 utilise des groupes de 6 bits (2^6 = 64 possibilités)",
            "",
            f"Binaire d'entrée ({len(binary_string)} bits) :",
        ]

        # Affichage du binaire d'origine
        for i in range(0, len(binary_string), 48):
            chunk = binary_string[i:i+48]
            formatted_chunk = ' '.join(chunk[j:j+8] for j in range(0, len(chunk), 8))
            result_lines.append(f" {formatted_chunk}")

        # Padding si nécessaire (doit être multiple de 6)
        padded_binary = binary_string
        padding_needed = (6 - len(binary_string) %6) %6
        if padding_needed > 0:
            padded_binary += '0' * padding_needed
            result_lines.extend([
                "",
                f"⚠️ PADDING NÉCESSAIRE : {padding_needed} zéros ajoutés",
                f"Binaire avec padding ({len(padded_binary)} bits) :",
            ])
            for i in range(0, len(padded_binary), 48):
                chunk = padded_binary[i:i+48]
                formatted_chunk = ' '.join(chunk[j:j+8] for j in range(0, len(chunk), 8))
                result_lines.append(f" {formatted_chunk}")

        # Découpage en groupes de 6 bits
        six_bits_groups = []
        result_lines.extend([
            "",
            "✂️ DÉCOUPAGE EN GROUPES DE 6 BITS :"
        ])

        for i in range(0, len(padded_binary), 6):
            group = padded_binary[i:i+6]
            six_bits_groups.append(group)
            decimal_value = int(group, 2)
            result_lines.append(f" Groupe {len(six_bits_groups)} : {group} -> décimal {decimal_value:2d}")

        result_lines.extend([
            "",
            f"📊 RÉSUMÉ : {len(six_bits_groups)} groupes de 6 bits créés"
        ])
        return six_bits_groups, "\n".join(result_lines)
    
    def step4_6bits_to_base64(self, six_bits_groups):
        """
        ÉTAPE 4 : Convertit les groupes de 6 bits en caractères Base64
        """

        result_lines = [
            "🎯 CONVERSION 6-BITS -> CARACTÈRES BASE64",
            "="*50,
            "Table Base64 : A-Z(0-25), a-z(26-51), 0-9(52-61), + (62), / (63)",
            "",
        ]

        base64_chars = []

        for i, group in enumerate(six_bits_groups):
            decimal_value = int(group, 2)
            base64_char = self.base64_chars[decimal_value]
            base64_chars.append(base64_char)

            result_lines.append(
                f" Groupe {i+1:2d}: {group} -> {decimal_value:2d} -> '{base64_char}'"
            )

        result_lines.extend([
            "",
            "🔤 CARACTÈRES BASE 64 OBTENUS :",
            f" {''.join(base64_chars)}",
            "",
            f"📊 {len(base64_chars)} caractères Base64 générés"
        ])

        return base64_chars, "\n".join(result_lines)
    
    def step5_final_result(self,base64_chars, original_text):
        """
        ÉTAPE 5 : Finalise le resultat avec le padding base64 (=)
        """

        # Calcul du padding nécessaire
        padding_needed = (4 - len(base64_chars) % 4) % 4

        # Résultat final
        final_base64 = ''.join(base64_chars) + '=' * padding_needed

        # Affichage du résultat final
        self.final_result.config(
            text=f"'{original_text}' -> {final_base64}",
            fg='#8e44ad'
        )

        # Vérification avec Python
        python_result = base64.b64encode(original_text.encode('utf-8')).decode('ascii')

        if final_base64 == python_result:
            verify_text = f"✅ CORRECT ! Python donne : {python_result}"
            color = '#27ae60'
        else:
            verification_text = f"❌ ERREUR ! Python donne : {python_result}"
            color = '#e74c3c'

        self.verify_result.config(text=verification_text, fg=color)
        self.current_result = final_base64
        return final_base64
    
    