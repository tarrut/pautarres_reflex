import reflex as rx
from .texts import paragraph, subheading


def create_project_description(title, description, link):
    """Create a box containing a project's title and description."""
    return rx.box(
        subheading(text=title, link=link),
        paragraph(text=description),
        padding="1.5rem",
    )


def create_project_image(alt_text, image_src, link):
    """Create an image for a project with specific dimensions and styling."""
    return rx.link(
        rx.image(
            src=image_src,
            alt=alt_text,
            height="12rem",
            object_fit="cover",
            width="100%",
        ),
        href=link,
    )


def project_card(
    image_alt, image_src, title, description, link, style=None
):
    """Create a complete project card with image, title, and description."""
    return rx.box(
        create_project_image(
            alt_text=image_alt, image_src=image_src, link=link
        ),
        create_project_description(
            title=title, description=description, link=link
        ),
        background_color="#ffffff",
        overflow="hidden",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        **(style or {}),
    )
