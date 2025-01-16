import reflex as rx

from ..projects_utils import markdown_style, load_markdown_file, load_csv_file

project = "nonlagrangian_finite_elements"

def nonlagrangian_finite_elements():
    return rx.box(
        rx.markdown(load_markdown_file("script1.md", project), component_map=markdown_style),
        rx.unordered_list(
            rx.list_item("Lagrange elements:"),
            rx.hstack(
                rx.image(src="../images/nonlagrangian_finite_elements/x_k1.jpg", alt="P1 Lagrange", style={"width": "33%", "display": "block", "margin": "auto"}),
                rx.image(src="../images/nonlagrangian_finite_elements/x2_k2.jpg", alt="P2 Lagrange", style={"width": "33%", "display": "block", "margin": "auto"}),
                rx.image(src="../images/nonlagrangian_finite_elements/x3_k3.jpg", alt="P3 Lagrange", style={"width": "33%", "display": "block", "margin": "auto"}),
            ),
            rx.list_item("Raviart-Thomas elements:"),
            rx.image(src="../images/nonlagrangian_finite_elements/x-y_1.jpg", alt="RT0", style={"width": "60%", "display": "block", "margin": "auto"}),
            rx.list_item("Nédélec elements:"),
            rx.image(src="../images/nonlagrangian_finite_elements/N_-y_x_1.jpg", alt="N0", style={"width": "60%", "display": "block", "margin": "auto"}),
        ),
        rx.markdown(load_markdown_file("script2.md", project), component_map=markdown_style),
        rx.unordered_list(
            rx.list_item(rx.markdown("$P1$ solution:")),
            rx.image(src="../images/nonlagrangian_finite_elements/k1_test1.jpg", alt="P1 solution", style={"width": "100%", "display": "block", "margin": "auto"}),
            rx.list_item(rx.markdown("$P2$ solution:")),
            rx.image(src="../images/nonlagrangian_finite_elements/k2_test1.jpg", alt="P2 solution", style={"width": "100%", "display": "block", "margin": "auto"}),
        ),
        rx.markdown(load_markdown_file("script3.md", project), component_map=markdown_style),
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