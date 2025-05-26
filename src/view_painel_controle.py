import flet as ft

from widgets.barra_lateral import barra_lateral

from services.Client import Client

def view_painel_controle(page: ft.Page, client: Client):
    page.title = "Painel de Controle"
    page.window.center()
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 5
    page.update()

    container_vendas = ft.Container(
        content=ft.Column(
                    controls=[
                        ft.Divider(thickness=0.01, height=5),
                        ft.Text("VENDAS", size=30, theme_style=ft.TextThemeStyle.LABEL_LARGE),
                        ft.Divider(),
                        ft.ElevatedButton(
                            text="CADASTRAR",
                            height=80, 
                            width=150, 
                            style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=12)),
                            on_click=lambda _: page.go("/cadastro_vendas")
                            ),
                        ft.ElevatedButton(
                            text="REVISAR", 
                            height=80, 
                            width=150, 
                            style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=12)),
                            on_click=lambda _ : page.go("/revisao_vendas")
                            )
                        ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=35,
        ),
        width=250
    )

    container_outras_saidas = ft.Container(
        content=ft.Column(
                controls=[
                        ft.Divider(thickness=0.01, height=5),
                        ft.Text("OUTRAS SAÍDAS", size=30, theme_style=ft.TextThemeStyle.LABEL_LARGE),
                        ft.Divider(),
                        ft.ElevatedButton(text="CADASTRAR", height=80, width=150, style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=12))),
                        ft.ElevatedButton(text="REVISAR", height=80, width=150, style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=12)))
                        ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=35,
        ),
        width=250
    )
    
    container_faruramento = ft.Container(
        content=ft.Column(
                controls=[
                        ft.Divider(thickness=0.01, height=5),
                        ft.Text("FATURAMENTO", size=30, theme_style=ft.TextThemeStyle.LABEL_LARGE),
                        ft.Divider(),
                        ft.ElevatedButton(text="VER", height=80, width=150, style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=12))),
                        ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=35,
        ),
        width=250,
    )

    layout = ft.Row(
            controls=[
                barra_lateral(page.go),
                container_vendas,
                ft.VerticalDivider(width=0, trailing_indent=900),
                container_outras_saidas,
                ft.VerticalDivider(width=0, trailing_indent=900),
                container_faruramento,
                ft.VerticalDivider(width=0, trailing_indent=900),

            ],
        expand=True
    )
    return layout
