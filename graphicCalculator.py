import tkinter as tk

# Létrehozzuk a fő ablakot
root = tk.Tk()
root.title("Számológép")

# Létrehozzuk a számításokat végző függvényt
def calculate():
  # Beolvassuk a szövegmezőkben lévő értékeket
  num1 = int(num1_entry.get())
  num2 = int(num2_entry.get())
  # Számítjuk ki az összeget és megjelenítjük a szövegmezőben
  result = num1 + num2
  result_label.config(text=str(result))

# Létrehozzuk a szövegmezőket a számok beviteléhez
num1_entry = tk.Entry(root)
num2_entry = tk.Entry(root)

# Létrehozzuk a gombot a számítás indításához
calculate_button = tk.Button(root, text="Számítás", command=calculate)

# Létrehozzuk a címkét az eredmény megjelenítéséhez
result_label = tk.Label(root, text="")

# Megjelenítjük a szövegmezőket, gombot és címkét az ablakban
num1_entry.pack()
num2_entry.pack()
calculate_button.pack()
result_label.pack()

# Futtatjuk az ablakot
root.mainloop()
