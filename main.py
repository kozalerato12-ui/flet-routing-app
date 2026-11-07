import flet as ft
from pages.home import home_page
from pages.error import error_page
from pages.profile import profile_page
from pages.settings import settings_page


def main(page: ft.Page):

    def on_route_change():
        page.views.clear()

        if page.route == "/":
            page.views.append(home_page(page))
        elif page.route == "/home":
            page.views.append(home_page(page))
        elif page.route == "/settings":
            page.views.append(settings_page(page))
        elif page.route == "/profile":
            page.views.append(profile_page(page))
        else:
            page.views.append(error_page(page))

        page.update()


    page.on_route_change=on_route_change

    on_route_change()

if __name__ == "__main__":
    ft.run(main)
