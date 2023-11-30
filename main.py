
import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)  # Met à jour toutes les 1000 millisecondes (1 seconde)

root = tk.Tk()
root.title("Horloge Numérique")

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

update_time()  # Lance la fonction de mise à jour initiale

root.mainloop()

