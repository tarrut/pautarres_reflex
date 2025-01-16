import reflex as rx
from ..components.project_card import project_card
from ..list_of_projects import projects

def projects_section():
    """Create multiple project cards with data from the projects list."""
    return rx.box(
        *[
            project_card(
                image_alt=project["title"],
                image_src=project["image_src"],
                title=project["title"],
                description=project["description"],
                link=project["link"],
                style={
                    "transition": "transform 0.3s, box-shadow 0.3s",
                    ":hover": {
                        "transform": "scale(1.05)",
                        "box-shadow": "0 10px 20px rgba(0, 0, 0, 0.2)",
                    },
                },
            )
            for project in projects
        ],
        gap="2rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(2, minmax(0, 1fr))",
                "1024px": "repeat(3, minmax(0, 1fr))",
            }
        ),
        id="projects",
        margin_bottom="7rem",
    )