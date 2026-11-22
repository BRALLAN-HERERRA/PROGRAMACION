
## 8. Ejecución desde el navegador - GitHub Codespaces

El repositorio de Software FJ es público, por lo que
cualquier persona puede consultar el código fuente,
revisar la documentación y descargar el proyecto
sin iniciar sesión en GitHub.

### Acceso público al proyecto

https://github.com/BRALLAN-HERERRA/PROGRAMACION/tree/main/Software_FJ

### Ejecutar el proyecto desde el navegador

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/BRALLAN-HERERRA/PROGRAMACION)

Para ejecutar Python en la nube mediante GitHub Codespaces
se requiere una cuenta de GitHub y disponibilidad de cuota.

No es necesario instalar Python ni Visual Studio Code
en el computador local para esta modalidad.

### Paso 1. Abrir el entorno de desarrollo

- Presionar el botón Open in GitHub Codespaces.
- Iniciar sesión en GitHub si se solicita.
- Seleccionar Create codespace.
- Esperar que se abra Visual Studio Code en el navegador.

### Paso 2. Abrir la terminal

Seleccionar Terminal > New Terminal.

### Paso 3. Ingresar a la carpeta del proyecto

```bash
cd /workspaces/PROGRAMACION/Software_FJ
```

### Paso 4. Verificar Python

```bash
python3 --version
```

### Paso 5. Ejecutar la simulación

```bash
python3 main.py
```

Resultado esperado:

- 28 de 28 casos verificados.
- 17 operaciones exitosas.
- 11 errores controlados.

### Paso 6. Ejecutar las pruebas unitarias

```bash
python3 -m unittest test_sistema -v
```

Resultado esperado:

```text
Ran 8 tests
OK
```

### Paso 7. Verificar el estado del repositorio

```bash
git status
```

### Nota sobre la interfaz gráfica

La simulación y las pruebas unitarias pueden ejecutarse
directamente desde el navegador.

La interfaz gráfica desarrollada con Tkinter requiere
un entorno de escritorio, por lo que se recomienda
ejecutarla en Windows o mediante un escritorio virtual
previamente configurado en GitHub Codespaces.

Si el usuario no dispone de una cuenta de GitHub,
puede descargar gratuitamente el proyecto en formato ZIP
y ejecutarlo localmente siguiendo las instrucciones
del apartado 7.
