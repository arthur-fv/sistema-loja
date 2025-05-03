import flet as ft
import asyncio
import asyncpg

from widgets.barra_lateral import barra_lateral

async def pg_revisao_vendas(page: ft.Page):
    page.window.center()
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 5
    page.update()


    async def linhas_tabela(t: ft.DataTable):
        try:
            conn = await asyncpg.connect(
                host=     "morally-welcoming-bowerbird.data-1.use1.tembo.io",
                database= "postgres",
                user=     "postgres",
                password= "ChvxLwgmkIJcT81G"
            )
            print('passei')

            # Executar a consulta (você pode limitar o número de resultados por vez)
            async with conn.transaction():
                async for row in conn.cursor("SELECT * FROM vendas WHERE data_venda = '2025-02-01' AND id >= 1 ORDER BY id LIMIT 50"):
                    t.rows.append(ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(row['nome_vendedor'])),
                            ft.DataCell(ft.Text(row['valor_venda'])),
                            ft.DataCell(ft.Text(row['metodo_pagamento'])),
                            ft.DataCell(ft.Text(row['data_venda'])),
                            ft.DataCell(ft.Text(row['horario_venda'])),
                            ft.DataCell(ft.Text('')),
                        ]
                    ))
                    tabela.update()  # Atualiza a interface
                    await asyncio.sleep(0.1)  # Simula um delay para visualizar o carregamento
            await conn.close()
        except Exception as e:
            print(e)

    tabela = ft.DataTable(columns=[
                            ft.DataColumn(ft.Text('Vendedor(a)',size=20, color=ft.Colors.BLACK, width=150)),
                            ft.DataColumn(ft.Text('Valor', size=20, color=ft.Colors.BLACK, width=100)),
                            ft.DataColumn(ft.Text('Forma de Pagamento', size=20, color=ft.Colors.BLACK, width=200)),
                            ft.DataColumn(ft.Text('Data', size=20, color=ft.Colors.BLACK, width=150)),
                            ft.DataColumn(ft.Text('Horario', size=20, color=ft.Colors.BLACK, width=150)),
                            ft.DataColumn(ft.Text('', size=20, color=ft.Colors.BLACK, width=100))
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
            barra_lateral(page.go, '/painel_controle'),
            base
        ],
        expand=True
    )
    

    return layout
