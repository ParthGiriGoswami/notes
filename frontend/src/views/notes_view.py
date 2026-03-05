import asyncio
import flet as ft
def NotesView(page: ft.Page):
    def notes_card():
        title = ft.TextField(
            hint_text="Title",
            border=ft.InputBorder.OUTLINE,
            width=1400,
        )
        description = ft.TextField(
            hint_text="Write your note here...",
            multiline=True,
            expand=True,
            min_lines=20,
            border=ft.InputBorder.OUTLINE,
            text_align=ft.TextAlign.LEFT,
            text_vertical_align=ft.VerticalAlignment.START,
        )
        return ft.Card(
            expand=True,
            content=ft.Container(
                padding=30,
                content=ft.Column(
                    [
                        title,
                        description,
                        ft.Row(
                            [
                                ft.IconButton(
                                    ft.Icons.DELETE_OUTLINE,
                                    icon_color="red400",
                                ),
                                ft.IconButton(
                                    ft.Icons.SAVE_OUTLINED,
                                    icon_color="blue400",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ],
                    tight=True,
                ),
            ),
        )
    def history_card():
        notes = [f"Note {i}" for i in range(1, 11)]
        list_view = ft.ListView(
            expand=True,
            spacing=10,
            controls=[
                ft.ListTile(
                    title=ft.Text(note),
                    leading=ft.Icon(ft.Icons.DESCRIPTION_OUTLINED),
                )
                for note in notes
            ],
        )
        return ft.Card(
            expand=True,
            content=ft.Container(
                padding=30,
                content=list_view,
            ),
        )
    card_container = ft.Container(
        expand=True,
        padding=20,
        content=notes_card(),
    )
    async def open_drawer(e):
        await page.show_drawer()
    async def drawer_change(e: ft.Event[ft.NavigationDrawer]):
        index = e.control.selected_index
        if index == 0:
            card_container.content = notes_card()
        elif index == 1:
            card_container.content = history_card()
        page.update()
        await page.close_drawer()
    drawer = ft.NavigationDrawer(
        on_change=drawer_change,
        controls=[
            ft.Container(height=10),
            ft.NavigationDrawerDestination(
                label="New Note",
                icon=ft.Icons.NOTE_ADD_OUTLINED,
                selected_icon=ft.Icons.NOTE_ADD,
            ),
            ft.NavigationDrawerDestination(
                label="History",
                icon=ft.Icons.HISTORY_OUTLINED,
                selected_icon=ft.Icons.HISTORY,
            ),
        ],
    )
    menu_button = ft.IconButton(
        ft.Icons.MENU,
        on_click=open_drawer,
    )
    logout_button = ft.IconButton(
        ft.Icons.EXIT_TO_APP,
        on_click=lambda e: asyncio.create_task(page.push_route("/")),
    )
    header = ft.Row(
        [
            menu_button,
            ft.Container(expand=True),
            logout_button,
        ],
    )
    layout = ft.Column(
        [
            header,
            card_container,
        ],
        expand=True,
    )
    return ft.View(
        route="/notes",
        drawer=drawer,
        controls=[layout],
        padding=0,
        spacing=0,
    )