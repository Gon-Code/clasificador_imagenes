import os
import shutil
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk

# Directorios
DIRECTORIO_ORIGEN = os.path.join(os.path.dirname(__file__), "img")
DIRECTORIO_DESTINO = os.path.join(os.path.dirname(__file__), "img_clasificadas")
DIRECTORIO_DUDOSAS = os.path.join(os.path.dirname(__file__), "img_dudosas")


EXTENSIONES_VALIDAS = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

# Funcion auxiliar para eliminar caracteres no deseados en nombres de archivos
def sanitizar(texto):
    return texto.replace(":", "-").replace("/", "-").replace("\\", "-").replace(" ", "-").strip()

class VisorImagenes:
    def __init__(self, master):
        self.master = master
        self.master.title("Visor de Imágenes")

        os.makedirs(DIRECTORIO_DESTINO, exist_ok=True)
        os.makedirs(DIRECTORIO_DUDOSAS, exist_ok=True)

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
        self.master.bind("<Key-2>", self.marcar_como_2)
        self.master.bind("<e>", self.marcar_como_evento)  # Clasificación especial

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

    def renombrar_y_mover_imagen(self, nuevo_nombre, directorio_destino):
        if self.index >= self.total:
            return

        nombre_original = self.imagenes[self.index]
        origen = os.path.join(DIRECTORIO_ORIGEN, nombre_original)
        destino = os.path.join(directorio_destino, nuevo_nombre)

        shutil.move(origen, destino)

    def marcar_como_0(self, event):
        self.mover_con_sufijo('0', DIRECTORIO_DESTINO)
        self.siguiente_imagen()

    def marcar_como_1(self, event):
        self.mover_con_sufijo('1', DIRECTORIO_DESTINO)
        self.siguiente_imagen()

    def marcar_como_2(self, event):
        self.mover_con_sufijo('2', DIRECTORIO_DUDOSAS)
        self.siguiente_imagen()

    def mover_con_sufijo(self, sufijo, directorio_destino):
        nombre_original = self.imagenes[self.index]
        nombre_base, extension = os.path.splitext(nombre_original)
        nuevo_nombre = f"{sufijo}-{nombre_base}{extension}"
        self.renombrar_y_mover_imagen(nuevo_nombre, directorio_destino)

    def marcar_como_evento(self, event):
        nombre_original = self.imagenes[self.index]
        id_afiche, _ = os.path.splitext(nombre_original)

        # Crear ventana para ingreso de datos
        datos = self.pedir_datos_evento(id_afiche)
        if not datos:
            return
        
        (
            fecha_evento,
            fecha_escrita,
            hora_evento,
            hora_escrita,
            lugar
        ) = datos

        fecha_evento = sanitizar(fecha_evento)
        fecha_escrita = sanitizar(fecha_escrita)
        hora_evento = sanitizar(hora_evento)
        hora_escrita = sanitizar(hora_escrita)
        lugar = sanitizar(lugar)
        
        nombre_final = f"1_{id_afiche}_{fecha_evento}_{fecha_escrita}_{hora_evento}_{hora_escrita}_{lugar}.jpg"
        self.renombrar_y_mover_imagen(nombre_final, DIRECTORIO_DESTINO)
        self.siguiente_imagen()

    def pedir_datos_evento(self, id_afiche):
        # Ventana de diálogo personalizada
        top = tk.Toplevel(self.master)
        top.title(f"Formulario para Evento - {id_afiche}")
        top.grab_set()  # Bloquea la ventana principal

        campos = {
            "Fecha evento (dd-mm-aaaa)": "",
            "Fecha escrita": "",
            "Hora evento (HH:MM 24hrs)": "",
            "Hora escrita": "",
            "Lugar": ""
        }

        entradas = {}
        for i, (label_text, _) in enumerate(campos.items()):
            tk.Label(top, text=label_text).grid(row=i, column=0, sticky="w", padx=5, pady=5)
            entrada = tk.Entry(top, width=30)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            entradas[label_text] = entrada

        resultado = []

        def confirmar():
            for label in campos:
                texto = entradas[label].get().strip().replace(" ", "_")
                if not texto:
                    return
                resultado.append(texto)
            top.destroy()

        tk.Button(top, text="Aceptar", command=confirmar).grid(columnspan=2, pady=10)
        top.wait_window()

        return resultado if len(resultado) == 5 else None

    def siguiente_imagen(self):
        self.index += 1
        self.cargar_imagen()

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = VisorImagenes(root)
    root.mainloop()
