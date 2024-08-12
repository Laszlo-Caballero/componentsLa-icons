import flet as ft
from Parser import Parser
from SaveComponent import SaveComponent, SaveComponentMain

class MiAplicacion:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.width = 720
        self.page.window.height = 720
        self.page.title = "Aplicación Flet con Clases"
        self.page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        self.crear_interfaz()

    def crear_interfaz(self):
        self.txtNombre = ft.TextField(width=200, height=50, 
                                      bgcolor=ft.colors.WHITE, 
                                      color=ft.colors.BLACK)
        self.codigo = ft.TextField(multiline=True, expand=True)
        self.boton = ft.FilledButton(text="Agregar", width=200, height=40, on_click=self.Guardar)
        
        self.dialog_modal = ft.AlertDialog(modal=True, 
                                           title=ft.Text("Exito"),
                                           content=ft.Text("Se creo el Icono, dale formato despues de cerrar esta modal ;)"),
                                           actions=[
                                               ft.TextButton("Cerrar", on_click=self.cerrar_Modal)
                                           ])
        
        
        self.superior = ft.Container(
            height=150, 
            content=ft.Column([
                ft.Container(
                    content=ft.Text(
                        "Nombre del svg",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                    alignment=ft.alignment.center,
                    expand=True
                ),
                ft.Row([
                    ft.Text("Nombre: "),
                    self.txtNombre,
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Container(
                    content=ft.Text(
                        "El nombre del Componente tiene que estar en Camel Case",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                    alignment=ft.alignment.center,
                    expand=True)
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
        )
        
        self.medio = ft.Container(
            margin=ft.margin.only(top=5), 
            content=self.codigo, expand=True
        )
        
        self.abajo = ft.Container(
            margin=ft.margin.only(top=5), 
            content=ft.Row(
                [self.boton],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            )
        )
        
        self.page.add(ft.Column([
            self.superior,
            self.medio,
            self.abajo
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True
        ))
        

    
    def Guardar(self, e):
        nombre_value = str(self.txtNombre.value)
        codigo_value = str(self.codigo.value)
        codigo_parseado = Parser(codigo_value)
        SaveComponent(nombre_value, codigo_parseado)
        SaveComponentMain(nombre_value)
        self.page.open(self.dialog_modal)
        
    def cerrar_Modal(self, e):
        self.page.close(self.dialog_modal)
        
def main(page: ft.Page):
    app = MiAplicacion(page)

ft.app(target=main)
