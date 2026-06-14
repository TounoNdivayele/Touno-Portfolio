import flet as ft
import os


def get_icon(name: str):
    icons = getattr(ft, "Icons", None) or getattr(ft, "icons")
    return getattr(icons, name)


def main(page: ft.Page):
    page.clean()
    page.title = "Touno Ndivayele Portfolio"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0

    primary = "#0b3d91"
    accent = "#87CEEB"
    secondary = "#6b7280"
    card = "#111827"
    panel = accent
    text = "#ffffff"
    subtext = "#d1d5db"

    def symmetric_padding(horizontal: int, vertical: int):
        return ft.Padding(horizontal, vertical, horizontal, vertical)

    def border_all(width: int, color: str):
        side = ft.BorderSide(width=width, color=color)
        return ft.Border(top=side, right=side, bottom=side, left=side)

    async def open_route(route: str):
        await page.push_route(route)

    async def open_certificate(file_name: str):
        # Open the local PDF with the OS default application using a proper file URI
        from pathlib import Path

        path = Path(os.path.abspath(os.path.join("assets", file_name)))
        file_uri = path.as_uri()
        await ft.UrlLauncher().launch_url(
            file_uri,
            mode=ft.LaunchMode.EXTERNAL_APPLICATION,
        )

    async def open_asset(file_name: str):
        from pathlib import Path

        path = Path(os.path.abspath(os.path.join("assets", file_name)))
        file_uri = path.as_uri()
        await ft.UrlLauncher().launch_url(
            file_uri,
            mode=ft.LaunchMode.EXTERNAL_APPLICATION,
        )

    def nav_link(label: str, section_key: str):
        route = "/" if section_key == "home" else f"/{section_key}"
        return ft.Button(
            label,
            color=text,
            bgcolor=accent,
            elevation=0,
            height=36,
            on_click=lambda _: page.run_task(open_route, route),
            style=ft.ButtonStyle(
                padding=ft.Padding(8, 6, 8, 6),
                text_style=ft.TextStyle(size=13, weight=ft.FontWeight.BOLD),
            ),
        )

    def section_title(label: str, title: str):
        return ft.Column(
            spacing=8,
            controls=[
                ft.Text(label, size=14, color=primary, weight=ft.FontWeight.BOLD),
                ft.Text(title, size=42, weight=ft.FontWeight.BOLD, color=text),
            ],
        )

    def feature_card(title: str, description: str, icon_name: str):
        is_developer = title == "Developer Skills"
        return ft.Container(
            bgcolor=card,
            border_radius=12,
            padding=28,
            height=300 if is_developer else 260,
            border=border_all(1, secondary),
            expand=True,
            content=ft.Column(
                spacing=14,
                controls=[
                    ft.Icon(get_icon(icon_name), size=38, color=primary),
                    ft.Text(title, size=22, weight=ft.FontWeight.BOLD, color=text),
                    ft.Text(
                        description,
                        size=15 if is_developer else 16,
                        color=subtext,
                    ),
                ],
            ),
        )

    def evidence_card(title: str, description: str, image_src: str):
        return ft.Container(
            bgcolor=card,
            border_radius=12,
            padding=24,
            border=border_all(1, secondary),
            expand=True,
            content=ft.Column(
                spacing=16,
                controls=[
                    ft.Text(title, size=22, weight=ft.FontWeight.BOLD, color=text),
                    ft.Image(
                        src=image_src,
                        fit=ft.BoxFit.COVER,
                        height=160,
                        border_radius=12,
                    ),
                    ft.Text(description, size=15, color=subtext),
                ],
            ),
        )

    def video_card(title: str, description: str, file_name: str):
        return ft.Container(
            bgcolor=card,
            border_radius=12,
            padding=28,
            border=border_all(1, secondary),
            expand=True,
            content=ft.Column(
                spacing=14,
                controls=[
                    ft.Icon(get_icon("PLAY_CIRCLE_FILL"), size=38, color=primary),
                    ft.Text(title, size=22, weight=ft.FontWeight.BOLD, color=text),
                    ft.Text(description, size=16, color=subtext),
                    ft.Button(
                        "Watch Video",
                        bgcolor=accent,
                        color="#000000",
                        on_click=lambda _: page.run_task(open_asset, file_name),
                    ),
                ],
            ),
        )

    def certificate_card(title: str, description: str, icon_name: str, certificate_file: str):
        return ft.Container(
            bgcolor=card,
            border_radius=12,
            padding=28,
            border=border_all(1, secondary),
            expand=True,
            content=ft.Column(
                spacing=14,
                controls=[
                    ft.Icon(get_icon(icon_name), size=38, color=primary),
                    ft.Text(title, size=22, weight=ft.FontWeight.BOLD, color=text),
                    ft.Text(description, size=16, color=subtext),
                    ft.Button(
                        "View Certificate",
                        bgcolor=primary,
                        color="#ffffff",
                        on_click=lambda _: page.run_task(open_certificate, certificate_file),
                    ),
                ],
            ),
        )

    def stat_card(number: str, label: str):
        return ft.Container(
            bgcolor=card,
            padding=26,
            border_radius=12,
            border=border_all(1, secondary),
            expand=True,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(number, size=38, weight=ft.FontWeight.BOLD, color=primary),
                    ft.Text(label, size=17, color=subtext),
                ],
            ),
        )

    nav_items = [
        ("HOME", "home"),
        ("ABOUT", "about"),
        ("TIMELINE", "timeline"),
        ("MATLAB", "matlab"),
        ("BLOG", "blog"),
        ("GITHUB", "github"),
        ("CONTACT", "contact"),
    ]
    page.appbar = ft.AppBar(
        title=ft.Text("Touno Ndivayele", size=28, weight=ft.FontWeight.BOLD, color=text),
        bgcolor=accent,
        toolbar_height=76,
        actions=[nav_link(label, section_key) for label, section_key in nav_items],
        actions_padding=ft.Padding(0, 0, 28, 0),
    )

    hero_section = ft.Container(
        key="home",
        image=ft.DecorationImage(
            src="background.jpg",
            fit=ft.BoxFit.COVER,
        ),
        content=ft.Stack(
            controls=[
                ft.Container(expand=True, bgcolor="#000000", opacity=0.20),
                ft.Container(
                    padding=symmetric_padding(horizontal=50, vertical=60),
                    content=ft.ResponsiveRow(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Column(
                                col={"md": 6, "sm": 12, "xs": 12},
                                spacing=20,
                                controls=[
                                    ft.Text("WELCOME", size=18, color=secondary, weight=ft.FontWeight.BOLD),
                                    ft.Text("Touno Ndivayele", size=58, weight=ft.FontWeight.BOLD, color=text),
                                    ft.Text(
                                        "Mechanical Engineering Student",
                                        size=24,
                                        color=subtext,
                                    ),
                                    ft.Row(
                                        spacing=16,
                                        wrap=True,
                                        controls=[
                                            ft.Button(
                                                "Hire Me",
                                                bgcolor=accent,
                                                color="#000000",
                                                on_click=lambda _: page.run_task(open_route, "/contact"),
                                            ),
                                            ft.Button(
                                                "View Projects",
                                                bgcolor=accent,
                                                color="#000000",
                                                on_click=lambda _: page.run_task(open_route, "/timeline"),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            ft.Column(
                                col={"md": 6, "sm": 12, "xs": 12},
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(
                                        width=340,
                                        height=340,
                                        border_radius=170,
                                        border=border_all(5, primary),
                                        image=ft.DecorationImage(
                                            src="profile.jpg",
                                            fit=ft.BoxFit.COVER,
                                        ),
                                    )
                                ],
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )

    features = ft.Container(
        padding=symmetric_padding(horizontal=40, vertical=30),
        content=ft.ResponsiveRow(
            run_spacing=20,
            controls=[
                ft.Column(col={"md": 4, "sm": 12, "xs": 12}, controls=[feature_card(
                    "Developer Skills",
                    "• Python — automation, calculations, data analysis\n\n• MATLAB — engineering simulations and problem solving\n\n• CAD (SolidWorks / AutoCAD) — 3D design and modeling",
                    "DEVELOPER_MODE",
                )]),
                ft.Column(col={"md": 4, "sm": 12, "xs": 12}, controls=[feature_card("Creative Work", "Modern responsive UI design and animation.", "BRUSH")]),
                ft.Column(col={"md": 4, "sm": 12, "xs": 12}, controls=[feature_card("Mechanical & Metallurgical", "Mechanical and metallurgical engineering modules.", "PRECISION_MANUFACTURING")]),
            ],
        ),
        bgcolor=accent,
    )

    about_section = ft.Container(
        key="about",
        padding=symmetric_padding(horizontal=50, vertical=50),
        content=ft.ResponsiveRow(
            run_spacing=24,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    col={"md": 6, "sm": 12, "xs": 12},
                    controls=[
                        ft.Image(
                            src="about.jpg",
                            border_radius=12,
                            fit=ft.BoxFit.COVER,
                            height=360,
                            width=620,
                        )
                    ],
                ),
                ft.Column(
                    col={"md": 6, "sm": 12, "xs": 12},
                    spacing=20,
                    controls=[
                        section_title("ABOUT ME", "A Mechanical Engineering Student Building Practical Solutions"),
                        ft.Text(
                            "I am studying mechanical engineering and building practical technical projects that connect design, analysis, and problem solving.",
                            size=18,
                            color=subtext,
                        ),
                    ],
                ),
            ],
        ),
    )

    stats = ft.Container(
        padding=symmetric_padding(horizontal=40, vertical=30),
        content=ft.ResponsiveRow(
            run_spacing=20,
            controls=[
                ft.Column(col={"md": 3, "sm": 6, "xs": 12}, controls=[stat_card("20", "Projects")]),
                ft.Column(col={"md": 3, "sm": 6, "xs": 12}, controls=[stat_card("280", "Commits")]),
                ft.Column(col={"md": 3, "sm": 6, "xs": 12}, controls=[stat_card("3K", "Lines of Code")]),
                ft.Column(col={"md": 3, "sm": 6, "xs": 12}, controls=[stat_card("8", "Certificates")]),
            ],
        ),
    )

    timeline_cards = [
        ("Week 1", "I planned the portfolio structure and organized the engineering evidence into clear sections."),
        ("Week 2", "I developed the responsive Flet interface, navigation routes, and reusable card components."),
        ("Week 3", "I implemented engineering-focused content for MATLAB certificates, GitHub evidence, and technical blog notes."),
    ]
    timeline_section = ft.Container(
        key="timeline",
        padding=symmetric_padding(horizontal=50, vertical=50),
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Text("Project Timeline", size=42, weight=ft.FontWeight.BOLD, color=text),
                *[
                    ft.Container(
                        bgcolor=card,
                        padding=24,
                        border_radius=12,
                        border=border_all(1, primary),
                        content=ft.Column(
                            spacing=8,
                            controls=[
                                ft.Text(week, size=23, weight=ft.FontWeight.BOLD, color=primary),
                                ft.Text(description, color=subtext, size=16),
                            ],
                        ),
                    )
                    for week, description in timeline_cards
                ],
            ],
        ),
    )

    matlab_section = ft.Container(
        key="matlab",
        bgcolor=panel,
        padding=symmetric_padding(horizontal=50, vertical=50),
        content=ft.Column(
            spacing=24,
            controls=[
                ft.Text("MATLAB Achievement Hub", size=42, weight=ft.FontWeight.BOLD, color=text),
                ft.ResponsiveRow(
                    run_spacing=20,
                    controls=[
                        ft.Column(col={"md": 3, "sm": 6, "xs": 12}, controls=[certificate_card("MATLAB Onramp", "Certificate completed and attached as PDF evidence.", "VERIFIED", "matlab_onramp_certificate.pdf")]),
                        ft.Column(col={"md": 3, "sm": 6, "xs": 12}, controls=[certificate_card("Simulink Onramp", "Certificate completed and attached as PDF evidence.", "VERIFIED", "simulink_onramp_certificate.pdf")]),
                        ft.Column(col={"md": 3, "sm": 6, "xs": 12}, controls=[certificate_card("Machine Learning Onramp", "Certificate completed and attached as PDF evidence.", "VERIFIED", "machine_learning_onramp_certificate.pdf")]),
                        ft.Column(col={"md": 3, "sm": 6, "xs": 12}, controls=[certificate_card("Make and Manipulate Matrices", "Certificate completed and attached as PDF evidence.", "VERIFIED", "make_and_manipulate_matrices_certificate.pdf")]),
                        ft.Column(col={"md": 3, "sm": 6, "xs": 12}, controls=[certificate_card("Calculations with Vectors and Matrices", "Certificate completed and attached as PDF evidence.", "VERIFIED", "calculations_with_vectors_and_matrices_certificate.pdf")]),
                        ft.Column(col={"md": 3, "sm": 6, "xs": 12}, controls=[certificate_card("Solve Higher-Order ODEs", "Certificate completed and attached as PDF evidence.", "VERIFIED", "solve_higher_order_odes_certificate.pdf")]),
                        ft.Column(col={"md": 3, "sm": 6, "xs": 12}, controls=[certificate_card("Explore Data with MATLAB Plots", "Certificate completed and attached as PDF evidence.", "VERIFIED", "explore_data_with_matlab_plots_certificate.pdf")]),
                    ],
                ),
            ],
        ),
    )

    blog_section = ft.Container(
        key="blog",
        padding=symmetric_padding(horizontal=50, vertical=50),
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Text("Technical Blog", size=42, weight=ft.FontWeight.BOLD, color=text),
                video_card("Individual Contribution Video", "A local video demonstrating my Python work and individual contribution to the portfolio.", "portfolio video.mp4"),
                feature_card("Understanding Data Structures", "Stacks, queues, and linked lists are useful for storing sensor readings, simulation steps, and project records.", "PLAY_CIRCLE_FILL"),
                ft.Container(
                    bgcolor=card,
                    padding=28,
                    border_radius=12,
                    border=border_all(1, secondary),
                    content=ft.Column(
                        spacing=12,
                        controls=[
                            ft.Text("Embedded Video", size=30, weight=ft.FontWeight.BOLD, color=primary),
                            ft.Text("YouTube: MATLAB for Engineering Calculations", size=20, weight=ft.FontWeight.BOLD, color=text),
                            ft.Text(
                                "https://www.youtube.com/embed/T_ekAD7U-wU",
                                size=16,
                                color=subtext,
                            ),
                            ft.Text(
                                "This video supports the blog by showing how MATLAB can be used to model equations, analyze results, and explain technical workflows.",
                                size=16,
                                color=subtext,
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    bgcolor=card,
                    padding=28,
                    border_radius=12,
                    border=border_all(1, primary),
                    content=ft.Column(
                        spacing=12,
                        controls=[
                            ft.Text("Mathematical Notation", size=30, weight=ft.FontWeight.BOLD, color=primary),
                            ft.Text("Total Cost = Σ (Qi × Pi) + O", size=26, color=text),
                        ],
                    ),
                ),
            ],
        ),
    )

    github_section = ft.Container(
        key="github",
        bgcolor=panel,
        padding=symmetric_padding(horizontal=50, vertical=50),
        content=ft.Column(
            spacing=24,
            controls=[
                ft.Text("GitHub Evidence", size=42, weight=ft.FontWeight.BOLD, color=text),
                ft.Text(
                    "See GitHub commit activity and development progress from portfolio updates.",
                    size=16,
                    color=subtext,
                ),
                ft.ResponsiveRow(
                    run_spacing=20,
                    controls=[
                        ft.Column(col={"md": 3, "sm": 12, "xs": 12}, controls=[evidence_card("GitHub Commit History", "Screenshot showing a consistent history of portfolio updates, UI refinements, and feature additions.", "commit_history (1).png")]),
                        ft.Column(col={"md": 3, "sm": 12, "xs": 12}, controls=[evidence_card("GitHub Commit History", "Second screenshot showing regular contributions, bug fixes, and interface improvements.", "commit_history (2).png")]),
                        ft.Column(col={"md": 3, "sm": 12, "xs": 12}, controls=[feature_card("Pull Request Logs", "Review notes, approvals, and merged pull requests document how changes were checked before being added.", "MERGE_TYPE")]),
                        ft.Column(col={"md": 3, "sm": 12, "xs": 12}, controls=[feature_card("Impact Summary", "My work improved usability, visual design, and portfolio clarity across engineering modules and evidence cards.", "INSIGHTS")]),
                    ],
                ),
            ],
        ),
    )

    contact_section = ft.Container(
        key="contact",
        padding=symmetric_padding(horizontal=50, vertical=60),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Text("Contact Me", size=42, weight=ft.FontWeight.BOLD, color=text),
                ft.Text("Available for mechanical engineering projects and technical collaboration.", size=18, color=subtext, text_align=ft.TextAlign.CENTER),
                ft.Text("Email: tndivayele2@gmail.com", size=18, color=text, text_align=ft.TextAlign.CENTER),
                ft.Text("Cellphone: 0817207027", size=18, color=text, text_align=ft.TextAlign.CENTER),
                ft.TextField(width=500, label="Your Name", bgcolor=card, border_color=primary, color=text),
                ft.TextField(width=500, label="Your Email", bgcolor=card, border_color=primary, color=text),
                ft.TextField(width=500, min_lines=4, max_lines=6, multiline=True, label="Message", bgcolor=card, border_color=primary, color=text),
                ft.Button(
                    "Send Message",
                    bgcolor=accent,
                    color="#000000",
                ),
            ],
        ),
    )

    footer = ft.Container(
        padding=30,
        alignment=ft.Alignment.CENTER,
        content=ft.Text("(c) 2026 Touno Ndivayele Portfolio - All Rights Reserved", color=subtext),
    )

    pages = {
        "home": [hero_section, features],
        "about": [about_section],
        "timeline": [timeline_section],
        "matlab": [matlab_section],
        "blog": [blog_section],
        "github": [github_section],
        "contact": [contact_section],
    }

    def render_route(_=None):
        section = page.route.strip("/") or "home"
        controls = pages.get(section, pages["home"])
        page.controls.clear()
        page.add(ft.Column(spacing=0, controls=[*controls, footer]))
        page.update()

    page.on_route_change = render_route
    render_route()


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
