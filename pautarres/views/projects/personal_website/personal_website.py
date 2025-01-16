import reflex as rx

from ..projects_utils import markdown_style, load_markdown_file

project = "personal_website"

def personal_website():
    return rx.box(
        rx.markdown(load_markdown_file("script1.md", project), component_map=markdown_style),
        justify_content="center",
        style=rx.breakpoints(
            {
                "300px": {"max-width": "300px", "font-size": "0.5rem"},
                "350px": {"max-width": "350px", "font-size": "0.7rem"},
                "400px": {"max-width": "400px", "font-size": "0.8rem"},
                "500px": {"max-width": "500px", "font-size": "1rem"},
                "640px": {"max-width": "640px", "font-size": "1rem"},
                "768px": {"max-width": "768px", "font-size": "1rem"},
                "1024px": {"max-width": "900px", "font-size": "1rem"},
                "1280px": {"max-width": "900px", "font-size": "1rem"},
                "1536px": {"max-width": "900px", "font-size": "1rem"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="1rem",
        padding_bottom="0rem",
        color="#000000",
    )