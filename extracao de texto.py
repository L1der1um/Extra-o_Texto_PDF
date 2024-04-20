import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image

class OCRMAXApp:
    def __init__(self, master):
        self.master = master
        self.master.title("OCR MAX")
        self.master.geometry("400x200")
        self.master.resizable(False, False)
        
        self.label = tk.Label(self.master, text="Selecione um arquivo PDF:")
        self.label.pack(pady=10)
        
        self.btn_browse = tk.Button(self.master, text="Procurar", command=self.open_file)
        self.btn_browse.pack(pady=5)
        
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            try:
                pdf = PdfReader(file_path)
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
                self.save_text(text)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao abrir o arquivo PDF: {e}")
    
    def save_text(self, text):
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivo de texto", "*.txt")])
        if save_path:
            try:
                with open(save_path, "w") as f:
                    f.write(text)
                messagebox.showinfo("Concluído", "Texto extraído com sucesso e salvo como arquivo TXT.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

def main():
    root = tk.Tk()
    app = OCRMAXApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
