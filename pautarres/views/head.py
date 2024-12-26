import reflex as rx

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
        ),
        id="hero",
        margin_bottom="5rem",
        text_align="left",
        height="100hv",
    )
