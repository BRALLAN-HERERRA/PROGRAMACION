"""Interfaz gráfica de escritorio para Software FJ.

La ventana utiliza Tkinter, biblioteca incluida con la mayoría de las
instalaciones de Python. Los formularios se integran en la pestaña activa,
sin abrir ventanas secundarias para registrar o editar información. La lógica
 del negocio NO se repite aquí: todos
los registros y operaciones se delegan a la clase Sistema y a los
modelos Cliente, Sala, Equipo, Asesoria y Reserva.

Ejecución: python aplicacion.py
"""

# ----------------------------- IMPORTACIONES -----------------------------
import tkinter as tk                         # Biblioteca base para crear ventanas.
from tkinter import ttk, messagebox          # Controles modernos y cuadros de diálogo.
from decimal import Decimal                  # Permite convertir porcentajes sin errores binarios.
from pathlib import Path                     # Facilita localizar el archivo eventos.log.

from sistema import Sistema                  # Controlador que administra las listas en memoria.
from modelos import Sala, Equipo, Asesoria    # Tipos concretos de servicios del proyecto.
from excepciones import ErrorSistema          # Excepciones propias de las reglas del negocio.


# ----------------------------- CONFIGURACIÓN ------------------------------
COLOR_FONDO = "#F3F6FB"                      # Fondo general de la aplicación.
COLOR_AZUL = "#173B68"                       # Color institucional principal.
COLOR_AZUL_CLARO = "#E7EFF8"                  # Fondo secundario para tarjetas.
COLOR_TEXTO = "#243247"                      # Color de textos principales.
COLOR_VERDE = "#18845B"                      # Color de indicadores positivos.


class FormularioIntegrado(ttk.Frame):
    """Panel reutilizable que representa un formulario dentro de una pestaña.

    Al llamar destroy(), se elimina el formulario y se ejecuta una función
    que restaura los controles originales del módulo. Así se evita crear
    ventanas Toplevel adicionales para registrar clientes, servicios o reservas.
    """

    def __init__(self, master, al_cerrar):
        super().__init__(master, padding=10)
        self._al_cerrar = al_cerrar
        self._cerrando = False

    def destroy(self):
        """Cierra el panel una sola vez y restaura la pantalla del módulo."""
        if self._cerrando:
            return
        self._cerrando = True
        super().destroy()
        self._al_cerrar()


