import reflex as rx

def contact_button():
    """Create a 'Contact Me' button with hover effect."""
    return rx.el.a(
        "Contact Me",
        href="mailto:tarres.pau@gmail.com",
        background_color="#000000",
        transition_duration="300ms",
        _hover={"background-color": "#9CA3AF"},
        display="inline-block",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="9999px",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )
