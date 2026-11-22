
# Software FJ

## Sistema Integral de Gestión de Clientes, Servicios y Reservas

### 1. Información académica

- Universidad: Universidad Nacional Abierta y a Distancia - UNAD.
- Escuela: Escuela de Ciencias Básicas, Tecnología e Ingeniería - ECBTI.
- Programa: Ingeniería de Sistemas.
- Curso: Programación.
- Código: 213023.
- Grupo: 213023_651.
- Actividad: Fase 4 - Prácticas simuladas.
- Estudiante: Brallan Smith Herrera Parrado.
- Tutora: Alejandra Giraldo Gaviria.
- Año: 2026.

### 2. Descripción del proyecto

Software FJ es una aplicación de escritorio desarrollada en Python
y Tkinter para gestionar clientes, servicios y reservas.

El sistema permite administrar reservas de salas, alquiler de
equipos y asesorías especializadas, aplicando los principios
de programación orientada a objetos y manejo avanzado
de excepciones.

La aplicación no utiliza ningún motor de bases de datos.
La información se administra mediante objetos y listas
internas durante la ejecución del programa.

### 3. Funcionalidades

- Registro y consulta de clientes.
- Gestión de servicios.
- Gestión de reservas.
- Confirmación y cancelación de reservas.
- Cálculo de costos, impuestos y descuentos.
- Validación de datos ingresados.
- Control de disponibilidad de servicios.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores.
- Interfaz gráfica con formularios integrados.
- Simulación de operaciones.
- Pruebas unitarias automatizadas.

### 4. Conceptos de programación aplicados

- Abstracción.
- Herencia.
- Polimorfismo.
- Encapsulación.
- Clases abstractas.
- Métodos sobrescritos.
- Sobrecarga simulada mediante parámetros opcionales.
- Excepciones personalizadas.
- Bloques try/except.
- Bloques try/except/else.
- Bloques try/except/finally.
- Encadenamiento de excepciones.
- Manejo de objetos, listas y archivos.

### 5. Estructura del proyecto

| Archivo | Descripción |
|---|---|
| aplicacion.py | Interfaz gráfica principal del sistema. |
| modelos.py | Clases, entidades y reglas del negocio. |
| sistema.py | Administración de clientes, servicios y reservas. |
| excepciones.py | Definición de excepciones personalizadas. |
| main.py | Simulación de 28 operaciones. |
| test_sistema.py | Pruebas unitarias automatizadas. |
| VERIFICAR_INSTALACION.py | Verificación del entorno de ejecución. |
| INICIAR_SOFTWARE_FJ.bat | Inicio de la aplicación en Windows. |
| .gitignore | Exclusión de archivos temporales. |
| eventos.log | Registro generado durante la ejecución. |

### 6. Requisitos del sistema

- Python 3.
- Biblioteca Tkinter para la interfaz gráfica.
- Visual Studio Code (opcional).
- GitHub Codespaces para la ejecución desde el navegador.
- No requiere bases de datos externas.

---

## 7. Ejecución desde Windows

### Paso 1. Descargar el proyecto

Ingresar al repositorio:

https://github.com/BRALLAN-HERERRA/PROGRAMACION

Seleccionar:

Code > Download ZIP

Descomprimir el archivo descargado.

### Paso 2. Abrir el proyecto

Abrir Visual Studio Code.

Seleccionar Archivo > Abrir carpeta.

Seleccionar la carpeta PROGRAMACION descargada.

### Paso 3. Verificar Python

Abrir la terminal y ejecutar:

```powershell
python --version
```

### Paso 4. Ingresar a la carpeta del sistema

```powershell
cd Software_FJ
```

### Paso 5. Ejecutar la aplicación gráfica

```powershell
python aplicacion.py
```

Se abrirá la interfaz gráfica de Software FJ.

También se puede iniciar la aplicación haciendo doble clic
sobre el archivo INICIAR_SOFTWARE_FJ.bat.

### Paso 6. Ejecutar la simulación

Desde la carpeta Software_FJ, ejecutar:

```powershell
python main.py
```

