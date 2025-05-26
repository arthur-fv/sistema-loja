import flet as ft

from routes import ROUTES

from services.Client import Client

async def main(page: ft.Page):

    pool = await Client.create_pool(min_sixe=1, max_sixe=10)

    def route_change(route: ft.RouteChangeEvent):
        page.views.clear()
        new = ROUTES[route.route]
        page.views.append(ft.View(controls=[new(page, pool)]))
        page.update()
    
    def view_pop(view):
        print(type(view))
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    page.on_view_pop = view_pop
    page.on_route_change = route_change
    
    page.go('/painel_controle')

ft.app(target=main, view=ft.AppView.FLET_APP)
