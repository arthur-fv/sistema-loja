import flet as ft
import asyncio

from widgets.barra_lateral import barra_lateral

from services.Client import Client

async def view_revisao_vendas(page: ft.Page, client: Client):
    page.window.center()
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 5
    page.update()

    # processar vendas concluidas
    async def linhas_tabela(tabela: ft.DataTable):
        pass

    tabela = ft.DataTable(columns=[
                            ft.DataColumn(ft.Text("Vendedor(a)",size=20, color=ft.Colors.BLACK, width=150)),
                            ft.DataColumn(ft.Text("Valor", size=20, color=ft.Colors.BLACK, width=100)),
                            ft.DataColumn(ft.Text("Forma de Pagamento", size=20, color=ft.Colors.BLACK, width=200)),
                            ft.DataColumn(ft.Text("Data", size=20, color=ft.Colors.BLACK, width=150)),
                            ft.DataColumn(ft.Text("Horario", size=20, color=ft.Colors.BLACK, width=150)),
                            ft.DataColumn(ft.Text("", size=20, color=ft.Colors.BLACK, width=100))
                        ],
                        data_row_color=ft.Colors.GREY,
                        width=1100,
                        height=600,
                        expand=True,
                        border=ft.Border()
                        )
    
    page.add(tabela)

    asyncio.create_task(linhas_tabela(tabela))

    coluna = ft.Column(
        controls=[tabela],
        scroll=ft.ScrollMode.AUTO,
        expand=1
    )

    base = ft.Container(
        content=ft.Row(
            controls=[
                coluna
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor=ft.Colors.GREY_400,
        width=1500,
        padding=100,
    )

    layout = ft.Row(
        controls=[
            barra_lateral(page.go, "/painel_controle"),
            base
        ],
        expand=True
    )
    
    return layout
