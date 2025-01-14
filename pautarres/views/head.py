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
    )
