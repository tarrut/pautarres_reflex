import reflex as rx

def footer():
    """Create the footer with copyright information and social links."""
    return rx.box(
        rx.flex(
            rx.text("© 2025 Pau Tarrés. All rights reserved."),
            rx.flex(
                create_social_link(
                    alt_text="GitHub", icon_tag="github", link="https://github.com/tarrut"
                ),
                create_social_link(
                    alt_text="LinkedIn", icon_tag="linkedin", link="https://www.linkedin.com/in/pau-tarres/"
                ),
                display="flex",
                column_gap="1rem",
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
            display="flex",
            align_items="center",
            justify_content="space-between",
            margin_left="auto",
            margin_right="auto",
            padding_left="1.5rem",
            padding_right="1.5rem",
            color="#000000",
        ),
        background_color="#ffffff",
        padding_top="2rem",
        padding_bottom="2rem",
    )


def create_social_icon(alt_text, icon_tag):
    """Create a social media icon with specific dimensions."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="1.5rem",
        width="1.5rem",
    )


def create_social_link(alt_text, icon_tag, link):
    """Create a social media link with an icon."""
    return rx.el.a(
        create_social_icon(
            alt_text=alt_text, icon_tag=icon_tag
        ),
        href=link,
        _hover={"color": "#9CA3AF"},
    )

