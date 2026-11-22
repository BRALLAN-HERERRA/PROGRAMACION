"""Diagnostico sencillo de Python y Tkinter para Software FJ.

Ejecutar con: py VERIFICAR_INSTALACION.py
Este archivo no modifica ni elimina datos del proyecto.
"""
import sys
import platform

print("=" * 58)
print("DIAGNOSTICO DE SOFTWARE FJ")
print("=" * 58)
print("Version de Python:", sys.version)
print("Ejecutable:", sys.executable)
print("Sistema operativo:", platform.platform())

try:
    import tkinter as tk
    from tkinter import ttk
    print("Tkinter: DISPONIBLE (version", tk.TkVersion, ")")
    try:
        ventana = tk.Tk()
        ventana.title("Prueba de Tkinter - Software FJ")
        ventana.geometry("420x150")
        ttk.Label(
            ventana,
            text="Tkinter funciona correctamente.\nPuedes cerrar esta ventana y abrir Software FJ.",
            padding=25,
            justify="center",
        ).pack(expand=True)
        print("Se abrira una ventana de prueba. Si la ves, Tkinter esta funcionando.")
        ventana.mainloop()
        print("Prueba grafica finalizada correctamente.")
    except Exception as error_ventana:
        print("ERROR AL CREAR LA VENTANA:", repr(error_ventana))
        raise
except Exception as error_tk:
    print("ERROR: Tkinter no esta disponible o no puede crear ventanas.")
    print("Detalle:", repr(error_tk))
    input("Presiona ENTER para cerrar...")
    raise SystemExit(1)
