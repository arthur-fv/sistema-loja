from flet import Container, Column, IconButton, Icons, Colors, ElevatedButton, CrossAxisAlignment


def barra_lateral(route_func, route = '/login'):
    barra = Container(
        content=Column(
            controls=[
            IconButton(icon=Icons.ACCOUNT_CIRCLE, icon_size=50, icon_color=Colors.GREY),
            Container(expand=True),
            ElevatedButton(text="Voltar", color=Colors.GREY, icon=Icons.ARROW_BACK, width=90, on_click=lambda _: route_func(route)),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER
        ),
        width=100,
        bgcolor=Colors.BLACK54,
    )
    return barra
