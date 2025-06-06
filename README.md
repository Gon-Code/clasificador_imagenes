# 🖼️ Clasificador de Imágenes con Teclado (Python + Tkinter)

Este es un pequeño visor de imágenes interactivo en Python que permite **clasificar imágenes** usando las teclas **izquierda** y **derecha**. Al presionar una de las dos teclas, la imagen actual es:

1. ✅ Renombrada agregando el prefijo `0-` o `1-` al nombre del archivo.
2. 📁 Movida a la carpeta `img_clasificadas`.

---

## 🛠️ Requisitos

- Python 3.x
- Librería `Pillow`

### ▶️ Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate      # En Linux/macOS
venv\Scripts\activate         # En Windows
pip install -r requirements.txt
```

# 📂 Estructura esperada de carpetas

```plaintext
proyecto/
│
├── clasificador.py         # archivo principal del script
├── img/                    # carpeta con las imágenes a clasificar
├── img_clasificadas/       # (se crea automáticamente)
└── README.md
```


# ▶️ Cómo usar

Coloca tus imágenes dentro de la carpeta img/.

Ejecuta el script:

```bash
python app.py
```

Usa las teclas de flecha:

⬅️ Flecha izquierda: renombra la imagen con el prefijo 0- y mueve la imagen a la carpeta img_clasificadas.

➡️ Flecha derecha: renombra la imagen con el prefijo 1- y mueve la imagen a la carpeta img_clasificadas.

2️⃣ Numero 2: renombra la imagen con el prefijo 2- y mueve la imagen a la carpeta img_dudosas.

# 📊 Progreso

El visor muestra un contador como:

**Imagen 3 de 20**

Al finalizar, mostrará un mensaje indicando que todas las imágenes han sido clasificadas.


# 🧑‍💻 Autor

Proyecto rápido hecho con Python y mucho cariño 🐍❤️.

**Gon-Code**


