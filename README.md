
# Software FJ

## Sistema Integral de Gestión de Clientes, Servicios y Reservas

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Interfaz](https://img.shields.io/badge/Interfaz-Tkinter-green)
![Pruebas](https://img.shields.io/badge/Pruebas-8%2F8-brightgreen)
![Simulación](https://img.shields.io/badge/Simulaci%C3%B3n-28%2F28-brightgreen)
![UNAD](https://img.shields.io/badge/UNAD-Fase%204-orange)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/BRALLAN-HERERRA/PROGRAMACION)

---

## 1. Información académica

| Información | Descripción |
|---|---|
| Universidad | Universidad Nacional Abierta y a Distancia - UNAD |
| Escuela | Escuela de Ciencias Básicas, Tecnología e Ingeniería - ECBTI |
| Programa | Ingeniería de Sistemas |
| Curso | Programación |
| Código del curso | 213023 |
| Grupo | 213023_651 |
| Actividad | Fase 4 - Prácticas simuladas |
| Estudiante | Brallan Smith Herrera Parrado |
| Tutora | Alejandra Giraldo Gaviria |
| Año | 2026 |

---

## 2. Descripción del proyecto

Software FJ es una aplicación de escritorio desarrollada 
en Python y Tkinter, diseñada para gestionar clientes, 
servicios y reservas de una empresa que ofrece diferentes 
modalidades de atención.

El sistema permite administrar reservas de salas, alquiler 
de equipos y asesorías especializadas, aplicando los 
principios de programación orientada a objetos y manejo 
avanzado de excepciones.

La solución se desarrolla de acuerdo con los requisitos 
establecidos en el Anexo 3 de la Fase 4 del curso de 
Programación de la UNAD.

La aplicación no utiliza motores de bases de datos. 
La información se administra mediante objetos y listas 
internas durante la ejecución del programa.

Los eventos y errores se registran en un archivo de logs, 
permitiendo identificar situaciones que puedan afectar 
el funcionamiento del sistema.

---

## 3. Objetivo del proyecto

Desarrollar una aplicación funcional, modular y organizada 
que permita gestionar clientes, servicios y reservas, 
implementando los principios de programación orientada 
a objetos y mecanismos avanzados de manejo de excepciones.

El sistema busca mantener la continuidad de las operaciones 
ante entradas inválidas, errores de cálculo y operaciones 
no permitidas.

---

## 4. Funcionalidades del sistema

### Módulo de inicio

- Panel general de indicadores.
- Cantidad de clientes registrados.
- Cantidad de servicios disponibles.
- Cantidad de reservas creadas.
- Consulta de reservas confirmadas.
- Acceso a los módulos del sistema.

### Módulo de clientes

- Registro de clientes.
- Consulta de clientes registrados.
- Validación de datos personales.
- Control de identificadores duplicados.
- Manejo de información mediante encapsulación.

### Módulo de servicios

- Registro y consulta de servicios.
- Reservas de salas.
- Alquiler de equipos.
- Asesorías especializadas.
- Validación de tarifas.
- Control de disponibilidad.
- Cálculo de costos según el tipo de servicio.

### Módulo de reservas

- Creación de reservas.
- Asociación de clientes y servicios.
- Validación de duración.
- Confirmación de reservas.
- Cancelación de reservas.
- Aplicación de impuestos y descuentos.
- Control de ocupación de servicios.
- Consulta de estados de las reservas.

### Módulo de eventos y errores

- Consulta del registro de eventos.
- Identificación de errores.
- Registro de excepciones.
- Seguimiento de operaciones registradas.
- Generación automática del archivo eventos.log.

---

## 5. Conceptos de programación aplicados

El proyecto implementa los siguientes conceptos:

- Programación orientada a objetos.
- Abstracción.
- Herencia.
- Polimorfismo.
- Encapsulación.
- Clases abstractas.
- Clases derivadas.
- Métodos sobrescritos.
- Sobrecarga simulada mediante parámetros opcionales.
- Manejo de listas internas.
- Manipulación de archivos.
- Validación de datos.
- Excepciones personalizadas.
- Encadenamiento de excepciones.
- Bloques try/except.
- Bloques try/except/else.
- Bloques try/except/finally.
- Pruebas unitarias.

El manejo de excepciones permite controlar situaciones 
inválidas y continuar con las operaciones posteriores 
en los escenarios evaluados.

---

## 6. Estructura del proyecto

```text
PROGRAMACION/
│
├── README.md
│
└── Software_FJ/
    ├── .gitignore
    ├── aplicacion.py
    ├── excepciones.py
    ├── modelos.py
    ├── sistema.py
    ├── main.py
    ├── test_sistema.py
    ├── VERIFICAR_INSTALACION.py
    └── INICIAR_SOFTWARE_FJ.bat
```

### Descripción de los archivos

| Archivo | Descripción |
|---|---|
| aplicacion.py | Interfaz gráfica principal desarrollada con Tkinter. |
| excepciones.py | Definición de excepciones personalizadas. |
| modelos.py | Entidades, clases abstractas, clases derivadas y reglas del negocio. |
| sistema.py | Administración de clientes, servicios, reservas y auditoría. |
| main.py | Simulación secuencial de 28 operaciones. |
| test_sistema.py | Pruebas unitarias automatizadas. |
| VERIFICAR_INSTALACION.py | Verificación del entorno de ejecución. |
| INICIAR_SOFTWARE_FJ.bat | Inicio de la aplicación gráfica en Windows. |
| .gitignore | Exclusión de archivos temporales y registros generados. |
| README.md | Documentación general e instrucciones de ejecución. |

El archivo eventos.log y la carpeta __pycache__ se 
generan durante la ejecución del sistema y no forman 
parte del código fuente publicado.

---

## 7. Requisitos del sistema

### Para ejecución local

- Sistema operativo Windows 10 o Windows 11.
- Python 3.
- Biblioteca Tkinter.
- Visual Studio Code (opcional).

### Para ejecución desde el navegador

- Navegador web.
- Conexión a Internet.
- Cuenta de GitHub para utilizar GitHub Codespaces.
- Disponibilidad de cuota de GitHub Codespaces.

El proyecto no requiere instalar un motor de bases 
de datos ni bibliotecas externas de terceros.

---

## 8. Acceso público al proyecto

El repositorio de Software FJ es público.

Cualquier persona puede realizar las siguientes 
actividades sin iniciar sesión en GitHub:

- Consultar el código fuente.
- Revisar los archivos del proyecto.
- Leer la documentación.
- Descargar el proyecto en formato ZIP.
- Ejecutar el proyecto descargado en su computador.

### Repositorio principal

https://github.com/BRALLAN-HERERRA/PROGRAMACION

### Acceso directo al código fuente

https://github.com/BRALLAN-HERERRA/PROGRAMACION/tree/main/Software_FJ

### Descargar el proyecto completo

[Descargar Software FJ en formato ZIP](https://github.com/BRALLAN-HERERRA/PROGRAMACION/archive/refs/heads/main.zip)

No se requiere una cuenta de GitHub para consultar 
o descargar el repositorio público.

El inicio de sesión únicamente será necesario para 
utilizar servicios como GitHub Codespaces o realizar 
modificaciones en el repositorio con los permisos 
correspondientes.

---

## 9. Ejecución de la aplicación en Windows

### Paso 1. Descargar el proyecto

Ingresar al siguiente enlace:

https://github.com/BRALLAN-HERERRA/PROGRAMACION

Seleccionar el botón verde:

Code (Código) > Download ZIP (Descargar ZIP).

También se puede descargar directamente desde:

[Descargar proyecto ZIP](https://github.com/BRALLAN-HERERRA/PROGRAMACION/archive/refs/heads/main.zip)

### Paso 2. Descomprimir el proyecto

Extraer el contenido del archivo ZIP descargado 
en una carpeta del computador.

### Paso 3. Abrir el proyecto en Visual Studio Code

1. Abrir Visual Studio Code.
2. Seleccionar Archivo.
3. Seleccionar Abrir carpeta.
4. Seleccionar la carpeta PROGRAMACION-main.
5. Abrir la terminal integrada.

### Paso 4. Verificar la instalación de Python

Ejecutar el siguiente comando:

```powershell
python --version
```

El sistema deberá mostrar la versión de Python 
instalada en el computador.

Si Python no se encuentra instalado, puede 
descargarse desde su página oficial:

https://www.python.org/downloads/

### Paso 5. Ingresar a la carpeta del sistema

Desde la carpeta principal del proyecto, ejecutar:

```powershell
cd Software_FJ
```

### Paso 6. Verificar el entorno de ejecución

```powershell
python VERIFICAR_INSTALACION.py
```

Este archivo permite comprobar las condiciones 
del entorno necesarias para ejecutar el sistema.

### Paso 7. Ejecutar la interfaz gráfica

```powershell
python aplicacion.py
```

Se abrirá la ventana principal de Software FJ, 
desde la cual se podrá acceder a los módulos de 
clientes, servicios, reservas y eventos.

### Método alternativo de ejecución

También se puede iniciar la aplicación haciendo 
doble clic sobre el archivo:

```text
INICIAR_SOFTWARE_FJ.bat
```

Este archivo está diseñado para facilitar el inicio 
de la aplicación desde Windows.

### Paso 8. Ejecutar la simulación

Desde la carpeta Software_FJ, ejecutar:

```powershell
python main.py
```

### Paso 9. Ejecutar las pruebas unitarias

```powershell
python -m unittest test_sistema -v
```

---

## 10. Ejecución desde el navegador - GitHub Codespaces

GitHub Codespaces permite utilizar Visual Studio Code 
directamente desde el navegador y ejecutar Python 
en un entorno de desarrollo remoto.

Esta modalidad no requiere instalar Python ni 
Visual Studio Code en el computador local.

Aunque el repositorio es público, para crear o 
utilizar un Codespace se requiere iniciar sesión 
con una cuenta de GitHub y disponer de cuota de uso.

### Acceso directo a GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/BRALLAN-HERERRA/PROGRAMACION)

### Paso 1. Ingresar al repositorio

https://github.com/BRALLAN-HERERRA/PROGRAMACION

### Paso 2. Abrir Visual Studio Code en el navegador

1. Seleccionar el botón verde Code (Código).
2. Seleccionar la pestaña Codespaces 
   (Espacios de código).
3. Seleccionar un espacio de trabajo existente 
   o Create codespace on main.
4. Iniciar sesión en GitHub si se solicita.
5. Esperar a que se cargue el entorno de desarrollo.

También puede utilizarse el botón de acceso directo 
a Codespaces ubicado en este documento.

### Paso 3. Abrir la terminal

En Visual Studio Code seleccionar:

Terminal > New Terminal (Nueva terminal).

### Paso 4. Ingresar a la carpeta del proyecto

Ejecutar el siguiente comando:

```bash
cd /workspaces/PROGRAMACION/Software_FJ
```

### Paso 5. Verificar la versión de Python

```bash
python3 --version
```

### Paso 6. Ejecutar la simulación del sistema

```bash
python3 main.py
```

El sistema ejecutará automáticamente los 28 casos 
de simulación, incluyendo operaciones válidas 
e inválidas.

Al finalizar, se espera obtener:

```text
RESUMEN: 28/28 casos esperados; 
17 éxitos y 11 errores controlados.
```

Los errores controlados corresponden a escenarios 
de prueba intencionales que permiten comprobar 
el manejo de excepciones.

### Paso 7. Ejecutar las pruebas unitarias

```bash
python3 -m unittest test_sistema -v
```

Resultado esperado:

```text
Ran 8 tests

OK
```

El mensaje OK indica que todas las pruebas unitarias 
ejecutadas finalizaron satisfactoriamente.

### Paso 8. Consultar el archivo de eventos

Después de ejecutar la simulación, se puede consultar 
el archivo de auditoría mediante:

```bash
cat eventos.log
```

Si el archivo fue generado en otro directorio, 
se puede localizar mediante:

```bash
find .. -name "eventos.log"
```

### Paso 9. Verificar el estado del repositorio

```bash
git status
```

Si no existen modificaciones pendientes, se espera 
obtener un mensaje similar al siguiente:

```text
On branch main

Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Esto indica que la rama local se encuentra sincronizada 
con el estado conocido de la rama remota y que no 
existen cambios pendientes en la carpeta de trabajo.

---

## 11. Consideraciones sobre la interfaz gráfica en la web

Software FJ utiliza Tkinter, una biblioteca de Python 
orientada al desarrollo de aplicaciones de escritorio.

GitHub Codespaces no dispone de una pantalla gráfica 
configurada de manera predeterminada.

Por lo tanto, al ejecutar el archivo aplicacion.py 
en Codespaces puede aparecer el siguiente mensaje:

```text
_tkinter.TclError: no display name and no 
$DISPLAY environment variable
```

Este mensaje corresponde a la ausencia de un entorno 
gráfico configurado y no necesariamente a un error 
en la lógica del programa.

Para visualizar la interfaz gráfica se recomienda 
utilizar alguna de las siguientes alternativas:

- Ejecutar el proyecto directamente en Windows.
- Configurar un escritorio virtual en Codespaces.

La simulación y las pruebas unitarias pueden 
ejecutarse directamente desde el navegador sin 
necesidad de configurar un escritorio virtual.

### Comparación de modalidades de ejecución

| Funcionalidad | Windows | GitHub Codespaces |
|---|---|---|
| Consultar código fuente | Sí | Sí |
| Editar código fuente | Sí | Sí |
| Ejecutar simulación | Sí | Sí |
| Ejecutar pruebas unitarias | Sí | Sí |
| Generar archivo de logs | Sí | Sí |
| Interfaz gráfica Tkinter | Sí | Requiere entorno gráfico |
| Instalación local de Python | Sí | No |
| Cuenta de GitHub | No | Sí |

---

## 12. Resultados de las pruebas realizadas

El funcionamiento del sistema fue comprobado mediante 
la ejecución de la simulación y las pruebas unitarias 
en GitHub Codespaces.

### Resultados generales

| Indicador | Resultado |
|---|---:|
| Operaciones simuladas | 28 |
| Casos verificados correctamente | 28 de 28 |
| Operaciones exitosas | 17 |
| Errores controlados | 11 |
| Pruebas unitarias aprobadas | 8 de 8 |
| Coincidencia con los resultados esperados | 100 % |

Los resultados demuestran que el sistema responde 
correctamente a los escenarios evaluados y continúa 
ejecutando las operaciones posteriores cuando se 
presentan excepciones controladas.

---

## 13. Pruebas unitarias implementadas

| Prueba | Descripción | Resultado |
|---|---|---|
| test_abstractas | Validación de clases abstractas. | OK |
| test_costos | Comprobación del cálculo de costos. | OK |
| test_datos_invalidos | Validación de datos incorrectos. | OK |
| test_disponibilidad | Control de disponibilidad. | OK |
| test_duplicado_y_encapsulacion | Duplicados y encapsulación. | OK |
| test_encadenamiento | Encadenamiento de excepciones. | OK |
| test_estado_atomico | Conservación del estado ante errores. | OK |
| test_ocupacion | Control de servicios ocupados. | OK |

Las ocho pruebas unitarias fueron ejecutadas 
satisfactoriamente en GitHub Codespaces.

---

## 14. Manejo de errores y excepciones

El proyecto incorpora mecanismos para controlar 
situaciones que puedan afectar la ejecución normal 
del sistema.

Entre los casos evaluados se encuentran:

- Datos personales inválidos.
- Identificadores duplicados.
- Clientes inexistentes.
- Tarifas incorrectas.
- Servicios no disponibles.
- Duraciones fuera de los límites permitidos.
- Descuentos inválidos.
- Parámetros obligatorios faltantes.
- Reservas incorrectas.
- Operaciones no permitidas.
- Intentos de utilizar servicios ocupados.

Los errores gestionados durante la simulación se 
registran en el archivo eventos.log, permitiendo 
consultar posteriormente la información de auditoría.

---

## 15. Almacenamiento de información

El sistema no utiliza bases de datos.

La información relacionada con clientes, servicios 
y reservas se administra mediante objetos y listas 
internas durante la ejecución de la aplicación.

El archivo:

```text
eventos.log
```

se utiliza para registrar eventos y errores.

Este archivo se genera automáticamente durante 
la ejecución y se excluye del repositorio mediante 
las reglas establecidas en .gitignore.

Los datos operativos permanecen en memoria 
durante la sesión de trabajo.

Al cerrar la aplicación, los registros almacenados 
en las listas internas no se conservan de forma 
permanente.

Esta característica responde a las condiciones 
establecidas en el Anexo 3 de la actividad académica.

---

## 16. Organización y control de versiones

El proyecto se encuentra publicado en GitHub 
para facilitar:

- La consulta del código fuente.
- La documentación del desarrollo.
- El seguimiento de modificaciones.
- El control de versiones.
- La colaboración entre los integrantes autorizados.
- La revisión académica por parte de la tutora.
- La ejecución de pruebas desde Codespaces.

El archivo .gitignore permite excluir los archivos 
temporales generados durante el funcionamiento 
del sistema, evitando publicar información 
innecesaria en el repositorio.

---

## 17. Finalidad académica

Software FJ fue desarrollado como parte de la 
Fase 4 - Prácticas simuladas del curso de 
Programación de la Universidad Nacional Abierta 
y a Distancia - UNAD.

Su finalidad es demostrar la aplicación práctica 
de los conocimientos adquiridos sobre programación 
orientada a objetos, manejo avanzado de excepciones, 
validación de datos, modularidad y desarrollo 
de aplicaciones mediante Python.

El proyecto integra una solución funcional de 
escritorio con mecanismos de simulación y pruebas 
automatizadas que permiten evaluar su comportamiento 
ante diferentes situaciones.

---

## 18. Referencias bibliográficas

- Universidad Nacional Abierta y a Distancia. (s. f.).
  Anexo 3: Problema a desarrollar Fase 4.

- Universidad Nacional Abierta y a Distancia. (2026).
  Guía de aprendizaje para el desarrollo del 
  componente práctico del curso Programación 213023.

- Van Rossum, G., & Drake, F. L., Jr. (2024).
  El tutorial de Python: errores y excepciones.
  Python Software Foundation.
  https://docs.python.org/es/3.12/tutorial/errors.html

- Zambrano, J. P. (2025).
  Introducción al uso de GitHub.
  Repositorio Institucional UNAD.
  https://repository.unad.edu.co/handle/10596/75876

---

## 19. Enlaces de acceso rápido

- [Repositorio principal](https://github.com/BRALLAN-HERERRA/PROGRAMACION)
- [Consultar código fuente](https://github.com/BRALLAN-HERERRA/PROGRAMACION/tree/main/Software_FJ)
- [Descargar proyecto ZIP](https://github.com/BRALLAN-HERERRA/PROGRAMACION/archive/refs/heads/main.zip)
- [Ejecutar desde GitHub Codespaces](https://codespaces.new/BRALLAN-HERERRA/PROGRAMACION)
- [Documentación oficial de Python](https://docs.python.org/es/3/)

---

## Desarrollado por

**Brallan Smith Herrera Parrado**

Estudiante de Ingeniería de Sistemas.

Universidad Nacional Abierta y a Distancia - UNAD.

Escuela de Ciencias Básicas, Tecnología e Ingeniería.

**Software FJ | Fase 4 | Programación | 2026**
