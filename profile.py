import flet as ft




def profile_page(page: ft.Page) -> ft.View:
    async def on_back(e):
        await page.push_route("/home")
        page.update()

    app_bar = ft.AppBar(
        leading=ft.Button(
            content=ft.Icon(icon=ft.Icons.ARROW_BACK),
            on_click=on_back
        )
    )

    body = ft.Container(
        bgcolor=ft.Colors.BROWN,
        alignment=ft.Alignment.CENTER,
        height=page.height,
        width=page.width,
        content=ft.Text(
            "This is your Profile",
            expand=True,
            style=ft.TextStyle(
                color=ft.Colors.WHITE
            )
        )
    )


    return ft.View(
        route="/profile",
        appbar=app_bar,
        expand=True,
        controls=[
            body
        ]
    )
