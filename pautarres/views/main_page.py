import reflex as rx

from ..components.texts import section_heading
from ..components.contact_button import contact_button

from ..views.navbar import navbar
from ..views.footer import footer
from ..views.projects_section import projects_section

def contact_section():
    return rx.box(
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

def main_content():
    """Create the main content of the portfolio including hero, about, projects, and contact sections."""
    return rx.box(
        head(),
        projects_section(),
        contact_section(),
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

def head():
    """Create the hero section with name and title."""
    return rx.box(
        rx.heading(
            "Pau Tarrés",
            font_weight="700",
            margin_bottom="1rem",
            font_size="3rem",
            line_height="1",
            color="#111827",
            as_="h1",
        ),
        rx.text(
            "Aerospace Engineer & Tech Enthusiast",
            font_size="1.5rem",
            line_height="2rem",
            color="#4B5563",
            margin_bottom="6rem",
        ),
        rx.markdown(
            "Welcome to my **personal website**!",
            font_size="1.2rem",
            line_height="1.7rem",
            max_width="45rem",
        ),
        rx.markdown("Here you will find information about **projects** I have worked on as well as my **contact information**. " +
            "Feel free to take a look around and get in touch if you have any questions!",
            font_size="1.2rem",
            line_height="1.7rem",
            max_width="45rem",
        ),
        id="hero",
        margin_bottom="5rem",
        text_align="left",
        height="100hv",
        color="#000000",
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
