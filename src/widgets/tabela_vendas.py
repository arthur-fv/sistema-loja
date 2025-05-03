from flet import Column, DataTable, DataColumn, Text, Colors, ScrollMode


def tabela_vendas():
    tabela = Column(
        controls=[
            DataTable(
                columns=[
                    DataColumn(Text('Vendedor(a)', size=20, color=Colors.BLACK, width=120)),
                    DataColumn(Text('Valor',size=20, color=Colors.BLACK, width=100)),
                    DataColumn(Text('Forma de Pagamento', size=20, color=Colors.BLACK, width=200)),
                    DataColumn(Text('', width=40))
                ],
                data_row_color=Colors.GREY,
                width=660,
            ),
        ],
        height=400,
        scroll=ScrollMode.AUTO,
    )
    return tabela
