import reflex as rx


def navbar():
    """Create the main navigation section of the portfolio."""
    return rx.box(
        rx.box(
            rx.list(
                create_nav_item(href="/", text="Home"),
                create_nav_item(
                    href="/#projects", text="Projects"
                ),
                create_nav_item(
                    href="/#contact", text="Contact"
                ),
                display="flex",
                justify_content="flex-end",
                column_gap="1.5rem",
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
            padding_bottom="1rem",
            position= "sticky",
            top= "0",
        ),
        background_color="#ffffff",
    )


def create_nav_link(href, text):
    """Create a navigation link with hover effect."""
    return rx.el.a(
        text,
        href=href,
        _hover={"color": "#9CA3AF"},
        color="#000000",
        text_decoration="bold",
    )


def create_nav_item(href, text):
    """Create a list item containing a navigation link."""
    return rx.el.li(create_nav_link(href=href, text=text))
