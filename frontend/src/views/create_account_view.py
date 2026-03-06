import asyncio, httpx
import flet as ft
client = httpx.AsyncClient(base_url="http://localhost:8000")
def CreateAccountView(page: ft.Page):
    username = ft.TextField(label="Email")
    password = ft.TextField(label="Password", password=True)
    async def go_notes(e):
        page.pop_dialog()
        await page.push_route("/notes")
    async def signup(_):
        response = await client.post(
            "/create_user",
            json={"email": username.value, "password": password.value}
        )
        data = response.json()
        if data.get("status_code") == 200:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Success"),
                content=ft.Text(data.get("message")),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: asyncio.create_task(go_notes(e)))
                ]
            )
        elif data.get("status_code") == 400:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text(data.get("message")),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: page.pop_dialog())
                ]
            )
        page.show_dialog(page.dialog)
        page.update()
    async def go_login(_):
        await page.push_route("/")
    return ft.View(
        route="/create",
        horizontal_alignment="center",
        vertical_alignment="center",
        controls=[
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Create Account", size=25, weight="bold"),
                            username,
                            password,
                            ft.Button(
                                "Sign Up",
                                on_click=lambda e: asyncio.create_task(signup(e))
                            ),
                            ft.TextButton(
                                "Back to Login",
                                on_click=lambda e: asyncio.create_task(go_login(e))
                            ),
                        ],
                        horizontal_alignment="center"
                    ),
                    padding=40,
                )
            ),
        ]
    )