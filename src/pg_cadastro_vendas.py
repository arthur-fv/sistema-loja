import flet as ft

from widgets.barra_lateral      import barra_lateral
from widgets.info_venda         import info_venda
from widgets.tabela_vendas      import tabela_vendas

from widgets.buttons.btn_check  import btn_check
from widgets.buttons.btn_delete import btn_delete

from services.func_cadastrar_vendas_confirmadas import func_cadastrar_vendas_confirmadas

def pg_cadastro_vendas(page: ft.Page):
    page.title = 'Cadastrado Vendas'
    page.window.center()
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 5
    page.update()
    
    def on_click_DELETE(e):
        for i in range(len(tabela.controls[0].rows)-1, -1, -1):
            if tabela.controls[0].rows[i].cells[3].content.value:
                tabela.controls[0].rows.pop(i)
        tabela.controls[0].columns[3] = ft.DataColumn(ft.Text('', width=40))
        tabela.update()

    def on_change_DELETE_visible(e):
        if e.control.value:
            tabela.controls[0].columns[3] = ft.DataColumn(btn_delete(on_click_func=on_click_DELETE))
        else:
            selected = False
            for row in tabela.controls[0].rows:
                 selected = (selected or row.cells[3].content.value)
                 if selected: break
            if not selected:
                tabela.controls[0].columns[3] = ft.DataColumn(ft.Text('', width=40))
        tabela.update()

    def on_click_add_button(e):
        nome_vendedor = e.control.parent.controls[0].value
        valor_venda = float(e.control.parent.controls[1].value)
        met_pag = e.control.parent.controls[2].value
        e.control.parent.controls[0].value = '' 
        e.control.parent.controls[1].value = ''
        e.control.parent.controls[2].value = ''
        informacoes.update()
        if bool(valor_venda) and bool(nome_vendedor):
            tmn_txt, cor_txt = 20, ft.Colors.BLACK
            tabela.controls[0].rows.append(ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text(nome_vendedor, size=tmn_txt, color=cor_txt, width=105)),
                                            ft.DataCell(ft.Text(valor_venda, size=tmn_txt, color=cor_txt, width=100)),
                                            ft.DataCell(ft.Text(met_pag, size=tmn_txt, color=cor_txt, width=105)),
                                            ft.DataCell(ft.Checkbox(value=False, on_change=on_change_DELETE_visible, width=40))
                                        ]
                                    )
                                )
        tabela.update()

    async def on_click_confirm_button(e):
        conteudo_linhas = []
        for j in range(len(tabela.controls[0].rows)):
            conteudo_linhas.append([tabela.controls[0].rows[j].cells[i].content.value for i in range(3)])
        mensagem = await func_cadastrar_vendas_confirmadas(conteudo_linhas)
        print(mensagem) #DECIDA O QUE VOCÊ VAI FAZER COM ESSA BOMBA

    informacoes = info_venda(on_click_add_button)
    tabela = tabela_vendas()
    btn_cadastrar_vendas = btn_check(100, on_click_confirm_button)

    coluna_esquerda = ft.Column(
        controls=[
            informacoes,
            ft.Row(
                controls=[
                    ft.Column(
                        controls=[tabela]
                    ),
                    ft.Column(
                        controls=[]
                    )
                ]
            )
            ],
        width=750,
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        horizontal_alignment=ft.CrossAxisAlignment.START
        )
    
    coluna_direita = ft.Column(
        controls=[btn_cadastrar_vendas],
        width=600,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    base = ft.Container(
        content=ft.Row(
            controls=[
                coluna_esquerda,
                coluna_direita
            ],
            vertical_alignment=ft.CrossAxisAlignment.END
        ),
        bgcolor=ft.Colors.GREY_400,
        width=1500,
        padding=100,
    )
    
    layout = ft.Row(
        controls=[
            barra_lateral(page.go, '/painel_controle'),
            ft.Column(
                controls=[
                    base
                ],
            ),
        ],
        expand=True,
        spacing=5,
    )
    return layout
