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

    