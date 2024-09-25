import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd

# Fonction pour ouvrir le fichier CSV
def open_file():
    filepath = filedialog.askopenfilename(
        title="Ouvrir un fichier CSV",
        filetypes=(("Fichiers CSV", "*.csv"), ("Tous les fichiers", "*.*"))
    )
    if filepath:
        df = pd.read_csv(filepath)
        display_table(df)

# Fonction pour afficher le contenu CSV dans le tableau
def display_table(df):
    # Efface le tableau existant
    for row in tree.get_children():
        tree.delete(row)

    # Affiche les en-têtes de colonnes
    tree["columns"] = list(df.columns)
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Ajuster la largeur des colonnes

    # Affiche les lignes de données
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

# Créer la fenêtre principale
root = tk.Tk()
root.title("Affichage de fichier CSV")
root.geometry("600x400")

# Bouton pour charger le fichier CSV
button = tk.Button(root, text="Ajouter un fichier CSV", command=open_file)
button.pack(pady=10)

# Créer un tableau (Treeview) pour afficher le contenu CSV
tree = ttk.Treeview(root)
tree.pack(fill="both", expand=True)

# Lancer l'application
root.mainloop()
