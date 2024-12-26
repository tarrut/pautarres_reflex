import reflex as rx


ACCENT_COLOR = "#9CA3AF"


def paragraph(text):
    """Create a paragraph with specific text color."""
    return rx.text(text, color="#374151")


def subheading(text, link=""):
    """Create a subheading (h3) with specific styling and hover effect."""
    base_style = {
        "font_weight": "600",
        "margin_bottom": "0.5rem",
        "color": "#111827",  # Default color
        "font_size": "1.25rem",
        "line_height": "1.75rem",
    }
    
    hover_style = {"_hover": {
        "color": ACCENT_COLOR,
        "text_decoration": "none",
        }}  # Change color on hover (e.g., to blue)

    if link != "":
        return rx.link(
            rx.heading(
                text,
                as_="h3",
                style={**base_style, **hover_style},  # Combine base style with hover style
            ),
            href=link,
            style={"text_decoration": "none"},
        )
    
    return rx.heading(
        text,
        as_="h3",
        style={**base_style, **hover_style},  # Combine base style with hover style
    )


def section_heading(text):
    """Create a section heading (h2) with specific styling."""
    return rx.heading(
        text,
        font_weight="700",
        margin_bottom="1.5rem",
        font_size="1.875rem",
        line_height="2.25rem",
        color="#111827",
        as_="h2",
    )
