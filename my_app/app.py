import flet as ft


def main(page: ft.Page) -> None:
    status_Text = ft.Text("The button has not been pressed yet")
    n_clicks = 0

    def handle_click(*args) -> None:
        nonlocal n_clicks
        n_clicks += 1
        status_Text.value = f"The button has been pressed {n_clicks} times"
        status_Text.update()

    col = ft.Column(
        [
            ft.Text("Hello world"),
            ft.Text(),
            ft.Text(),
            ft.Button("Press me", on_click=handle_click),
            ft.Text(),
            status_Text,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(
        ft.Container(
            ft.Container(col),
            expand=1,
            alignment=ft.Alignment.CENTER,
        )
    )
