import flet as ft




def settings_page(page: ft.Page) -> ft.View:

    async def on_back(e):
            await page.push_route("/home")
            page.update()

    app_bar = ft.AppBar(
        leading=ft.Button(
            content=ft.Row(
                controls=[
                    ft.Icon(icon=ft.Icons.ARROW_BACK),
                    ft.Text(
                        value="Back"
                    )
                ]
            ),
            on_click=on_back
        )
    )

    body = ft.Container(
        bgcolor=ft.Colors.BLUE,
        alignment=ft.Alignment.CENTER,
        height=page.height,
        width=page.width,
        content=ft.Text(
            "These are your settings",
            expand=True,
            style=ft.TextStyle(
                color=ft.Colors.WHITE
            )
        )
    )


    return ft.View(
        route="/settings",
        appbar=app_bar,
        expand=True,
        controls=[
            body
        ]
    )
