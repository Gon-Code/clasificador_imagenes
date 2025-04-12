import os
import shutil
import tkinter as tk
from PIL import Image, ImageTk

# Directorios
DIRECTORIO_ORIGEN = os.path.join(os.path.dirname(__file__), "img")
DIRECTORIO_DESTINO = os.path.join(os.path.dirname(__file__), "img_clasificadas")

EXTENSIONES_VALIDAS = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

class VisorImagenes:
    def __init__(self, master):
        self.master = master
        self.master.title("Visor de Imágenes")

        if not os.path.exists(DIRECTORIO_DESTINO):
            os.makedirs(DIRECTORIO_DESTINO)

        self.imagenes = [f for f in os.listdir(DIRECTORIO_ORIGEN) if f.lower().endswith(EXTENSIONES_VALIDAS)]
        self.imagenes.sort()
        self.total = len(self.imagenes)
        self.index = 0

        self.label_imagen = tk.Label(self.master)
        self.label_imagen.pack()

        self.label_contador = tk.Label(self.master, font=("Arial", 14))
        self.label_contador.pack(pady=10)

        self.cargar_imagen()

        self.master.bind("<Left>", self.marcar_como_0)
        self.master.bind("<Right>", self.marcar_como_1)

    def cargar_imagen(self):
        if self.index >= self.total:
            self.label_imagen.config(image='', text="Fin de las imágenes.")
            self.label_contador.config(text="✅ Todas las imágenes han sido procesadas.")
            return

        path = os.path.join(DIRECTORIO_ORIGEN, self.imagenes[self.index])
        imagen = Image.open(path)
        imagen.thumbnail((800, 600))
        self.tk_image = ImageTk.PhotoImage(imagen)
        self.label_imagen.config(image=self.tk_image)

        self.label_contador.config(text=f"Imagen {self.index + 1} de {self.total}")

    def renombrar_y_mover_imagen(self, sufijo):
        if self.index >= self.total:
            return

        nombre_original = self.imagenes[self.index]
        nombre_base, extension = os.path.splitext(nombre_original)
        nuevo_nombre = f"{nombre_base}-{sufijo}{extension}"

        origen = os.path.join(DIRECTORIO_ORIGEN, nombre_original)
        destino = os.path.join(DIRECTORIO_DESTINO, nuevo_nombre)

        os.rename(origen, destino)

    def marcar_como_0(self, event):
        self.renombrar_y_mover_imagen('0')
        self.siguiente_imagen()

    def marcar_como_1(self, event):
        self.renombrar_y_mover_imagen('1')
        self.siguiente_imagen()

    def siguiente_imagen(self):
        self.index += 1
        self.cargar_imagen()

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = VisorImagenes(root)
    root.mainloop()
