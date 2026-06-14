import flet as ft
import os
from pathlib import Path

PDF_FILE = "matlab_onramp_certificate.pdf"

async def main(page: ft.Page):
    page.title = "Flet PDF Test"
    page.add(
        ft.Column(
            spacing=20,
            controls=[
                ft.Text("Click the button to open the PDF via Flet."),
                ft.ElevatedButton(
                    "Open PDF",
                    on_click=lambda _: page.run_task(open_pdf),
                ),
            ],
        )
    )

async def open_pdf():
    path = Path(os.path.abspath(os.path.join("assets", PDF_FILE)))
    await ft.UrlLauncher().launch_url(
        path.as_uri(),
        mode=ft.LaunchMode.EXTERNAL_APPLICATION,
    )

if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