### Paso 7. Ejecutar las pruebas unitarias

```powershell
python -m unittest test_sistema -v
```

---

## 8. Ejecución desde el navegador - GitHub Codespaces

Esta modalidad permite ejecutar la simulación y las pruebas
unitarias sin instalar Python o Visual Studio Code
en el computador local.

### Paso 1. Ingresar al repositorio

https://github.com/BRALLAN-HERERRA/PROGRAMACION

### Paso 2. Abrir GitHub Codespaces

1. Iniciar sesión en GitHub.
2. Seleccionar el botón verde Code (Código).
3. Seleccionar la pestaña Codespaces (Espacios de código).
4. Abrir un espacio de trabajo existente o crear uno nuevo
   mediante Create codespace on main.
5. Esperar a que se cargue Visual Studio Code en el navegador.

### Paso 3. Abrir la terminal

Seleccionar:

Terminal > New Terminal (Nueva terminal).

### Paso 4. Ingresar a la carpeta del proyecto

```bash
cd /workspaces/PROGRAMACION/Software_FJ
```

### Paso 5. Verificar Python

```bash
python3 --version
```

### Paso 6. Ejecutar la simulación

```bash
python3 main.py
```

### Paso 7. Verificar los resultados

El resultado esperado de la simulación es:

```text
RESUMEN: 28/28 casos esperados;
17 éxitos y 11 errores controlados.
```

Los errores controlados corresponden a casos intencionales
de validación que permiten comprobar la estabilidad
del programa.

### Paso 8. Ejecutar las pruebas unitarias

```bash
python3 -m unittest test_sistema -v
```

Resultado esperado:

```text
Ran 8 tests

OK
```

### Paso 9. Verificar el estado del repositorio

```bash
git status
```

Si no existen modificaciones pendientes, se mostrará:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### Nota sobre la interfaz gráfica en Codespaces

La aplicación utiliza Tkinter, una biblioteca para
interfaces gráficas de escritorio.

GitHub Codespaces no dispone de una pantalla gráfica
configurada de forma predeterminada.

Por esta razón, ejecutar aplicacion.py desde Codespaces
puede generar el siguiente mensaje:

```text
_tkinter.TclError: no display name and no
$DISPLAY environment variable
```

Este mensaje corresponde a una limitación del entorno
gráfico y no necesariamente a un error del código fuente.

Para utilizar la interfaz gráfica se recomienda ejecutar
el proyecto en Windows o configurar un escritorio virtual
en Codespaces.

La simulación y las pruebas unitarias funcionan directamente
desde la terminal del navegador.

---

## 9. Resultados de las pruebas

| Indicador | Resultado |
|---|---:|
| Operaciones simuladas | 28 |
| Casos verificados correctamente | 28 de 28 |
| Operaciones exitosas | 17 |
| Errores controlados | 11 |
| Pruebas unitarias aprobadas | 8 de 8 |

Los resultados obtenidos permiten comprobar el comportamiento
del sistema ante operaciones válidas e inválidas y su
capacidad para continuar funcionando después de una excepción.

### 10. Almacenamiento de información

Los clientes, servicios y reservas se administran mediante
objetos y listas internas en memoria.

El archivo eventos.log registra los eventos y errores
generados durante la ejecución del sistema.

Este archivo se genera automáticamente y se excluye
del repositorio mediante .gitignore.

No se utiliza ningún motor de bases de datos.

### 11. Finalidad académica

Este proyecto fue desarrollado como parte de la Fase 4
del curso de Programación de la Universidad Nacional
Abierta y a Distancia - UNAD.

Su finalidad es demostrar la aplicación práctica de la
programación orientada a objetos y el manejo avanzado
de excepciones mediante una solución funcional, modular
y documentada.

### 12. Repositorio del proyecto

Repositorio principal:

https://github.com/BRALLAN-HERERRA/PROGRAMACION

Acceso directo al código fuente:

https://github.com/BRALLAN-HERERRA/PROGRAMACION/tree/main/Software_FJ

---

**Software FJ | Ingeniería de Sistemas | UNAD | 2026**
