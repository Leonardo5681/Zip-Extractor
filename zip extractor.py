import tkinter as tk
from tkinter import filedialog
import zipfile

def seleziona_file():
    file_zip = filedialog.askopenfilename(filetypes=[("File ZIP", "*.zip")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_zip)

def seleziona_cartella():
    cartella_destinazione = filedialog.askdirectory()
    cartella_entry.delete(0, tk.END)
    cartella_entry.insert(0, cartella_destinazione)

def estrai_zip():
    file_zip = file_entry.get()
    cartella_destinazione = cartella_entry.get()
    with zipfile.ZipFile(file_zip, 'r') as zip_ref:
        zip_ref.extractall(cartella_destinazione)
    tk.messagebox.showinfo("Estrazione completata", "I file sono stati estratti correttamente.")

# Creazione della finestra
window = tk.Tk()
window.title("Estrazione di file ZIP")
window.geometry("400x200")

# Etichetta e campo di testo per il file ZIP
file_label = tk.Label(window, text="Seleziona un file ZIP:")
file_label.pack()
file_entry = tk.Entry(window, width=40)
file_entry.pack()
file_button = tk.Button(window, text="Sfoglia", command=seleziona_file)
file_button.pack()

# Etichetta e campo di testo per la cartella di destinazione
cartella_label = tk.Label(window, text="Seleziona una cartella di destinazione:")
cartella_label.pack()
cartella_entry = tk.Entry(window, width=40)
cartella_entry.pack()
cartella_button = tk.Button(window, text="Sfoglia", command=seleziona_cartella)
cartella_button.pack()

# Pulsante per l'estrazione
estrai_button = tk.Button(window, text="Estrai", command=estrai_zip)
estrai_button.pack()

# Avvio della finestra
window.mainloop()