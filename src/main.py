import flet as ft

from routes import ROUTES

def main(page: ft.Page):

    def route_change(route: ft.RouteChangeEvent):
        page.views.clear()
        new = ROUTES[route.route]
        page.views.append(ft.View(controls=[new(page)]))
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
