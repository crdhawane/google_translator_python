import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from tkinter import font

# Initialize the Translator
translator = Translator()

# Function to perform translation
def translate_text():
    input_text = text_entry.get("1.0", tk.END).strip()
    src_lang = source_lang.get()
    dest_lang = target_lang.get()
    if input_text:
        result = translator.translate(input_text, src=src_lang, dest=dest_lang)
        result_label.config(text=result.text)

# Create the main window
root = tk.Tk()
root.title("Language Translator")

# Create and place the input text box
text_font = font.Font(size=14) 
text_entry = tk.Text(root, height=5, width=40, font=text_font)
text_entry.pack(pady=10)

# Create and place the source language dropdown
source_lang = ttk.Combobox(root, values=list(LANGUAGES.values()))
source_lang.set("Select source language")
source_lang.pack(pady=5)

# Create and place the target language dropdown
target_lang = ttk.Combobox(root, values=list(LANGUAGES.values()))
target_lang.set("Select target language")
target_lang.pack(pady=5)

# Create and place the translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Create and place the result label with larger and bold font
result_font = font.Font(size=14, weight="bold")

# Create and place the result label
result_label = tk.Label(root, text="", wraplength=400,font=result_font)
result_label.pack(pady=10)

# Run the application
root.mainloop()