class AplicacionSoftwareFJ(tk.Tk):
    """Ventana principal y punto de entrada de la interfaz gráfica."""

    def __init__(self):
        # Inicializa la ventana raíz de Tkinter.
        super().__init__()

        # Crea una única instancia del sistema; las pestañas comparten
        # este objeto para consultar y modificar las mismas listas internas.
        self.sistema = Sistema()

        # Configura título, tamaño inicial y tamaño mínimo de la ventana.
        self.title("Software FJ | Gestión de clientes, servicios y reservas")
        self.geometry("1180x760")
        self.minsize(980, 650)
        self.configure(bg=COLOR_FONDO)

        # Construye los estilos visuales antes de crear los controles.
        self._configurar_estilos()

        # Crea la estructura visual general de la aplicación.
        self._construir_encabezado()
        self._construir_contenido()

        # Carga en pantalla los registros que existan en la sesión.
        self.actualizar_todo()

        # Registra el inicio de la aplicación en el archivo de auditoría.
        self.sistema.log.info("APLICACIÓN GRÁFICA INICIADA")

        # Intercepta el cierre de la ventana para dejar constancia en el log.
        self.protocol("WM_DELETE_WINDOW", self._cerrar_aplicacion)

    def _configurar_estilos(self):
        """Define tipografías, colores y apariencia de tablas y botones."""
        estilos = ttk.Style(self)
        estilos.theme_use("clam")
        estilos.configure("TFrame", background=COLOR_FONDO)
        estilos.configure("TLabel", background=COLOR_FONDO, foreground=COLOR_TEXTO,
                          font=("Segoe UI", 10))
        estilos.configure("Titulo.TLabel", font=("Segoe UI", 20, "bold"),
                          foreground=COLOR_AZUL)
        estilos.configure("Subtitulo.TLabel", font=("Segoe UI", 10), foreground="#617086")
        estilos.configure("TButton", font=("Segoe UI", 10), padding=(12, 7))
        estilos.configure("Primario.TButton", background=COLOR_AZUL,
                          foreground="white", font=("Segoe UI", 10, "bold"))
        estilos.map("Primario.TButton", background=[("active", "#24558C")])
        estilos.configure("Treeview", rowheight=30, font=("Segoe UI", 9),
                          background="white", fieldbackground="white")
        estilos.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"),
                          background=COLOR_AZUL_CLARO, foreground=COLOR_AZUL)
        estilos.configure("TNotebook", background=COLOR_FONDO, borderwidth=0)
        estilos.configure("TNotebook.Tab", padding=(18, 10), font=("Segoe UI", 10, "bold"))

    def _construir_encabezado(self):
        """Crea la franja superior con el nombre y la descripción del sistema."""
        encabezado = tk.Frame(self, bg=COLOR_AZUL, height=92)
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        tk.Label(encabezado, text="SOFTWARE FJ", bg=COLOR_AZUL, fg="white",
                 font=("Segoe UI", 22, "bold")).pack(anchor="w", padx=28, pady=(15, 0))
        tk.Label(encabezado, text="Sistema integral de gestión de clientes, servicios y reservas",
                 bg=COLOR_AZUL, fg="#DCE8F5", font=("Segoe UI", 10)).pack(anchor="w", padx=30)

    def _construir_contenido(self):
        """Crea las pestañas funcionales de la aplicación."""
        contenedor = ttk.Frame(self, padding=(20, 18))
        contenedor.pack(fill="both", expand=True)

        # Notebook organiza los módulos en pestañas para facilitar la navegación.
        self.pestanas = ttk.Notebook(contenedor)
        self.pestanas.pack(fill="both", expand=True)

        # Cada módulo se construye en un Frame independiente.
        self.tab_inicio = ttk.Frame(self.pestanas, padding=18)
        self.tab_clientes = ttk.Frame(self.pestanas, padding=18)
        self.tab_servicios = ttk.Frame(self.pestanas, padding=18)
        self.tab_reservas = ttk.Frame(self.pestanas, padding=18)
        self.tab_logs = ttk.Frame(self.pestanas, padding=18)

        self.pestanas.add(self.tab_inicio, text="  Inicio  ")
        self.pestanas.add(self.tab_clientes, text="  Clientes  ")
        self.pestanas.add(self.tab_servicios, text="  Servicios  ")
        self.pestanas.add(self.tab_reservas, text="  Reservas  ")
        self.pestanas.add(self.tab_logs, text="  Eventos y errores  ")

        self._crear_inicio()
        self._crear_modulo_clientes()
        self._crear_modulo_servicios()
        self._crear_modulo_reservas()
        self._crear_modulo_logs()

    # ================================ INICIO ================================
    def _crear_inicio(self):
        """Construye el panel de indicadores generales."""
        ttk.Label(self.tab_inicio, text="Panel general", style="Titulo.TLabel").pack(anchor="w")
        ttk.Label(self.tab_inicio, text="Resumen de la información registrada durante esta sesión.",
                  style="Subtitulo.TLabel").pack(anchor="w", pady=(2, 18))

        tarjetas = ttk.Frame(self.tab_inicio)
        tarjetas.pack(fill="x", pady=(0, 20))
        self.indicadores = {}
        for clave, titulo in (("clientes", "Clientes"), ("servicios", "Servicios"),
                              ("reservas", "Reservas"), ("confirmadas", "Confirmadas")):
            tarjeta = tk.Frame(tarjetas, bg="white", highlightbackground="#DCE4EF",
                               highlightthickness=1, padx=18, pady=15)
            tarjeta.pack(side="left", fill="both", expand=True, padx=(0, 12))
            tk.Label(tarjeta, text=titulo.upper(), bg="white", fg="#65758B",
                     font=("Segoe UI", 9, "bold")).pack(anchor="w")
            valor = tk.Label(tarjeta, text="0", bg="white", fg=COLOR_AZUL,
                             font=("Segoe UI", 25, "bold"))
            valor.pack(anchor="w", pady=(5, 0))
            self.indicadores[clave] = valor

        tk.Label(self.tab_inicio, text="¿Qué puedes hacer?", bg=COLOR_FONDO,
                 fg=COLOR_AZUL, font=("Segoe UI", 13, "bold")).pack(anchor="w", pady=(5, 8))
        acciones = [
            "• Registrar clientes con validación de correo y teléfono.",
            "• Crear salas, alquileres de equipos y asesorías especializadas.",
            "• Generar reservas, calcular su valor y confirmar o cancelar operaciones.",
            "• Consultar el historial de eventos y errores registrados en eventos.log.",
            "• Trabajar sin base de datos: los objetos se conservan en memoria mientras la aplicación está abierta.",
        ]
        for texto in acciones:
            ttk.Label(self.tab_inicio, text=texto).pack(anchor="w", pady=5)

        aviso = tk.Frame(self.tab_inicio, bg=COLOR_AZUL_CLARO, padx=15, pady=12)
        aviso.pack(fill="x", side="bottom", pady=(25, 0))
        tk.Label(aviso, text="Nota académica", bg=COLOR_AZUL_CLARO, fg=COLOR_AZUL,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w")
        tk.Label(aviso, text="Los valores y tarifas son datos simulados para demostrar la lógica del ejercicio.",
                 bg=COLOR_AZUL_CLARO, fg=COLOR_TEXTO, font=("Segoe UI", 9)).pack(anchor="w", pady=(3, 0))

    # =============================== CLIENTES ===============================
    def _crear_modulo_clientes(self):
        """Prepara la tabla y las acciones del módulo de clientes."""
        self._titulo_modulo(self.tab_clientes, "Gestión de clientes",
                            "Registra y consulta los datos personales validados.")
        barra = ttk.Frame(self.tab_clientes)
        barra.pack(fill="x", pady=(0, 12))
        ttk.Button(barra, text="＋ Nuevo cliente", style="Primario.TButton",
                   command=self._formulario_cliente).pack(side="left")
        ttk.Button(barra, text="↻ Actualizar", command=self._actualizar_clientes).pack(side="left", padx=8)

        columnas = ("codigo", "nombre", "correo", "telefono")
        self.tabla_clientes = self._crear_tabla(self.tab_clientes, columnas,
            ("Código", "Nombre", "Correo electrónico", "Teléfono"),
            (100, 220, 280, 150))

    def _formulario_cliente(self):
        """Solicita los datos de un cliente y los envía al modelo Sistema."""
        ventana = self._ventana_formulario("Registrar cliente", 460, 360)
        campos = self._campos_formulario(ventana, [
            ("Código", "codigo"), ("Nombre completo", "nombre"),
            ("Correo electrónico", "correo"), ("Teléfono (solo números)", "telefono")])

        def guardar():
            try:
                # El sistema crea el objeto Cliente y ejecuta sus validaciones.
                cliente = self.sistema.registrar_cliente(
                    campos["codigo"].get(), campos["nombre"].get(),
                    campos["correo"].get(), campos["telefono"].get())
            except ErrorSistema as error:
                # Los errores esperados se muestran sin cerrar la ventana principal.
                self.sistema.log.exception("GUI | Error al registrar cliente")
                messagebox.showerror("No se pudo registrar", str(error), parent=ventana)
                return
            except Exception as error:
                # Captura adicional para evitar que un error inesperado cierre la aplicación.
                self.sistema.log.exception("GUI | Error inesperado al registrar cliente")
                messagebox.showerror("Error inesperado", str(error), parent=ventana)
                return
            else:
                messagebox.showinfo("Cliente registrado", cliente.describir(), parent=ventana)
                ventana.destroy()
                self.actualizar_todo()
            finally:
                # El bloque finally deja constancia del intento, haya sido exitoso o no.
                self.sistema.log.info("FIN GUI | intento de registro de cliente")

        ttk.Button(ventana, text="Guardar cliente", style="Primario.TButton",
                   command=guardar).pack(pady=18)

    # =============================== SERVICIOS ==============================
    def _crear_modulo_servicios(self):
        """Prepara la tabla y el formulario para las tres clases de servicio."""
        self._titulo_modulo(self.tab_servicios, "Catálogo de servicios",
                            "Cada servicio aplica sus propias reglas mediante polimorfismo.")
        barra = ttk.Frame(self.tab_servicios)
        barra.pack(fill="x", pady=(0, 12))
        ttk.Button(barra, text="＋ Nuevo servicio", style="Primario.TButton",
                   command=self._formulario_servicio).pack(side="left")
        ttk.Button(barra, text="↻ Actualizar", command=self._actualizar_servicios).pack(side="left", padx=8)

        self.tabla_servicios = self._crear_tabla(self.tab_servicios,
            ("codigo", "tipo", "nombre", "tarifa", "disponible"),
            ("Código", "Tipo", "Nombre", "Tarifa por hora (COP)", "Disponible"),
            (90, 130, 220, 180, 110))

    def _formulario_servicio(self):
        """Crea un servicio especializado según el tipo seleccionado."""
        ventana = self._ventana_formulario("Crear servicio", 470, 390)
        tipo_var = tk.StringVar(value="Sala")
        ttk.Label(ventana, text="Tipo de servicio").pack(anchor="w", padx=22, pady=(12, 3))
        selector = ttk.Combobox(ventana, textvariable=tipo_var,
                                values=("Sala", "Equipo", "Asesoría"), state="readonly")
        selector.pack(fill="x", padx=22)
        campos = self._campos_formulario(ventana, [
            ("Código", "codigo"), ("Nombre del servicio", "nombre"),
            ("Tarifa por hora (COP)", "tarifa")])

        def guardar():
            try:
                codigo = campos["codigo"].get()
                nombre = campos["nombre"].get()
                tarifa = campos["tarifa"].get()
                tipo = tipo_var.get()
                # Se instancia una subclase concreta de Servicio.
                # El sistema recibe el objeto por su clase base y lo administra
                # sin necesitar conocer la fórmula interna de cada servicio.
                if tipo == "Sala":
                    servicio = Sala(codigo, nombre, tarifa)
                elif tipo == "Equipo":
                    servicio = Equipo(codigo, nombre, tarifa)
                elif tipo == "Asesoría":
                    servicio = Asesoria(codigo, nombre, tarifa)
                else:
                    raise ValueError("Seleccione un tipo de servicio válido.")

                self.sistema.registrar_servicio(servicio)
            except ErrorSistema as error:
                self.sistema.log.exception("GUI | Error al crear servicio")
                messagebox.showerror("No se pudo crear", str(error), parent=ventana)
                return
            except (ValueError, TypeError) as error:
                self.sistema.log.exception("GUI | Parámetros incorrectos del servicio")
                messagebox.showerror("Datos incorrectos", str(error), parent=ventana)
                return
            except Exception as error:
                self.sistema.log.exception("GUI | Error inesperado al crear servicio")
                messagebox.showerror("Error inesperado", str(error), parent=ventana)
                return
            else:
                messagebox.showinfo("Servicio creado", servicio.describir(), parent=ventana)
                ventana.destroy()
                self.actualizar_todo()
            finally:
                self.sistema.log.info("FIN GUI | intento de creación de servicio")

        ttk.Button(ventana, text="Guardar servicio", style="Primario.TButton",
                   command=guardar).pack(pady=18)

    # ================================ RESERVAS ==============================
    def _crear_modulo_reservas(self):
        """Prepara la tabla y los botones para gestionar reservas."""
        self._titulo_modulo(self.tab_reservas, "Gestión de reservas",
                            "Crea una reserva, confirma su costo o cancela una operación.")
        barra = ttk.Frame(self.tab_reservas)
        barra.pack(fill="x", pady=(0, 12))
        ttk.Button(barra, text="＋ Nueva reserva", style="Primario.TButton",
                   command=self._formulario_reserva).pack(side="left")
        ttk.Button(barra, text="✓ Confirmar seleccionada", command=self._confirmar_reserva).pack(side="left", padx=8)
        ttk.Button(barra, text="Cancelar seleccionada", command=self._cancelar_reserva).pack(side="left")
        ttk.Button(barra, text="↻ Actualizar", command=self._actualizar_reservas).pack(side="right")

        self.tabla_reservas = self._crear_tabla(self.tab_reservas,
            ("codigo", "cliente", "servicio", "duracion", "estado", "total"),
            ("Código", "Cliente", "Servicio", "Horas", "Estado", "Total (COP)"),
            (90, 180, 180, 75, 120, 150))

    def _formulario_reserva(self):
        """Permite seleccionar cliente y servicio registrados y crear la reserva."""
        clientes = self.sistema.obtener_clientes()
        servicios = self.sistema.obtener_servicios()
        if not clientes or not servicios:
            messagebox.showwarning("Faltan registros",
                "Primero debes registrar al menos un cliente y un servicio.", parent=self)
            return

        ventana = self._ventana_formulario("Crear reserva", 500, 390)
        cliente_var = tk.StringVar(value=clientes[0].codigo)
        servicio_var = tk.StringVar(value=servicios[0].codigo)
        # Los controles muestran una descripción amigable; al guardar,
        # se extrae el código situado antes del separador " - ".
        cliente_combo = self._selector_formulario(
            ventana, "Cliente", cliente_var,
            [f"{c.codigo} - {c.nombre}" for c in clientes])
        servicio_combo = self._selector_formulario(
            ventana, "Servicio", servicio_var,
            [f"{s.codigo} - {s.etiqueta()}" for s in servicios])

        campos = self._campos_formulario(ventana, [("Código de reserva", "codigo"),
                                                    ("Duración en horas", "duracion")])

        def guardar():
            try:
                codigo_cliente = cliente_combo.get().split(" - ", 1)[0]
                codigo_servicio = servicio_combo.get().split(" - ", 1)[0]
                reserva = self.sistema.crear_reserva(
                    campos["codigo"].get(), codigo_cliente,
                    codigo_servicio, campos["duracion"].get())
            except ErrorSistema as error:
                self.sistema.log.exception("GUI | Error al crear reserva")
                messagebox.showerror("No se pudo crear la reserva", str(error), parent=ventana)
                return
            except Exception as error:
                self.sistema.log.exception("GUI | Error inesperado al crear reserva")
                messagebox.showerror("Error inesperado", str(error), parent=ventana)
                return
            else:
                messagebox.showinfo("Reserva creada", reserva.describir(), parent=ventana)
                ventana.destroy()
                self.actualizar_todo()
            finally:
                self.sistema.log.info("FIN GUI | intento de creación de reserva")

        ttk.Button(ventana, text="Guardar reserva", style="Primario.TButton",
                   command=guardar).pack(pady=18)

    def _confirmar_reserva(self):
        """Solicita porcentajes opcionales y confirma la reserva seleccionada."""
        codigo = self._codigo_seleccionado(self.tabla_reservas)
        if not codigo:
            messagebox.showwarning("Selecciona una reserva", "Elige una fila de la tabla.", parent=self)
            return
        ventana = self._ventana_formulario("Confirmar reserva", 390, 270)
        campos = self._campos_formulario(ventana, [
            ("Impuesto (%)", "impuesto"), ("Descuento adicional (%)", "descuento")])
        campos["impuesto"].insert(0, "19")
        campos["descuento"].insert(0, "0")

        def confirmar():
            try:
                # Decimal permite validar los porcentajes antes de enviarlos al modelo.
                impuesto = Decimal(campos["impuesto"].get())
                descuento = Decimal(campos["descuento"].get())
                total = self.sistema.confirmar_reserva(codigo, impuesto, descuento)
            except (ErrorSistema, ArithmeticError, ValueError) as error:
                self.sistema.log.exception("GUI | Error al confirmar reserva %s", codigo)
                messagebox.showerror("No se pudo confirmar", str(error), parent=ventana)
                return
            except Exception as error:
                self.sistema.log.exception("GUI | Error inesperado al confirmar reserva")
                messagebox.showerror("Error inesperado", str(error), parent=ventana)
                return
            else:
                messagebox.showinfo("Reserva confirmada", f"Total a pagar: ${total:,.2f} COP", parent=ventana)
                ventana.destroy()
                self.actualizar_todo()
            finally:
                self.sistema.log.info("FIN GUI | intento de confirmación %s", codigo)

        ttk.Button(ventana, text="Calcular y confirmar", style="Primario.TButton",
                   command=confirmar).pack(pady=18)

    def _cancelar_reserva(self):
        """Cancela la reserva que el usuario haya seleccionado en la tabla."""
        codigo = self._codigo_seleccionado(self.tabla_reservas)
        if not codigo:
            messagebox.showwarning("Selecciona una reserva", "Elige una fila de la tabla.", parent=self)
            return
        if not messagebox.askyesno("Confirmar cancelación",
                                   f"¿Deseas cancelar la reserva {codigo}?", parent=self):
            return
        try:
            reserva = self.sistema.cancelar_reserva(codigo)
        except ErrorSistema as error:
            self.sistema.log.exception("GUI | Error al cancelar reserva %s", codigo)
            messagebox.showerror("No se pudo cancelar", str(error), parent=self)
        except Exception as error:
            self.sistema.log.exception("GUI | Error inesperado al cancelar reserva")
            messagebox.showerror("Error inesperado", str(error), parent=self)
        else:
            messagebox.showinfo("Reserva cancelada", reserva.describir(), parent=self)
        finally:
            self.sistema.log.info("FIN GUI | intento de cancelación %s", codigo)
            self.actualizar_todo()

    # =========================== EVENTOS Y ERRORES =========================
    def _crear_modulo_logs(self):
        """Muestra el contenido del archivo de auditoría del sistema."""
        self._titulo_modulo(self.tab_logs, "Eventos y errores",
                            "Consulta los intentos exitosos y los errores capturados por la aplicación.")
        barra = ttk.Frame(self.tab_logs)
        barra.pack(fill="x", pady=(0, 10))
        ttk.Button(barra, text="↻ Recargar registro", command=self._actualizar_logs).pack(side="left")
        ttk.Button(barra, text="Limpiar vista", command=lambda: self.consola_logs.delete("1.0", "end")).pack(side="left", padx=8)
        self.consola_logs = tk.Text(self.tab_logs, wrap="word", font=("Consolas", 9),
                                    bg="#142235", fg="#DCE7F4", insertbackground="white",
                                    relief="flat", padx=12, pady=12)
        self.consola_logs.pack(fill="both", expand=True)
        self._actualizar_logs()

    def _actualizar_logs(self):
        """Lee eventos.log; si todavía no existe, informa que no hay eventos."""
        ruta_log = Path(__file__).with_name("eventos.log")
        try:
            contenido = ruta_log.read_text(encoding="utf-8") if ruta_log.exists() else "Todavía no hay eventos registrados."
        except OSError as error:
            contenido = f"No fue posible leer el archivo de eventos: {error}"
        self.consola_logs.delete("1.0", "end")
        self.consola_logs.insert("1.0", contenido)
        self.consola_logs.see("end")

    # =========================== MÉTODOS DE APOYO ==========================
    def _titulo_modulo(self, padre, titulo, subtitulo):
        """Agrega un título y una explicación breve a cada pestaña."""
        ttk.Label(padre, text=titulo, style="Titulo.TLabel").pack(anchor="w")
        ttk.Label(padre, text=subtitulo, style="Subtitulo.TLabel").pack(anchor="w", pady=(2, 18))

    def _crear_tabla(self, padre, columnas, titulos, anchos):
        """Crea un Treeview con encabezados, columnas y barra de desplazamiento."""
        marco = ttk.Frame(padre)
        marco.pack(fill="both", expand=True)
        tabla = ttk.Treeview(marco, columns=columnas, show="headings", selectmode="browse")
        for columna, titulo, ancho in zip(columnas, titulos, anchos):
            tabla.heading(columna, text=titulo)
            tabla.column(columna, width=ancho, minwidth=65, anchor="w")
        scroll = ttk.Scrollbar(marco, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=scroll.set)
        tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        return tabla

    def _ventana_formulario(self, titulo, ancho, alto):
        """Muestra el formulario dentro de la pestaña activa, sin abrir otra ventana.

        Se conserva el nombre del método para no modificar la lógica de los
        formularios existentes. En esta versión, el formulario se incrusta en
        el área principal: se ocultan temporalmente los controles del módulo,
        se muestra el formulario y, al cerrarlo, se restaura la vista anterior.
        Los parámetros ancho y alto se conservan por compatibilidad, aunque
        el tamaño ahora se adapta al espacio disponible en la ventana principal.
        """
        # Identifica la pestaña desde la cual se solicitó abrir el formulario.
        identificador = self.pestanas.select()
        pestaña_activa = self.nametowidget(identificador)

        # Guarda los controles que actualmente están visibles y su configuración
        # de posicionamiento para poder restaurarlos exactamente al terminar.
        controles_ocultos = []
        for control in pestaña_activa.winfo_children():
            try:
                opciones_empaque = control.pack_info()
            except tk.TclError:
                # Si el control no utiliza pack, no necesita ser restaurado aquí.
                continue

            controles_ocultos.append((control, opciones_empaque))
            control.pack_forget()

        # Función que devuelve el módulo a su estado visual original.
        def restaurar_modulo():
            for control, opciones in controles_ocultos:
                try:
                    if control.winfo_exists():
                        control.pack(**opciones)
                except tk.TclError:
                    # Evita que un control ya destruido interrumpa la interfaz.
                    pass

            self._panel_formulario_activo = None

        # Crea un panel dentro de la pestaña activa, no un Toplevel independiente.
        ventana = FormularioIntegrado(pestaña_activa, restaurar_modulo)
        ventana.pack(fill="both", expand=True, padx=8, pady=8)
        self._panel_formulario_activo = ventana

        # Encabezado del formulario con título y botón para regresar al módulo.
        encabezado = ttk.Frame(ventana)
        encabezado.pack(fill="x", padx=22, pady=(18, 12))
        ttk.Label(encabezado, text=titulo, style="Titulo.TLabel").pack(side="left")
        ttk.Button(encabezado, text="Volver", command=ventana.destroy).pack(side="right")
        ttk.Separator(ventana, orient="horizontal").pack(fill="x", padx=22, pady=(0, 8))

        return ventana

    def _campos_formulario(self, ventana, definiciones):
        """Construye etiquetas y cajas de texto; retorna un diccionario de entradas."""
        entradas = {}
        for etiqueta, clave in definiciones:
            ttk.Label(ventana, text=etiqueta).pack(anchor="w", padx=22, pady=(9, 2))
            entrada = ttk.Entry(ventana, font=("Segoe UI", 10))
            entrada.pack(fill="x", padx=22)
            entradas[clave] = entrada
        return entradas

    def _selector_formulario(self, ventana, etiqueta, variable, opciones):
        """Añade una lista desplegable y devuelve el control creado."""
        ttk.Label(ventana, text=etiqueta).pack(anchor="w", padx=22, pady=(9, 2))
        selector = ttk.Combobox(ventana, textvariable=variable, values=opciones, state="readonly")
        selector.pack(fill="x", padx=22)
        if opciones:
            selector.current(0)
        return selector

    def _codigo_seleccionado(self, tabla):
        """Obtiene el identificador de la fila seleccionada o una cadena vacía."""
        seleccion = tabla.selection()
        if not seleccion:
            return ""
        valores = tabla.item(seleccion[0], "values")
        return str(valores[0]) if valores else ""

    def _actualizar_clientes(self):
        """Vuelve a cargar los clientes desde la lista interna del Sistema."""
        self.tabla_clientes.delete(*self.tabla_clientes.get_children())
        for cliente in self.sistema.obtener_clientes():
            self.tabla_clientes.insert("", "end", values=(
                cliente.codigo, cliente.nombre, cliente.correo, cliente.telefono))

    def _actualizar_servicios(self):
        """Actualiza el catálogo usando el método describir de cada subclase."""
        self.tabla_servicios.delete(*self.tabla_servicios.get_children())
        for servicio in self.sistema.obtener_servicios():
            tipo = type(servicio).__name__
            self.tabla_servicios.insert("", "end", values=(
                servicio.codigo, tipo, servicio.etiqueta(),
                f"{servicio.tarifa:,.2f}", "Sí" if servicio.disponible else "No"))

    def _actualizar_reservas(self):
        """Actualiza la tabla con las reservas creadas en la sesión."""
        self.tabla_reservas.delete(*self.tabla_reservas.get_children())
        for reserva in self.sistema.obtener_reservas():
            self.tabla_reservas.insert("", "end", values=(
                reserva.codigo, reserva.cliente.nombre, reserva.servicio.etiqueta(),
                str(reserva.duracion), reserva.estado,
                f"{reserva.total:,.2f}" if reserva.total is not None else "Pendiente"))

    def actualizar_todo(self):
        """Refresca tablas e indicadores después de cualquier operación."""
        self._actualizar_clientes()
        self._actualizar_servicios()
        self._actualizar_reservas()
        clientes = self.sistema.obtener_clientes()
        servicios = self.sistema.obtener_servicios()
        reservas = self.sistema.obtener_reservas()
        self.indicadores["clientes"].configure(text=str(len(clientes)))
        self.indicadores["servicios"].configure(text=str(len(servicios)))
        self.indicadores["reservas"].configure(text=str(len(reservas)))
        self.indicadores["confirmadas"].configure(
            text=str(sum(1 for reserva in reservas if reserva.estado == "CONFIRMADA")))
        self._actualizar_logs()

    def _cerrar_aplicacion(self):
        """Registra el cierre y termina el ciclo de eventos de Tkinter."""
        self.sistema.log.info("APLICACIÓN GRÁFICA CERRADA")
        self.destroy()


# ------------------------------- EJECUCIÓN --------------------------------
if __name__ == "__main__":
    # La condición evita abrir ventanas si este módulo se importa desde otro.
    aplicacion = AplicacionSoftwareFJ()
    aplicacion.mainloop()  # Mantiene activa la interfaz hasta que el usuario la cierre.
