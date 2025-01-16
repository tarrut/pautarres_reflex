import reflex as rx
from pathlib import Path

from ..navbar import navbar
from ..footer import footer

def project_page(content):
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
            content,
            footer(),
            display="flex",
            flex_direction="column",
            min_height="100vh",
            background_color="#ffffff",
            font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        ),
        background_color="#ffffff",
    )