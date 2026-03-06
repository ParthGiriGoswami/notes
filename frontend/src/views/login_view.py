import asyncio
import flet as ft
import httpx
client = httpx.AsyncClient(base_url="http://localhost:8000")
def LoginView(page):
    email = ft.TextField(label="Email")
    password = ft.TextField(label="Password", password=True)   
    async def open_notes(_):
        response = await client.post(
            "/login",
            json={"email": email.value, "password": password.value}
        )
        data = response.json()
        if data.get("status_code") == 200:
            await page.push_route("/notes")
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
    async def open_create(_):
        await page.push_route("/create")
    return ft.View(
        route="/",  
        horizontal_alignment="center",
        vertical_alignment="center",
        controls=[
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Sign In", size=25, weight="bold"),
                        email, password,
                        ft.Button(
                            "Login",
                            on_click=lambda e: asyncio.create_task(open_notes(e)),
                        ),
                        ft.Button(
                            "Create Account",
                            on_click=lambda e: asyncio.create_task(open_create(e)),
                        ),
                    ], horizontal_alignment="center"),
                    padding=40,
                )
            )
        ],
    )