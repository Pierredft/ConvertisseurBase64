import tkinter as tk
from tkinter import ttk, messagebox

class ConvertApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Convertisseur Lettre -> ASCII")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.setup_styles()

    def setup_style(self):
        self.root.configure(bg='#f0f0f0')
        style = ttk.Style()
        style.configure('Custom.TButton',
                        font=('Arial',12, 'bolde'),
                        padding=(10,5))
    
    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="🔤 Convertisseur Lettre -> ASCII",
            font=('Arial', 16, 'bold'),
            bg="#fb0000",
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

        self.lettre_var = tk.StringVar()
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
            style='Custome.TButton',
            command=self.convert_letter
        )
        convert_button.pack(pady=15)

        result_label = tk.Label (
            main_frame,
            text='Resultat :',
            font=('Arial', 12),
            bg='#f0f0f0'
        )
        result_label.pack(pady=(10, 5))

        result_frame = tk.Frame(
            main_frame,
            bg='white',
            relief='ridge',
            borderwidth=2
        )
        result_frame.pack(pady=5, padx=20, fill='x')

        self.result_label = tk.Label(
            result_frame,
            text='Aucune conversion effectuée',
            font=('Arial', 14, 'bold'),
            bg='white',
            fg='#666666',
            pady=15
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
        