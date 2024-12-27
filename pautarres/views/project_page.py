import reflex as rx
from pathlib import Path

from ..views.navbar import navbar
from ..views.footer import footer

def project_page(filename):
    return rx.fragment(
        rx.el.link(
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
            rel="stylesheet",
        ),
        rx.el.style(
            """
                @font-face {
                    font-family: 'LucideIcons';
                    src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
                }
            """
        ),
        rx.box(
            navbar(),
            insert_project(filename),
            footer(),
            display="flex",
            flex_direction="column",
            min_height="100vh",
            background_color="#ffffff",
            font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        )
    )



def load_markdown_file(filename):
    filepath = Path("assets/projects") / filename
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
    

def insert_project(filename):
    return rx.box(
        rx.box(
            rx.markdown(load_markdown_file(filename)),
            color="#000000"
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="1rem",
        padding_bottom="0rem",
    )
