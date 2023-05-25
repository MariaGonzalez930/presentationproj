import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x600")
        root.configure(background="black")

        style = ttk.Style()
        style.configure("TLabel", font=("Poppins", 30), background="black", foreground="white")
        style.configure("TSubtitulo.TLabel", font=("Poppins", 20), background="black", foreground="white")
        style.configure("TButton", font=("Poppins", 18))
        style.map("TButton",
                  foreground=[('active', 'white')],
                  background=[('active', 'gray')])

        self.lbl_titulo = ttk.Label(root, text="Maria Fernanda\nGonzález Mejía")
        self.lbl_titulo.pack(padx=50, pady=100, anchor="w")

        self.lbl_subtitulo=ttk.Label(root, text="19 años. \n Estudiante de Ingeniería de Software.", style="TSubtitulo.TLabel")
        self.lbl_subtitulo.pack(padx=50, pady=10, anchor="w")

        self.btn_opcion1 = ttk.Button(root, text="¿Quién soy?", command=lambda: self.abrir_ventana("¿Quién soy?", "Soy una persona apasionada por la tecnología y el desarrollo de software.", "ruta_de_la_imagen_1"))
        self.btn_opcion1.pack(padx=20,pady=5, anchor="e")

        self.btn_opcion2 = ttk.Button(root, text="¿Qué me rodea?", command=lambda: self.abrir_ventana("¿Qué me rodea?", "Mi entorno está lleno de oportunidades y personas increíbles.", "ruta_de_la_imagen_2"))
        self.btn_opcion2.pack(padx=20,pady=5, anchor="e")

        self.btn_opcion3 = ttk.Button(root, text="¿Qué me gusta?", command=lambda: self.abrir_ventana("¿Qué me gusta?", "Mi entorno está lleno de oportunidades y personas increíbles.", "ruta_de_la_imagen_2"))
        self.btn_opcion3.pack(padx=20,pady=5, anchor="e")

        self.btn_opcion4 = ttk.Button(root, text="¿Qué sé?", command=lambda: self.abrir_ventana("¿Qué sé?", "Mi entorno está lleno de oportunidades y personas increíbles.", "ruta_de_la_imagen_2"))
        self.btn_opcion4.pack(padx=20,pady=5, anchor="e")

        self.btn_opcion5 = ttk.Button(root, text="¿Qué quiero ser?", command=lambda: self.abrir_ventana("¿Qué quiero ser?", "Mi entorno está lleno de oportunidades y personas increíbles.", "ruta_de_la_imagen_2"))
        self.btn_opcion5.pack(padx=20,pady=5, anchor="e")

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        self.center_elements()

    def abrir_ventana(self, titulo, texto, ruta_imagen):
        ventana_info = tk.Toplevel(self.root)
        ventana_info.title("Ventana de Información")
        ventana_info.geometry("900x600")
        ventana_info.configure(background="black")

        label_titulo = ttk.Label(ventana_info, text=titulo, style="TLbl")
        label_titulo.pack()
        label_texto = ttk.Label(ventana_info, text=texto, style="TLbl")
        label_texto.pack()

        btn_volver = ttk.Button(ventana_info, text="Volver", command=ventana_info.destroy)
        btn_volver.pack(pady=10)

    def center_elements(self):
        total_rows = self.root.grid_size()[1]
        self.lbl_titulo.pack(pady=(self.root.winfo_height() - self.lbl_titulo.winfo_height()) // 2, anchor="w")
        for i in range(1, total_rows):
            widget = self.root.pack_slaves()[i]
            widget.pack(pady=(self.root.winfo_height() - widget.winfo_height()) // 2, anchor="e")

root = tk.Tk()
app = App(root)
root.mainloop()
