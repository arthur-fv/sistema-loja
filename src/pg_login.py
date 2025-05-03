import flet as ft

from services.func_login_usuario import func_login_usuario
from widgets.buttons.btn_check import btn_check
from widgets.buttons.btn_close import btn_close

from asyncio import sleep

def pg_login(page: ft.Page):
    page.route = '/login'
    page.title = 'Login'
    page.window.width = 600
    page.window.height = 500
    page.window.center()
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 5
    page.update()

    async def on_click_btn_login(e):
        btn_entrar.visible = False
        anel_carregamento.visible = True # faz o botão ser 'trocado' pelo anel de carregamento
        page.update()
        if await func_login_usuario(usuario_input.value.strip(), senha_input.value.strip()):
            anel_carregamento.visible = False
            btn_confimado.visible = True # logou
            page.go('/painel_controle')
        else:
            btn_cancelado.visible = True # log errado
            anel_carregamento.visible = False
            page.update()
            await sleep(1.5)
            btn_cancelado.visible = False
            btn_entrar.visible = True
        page.update()

    usuario_input = ft.TextField(label='Usuário', width=300)
    senha_input = ft.TextField(label='Senha', password=True, width=300)

    btn_entrar = ft.ElevatedButton("Entrar", on_click=on_click_btn_login)
    anel_carregamento = ft.ProgressRing(visible=False)
    btn_confimado = btn_check(size=40, is_visible=False, is_disabled=True)
    btn_cancelado = btn_close(size=40, v=False)

    layout = ft.Row(
        controls=[ft.Column(
                    controls=[
                        ft.Text("LOGIN", size=20),
                        usuario_input,
                        senha_input,
                        btn_entrar,
                        anel_carregamento,
                        btn_confimado,
                        btn_cancelado
                        ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                    )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )
    return layout
