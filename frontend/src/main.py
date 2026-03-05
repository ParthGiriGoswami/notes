import asyncio
import flet as ft
from views.login_view import LoginView
from views.notes_view import NotesView
from views.create_account_view import CreateAccountView
def main(page: ft.Page):
    page.title = "Notes App"
    def route_change(e):
        route = e.route or "/"
        page.views.clear()
        if route == "/":
            page.views.append(LoginView(page))
        elif route == "/create":
            page.views.append(CreateAccountView(page))
        elif route in ("/notes"):
            page.views.append(NotesView(page))
        page.update()
    async def view_pop(e):
        if e.view is not None and page.views:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)
    page.views.append(LoginView(page))
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    asyncio.create_task(page.push_route(page.route or "/"))
if __name__ == "__main__":
    ft.run(main)