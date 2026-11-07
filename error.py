import flet as ft




def error_page(page: ft.Page) -> ft.View:

    
    body = ft.Container(
        bgcolor=ft.Colors.RED,
        alignment=ft.Alignment.CENTER,
        content=ft.Text(
            "Page Not Found",
            expand=True,
            style=ft.TextStyle(
                color=ft.Colors.WHITE
            )
        )
    )


    return ft.View(
        route="/error_404",
        controls=[
            body
        ]
    )
