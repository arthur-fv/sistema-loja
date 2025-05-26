from flet import Text, Colors, FontWeight, Dropdown, TextStyle, dropdown, TextField, KeyboardType, IconButton, Icons, Column, Row, MainAxisAlignment
from asyncio import run


def info_venda(on_click_add_button, nomes_vendedores: list):

    cabecalho = Text('INFORMAÇÕES DA VENDA', color=Colors.BLACK, weight=FontWeight.W_900)

    tfield_vendedor = Dropdown(
                    label='Vendedor(a)',
                    label_style=TextStyle(color=Colors.BLACK),
                    icon_enabled_color=Colors.BLACK,
                    options=[dropdown.Option(nome) for nome in nomes_vendedores],
                    color=Colors.BLACK,
                    bgcolor=Colors.GREY_400,
                    border_color=Colors.BLACK,
                    width=210,
                    autofocus=False
                    )
    tfield_valor = TextField(
                    label=Text('Valor', color=Colors.BLACK),
                    color=Colors.BLACK,
                    prefix=Text('R$ ', color=Colors.BLACK),
                    width=200,
                    border_color=Colors.BLACK,
                    cursor_color=Colors.BLACK,
                    keyboard_type=KeyboardType.NUMBER
                    )
    dpdw_forma_pag = Dropdown(
                    label='Forma de Pagamento',
                    label_style=TextStyle(color=Colors.BLACK),
                    icon_enabled_color=Colors.BLACK,
                    options=[
                        dropdown.Option('DINHEIRO'),
                        dropdown.Option('PIX'),
                        dropdown.Option('DEBITO'), 
                        dropdown.Option('CREDITO'),
                    ],
                    color=Colors.BLACK,
                    bgcolor=Colors.GREY_400,
                    border_color=Colors.BLACK,
                    width=210,
                    autofocus=False
                    )

    btn_add = IconButton(
                icon=Icons.ADD,
                icon_color=Colors.BLACK87,
                bgcolor=Colors.BLUE,
                on_click=on_click_add_button,
                width=50,
                height=50
                )

    coluna = Column(
        controls=[
            cabecalho,
            Row(
                controls=[
                    tfield_vendedor,
                    tfield_valor,
                    dpdw_forma_pag,
                    btn_add
                ],
                alignment=MainAxisAlignment.START,
                spacing=5,
            )
        ],
        height=200
    )

    return coluna
