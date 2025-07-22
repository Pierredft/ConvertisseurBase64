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
        