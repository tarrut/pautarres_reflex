import reflex as rx

from ..components.texts import section_heading
from ..components.contact_button import contact_button

from ..views.navbar import navbar
from ..views.footer import footer
from ..views.projects_section import projects_section
from ..views.head import head

def main_content():
    """Create the main content of the portfolio including hero, about, projects, and contact sections."""
    return rx.box(
        head(),
        projects_section(),
        rx.box(
            section_heading(text="Get in Touch"),
            rx.text(
                "Interested in working together? Feel free to reach out!",
                margin_bottom="1rem",
                color="#374151",
            ),
            contact_button(),
            id="contact",
            text_align="center",
            margin_bottom="5rem",
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
        padding_top="3rem",
        padding_bottom="0rem",
    )


def index():
    """Render the complete portfolio with necessary styles and layout."""
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
            main_content(),
            footer(),
            background_color="#ffffff",
            font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        ),
    )
