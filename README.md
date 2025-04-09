# Sistema de Gestión de Tareas

## 📋 Descripción

Este proyecto es una aplicación de línea de comandos (CLI) desarrollada en Python que permite a los usuariosgestionar sus tareas diarias. 
Las funcionalidades incluyen crear, editar, eliminar, listar y filtrar tareas por categoría o estado. Además, 
el sistema guarda las tareas automáticamente utilizando persistencia en archivos JSON y asegura que solo exista una instancia del gestor de 
tareas mediante el patrón de diseño Singleton.

## ✅ Requisitos previos

- Python 3.7 o superior
- Sistema operativo: Windows, Linux o macOS

##  Instrucciones de instalación

1. **Clonar el repositorio:**

```bash
git clone https://github.com/tu-usuario/sistema-gestion-tareas.git
cd sistema-gestion-tareas

Opcional) Crear un entorno virtual:
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows

Instalar dependencias (si se usan):

pip install -r requirements.txt
Nota: Este proyecto no requiere paquetes externos, solo la biblioteca estándar de Python.


Ejecutar el programa:

python main.py

Guía de uso
Al ejecutar el sistema, se mostrará un menú interactivo con las siguientes opciones:
1. Agregar tarea
2. Editar tarea
3. Eliminar tarea
4. Listar tareas
5. Filtrar tareas
6. Salir

Ejemplo de uso:
Agregar una tarea:

Ingrese el título, descripción y categoría.

Filtrar tareas:

Puede filtrar por categoría ("Trabajo", "Personal", etc.) o estado ("Pendiente" o "Completada").

Salir:

Guarda automáticamente las tareas antes de salir del sistema.

Autores
[ismael eduardo sanatana avila]

Plan de evolución (futuro)
✅ Implementar una API REST para integración con aplicaciones móviles.

✅ Añadir recordatorios automáticos usando schedule o time.

✅ Migrar la interfaz a una aplicación gráfica con Tkinter, Kivy o PyQt.
