import asyncio
import flet as ft
def CreateAccountView(page: ft.Page):
    username = ft.TextField(label="Username")
    password = ft.TextField(label="Password", password=True)
    async def signup(_):
        if username.value and password.value:
            await page.push_route("/notes")
    async def go_login(_):
        await page.push_route("/")
    return ft.View(
        route="/create",
        horizontal_alignment="center",
        vertical_alignment="center",
        controls=[
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Create Account", size=25, weight="bold"),
                        username,
                        password,
                        ft.Button("Sign Up", on_click=lambda e: asyncio.create_task(signup(e))),
                        ft.TextButton("Back to Login", on_click=lambda e: asyncio.create_task(go_login(e))),
                    ], horizontal_alignment="center"),
                    padding=40,
                )
            ),
        ]
    )