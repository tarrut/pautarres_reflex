import reflex as rx

from ..projects_utils import markdown_style, load_markdown_file

project = "mcp_weather_tool"

def mcp_weather_tool():
    return rx.box(
        rx.markdown(load_markdown_file("script1.md", project), component_map=markdown_style),
        rx.image(
            src="../images/mcp_weather_tool/weather_api.png",
            alt="Weather API Diagram",
            style={"width": "80%", "display": "block", "margin": "auto"}
        ),
        rx.markdown(load_markdown_file("script2.md", project), component_map=markdown_style),
        rx.image(
            src="../images/mcp_weather_tool/mcp.png",
            alt="MCP Diagram",
            style={"width": "80%", "display": "block", "margin": "auto"}
        ),
        rx.markdown(load_markdown_file("script3.md", project), component_map=markdown_style),
        rx.image(
            src="../images/mcp_weather_tool/tools.png",
            alt="Claude's Tools",
            style={"width": "80%", "display": "block", "margin": "auto"}
        ),
        rx.markdown(load_markdown_file("script4.md", project), component_map=markdown_style),
        rx.image(
            src="../images/mcp_weather_tool/prompt.png",
            alt="Prompt",
            style={"width": "80%", "display": "block", "margin": "auto"}
        ),
        rx.markdown(load_markdown_file("script5.md", project), component_map=markdown_style),
        rx.image(
            src="../images/mcp_weather_tool/permissions.png",
            alt="Permissions",
            style={"width": "80%", "display": "block", "margin": "auto"}
        ),
        rx.markdown(load_markdown_file("script6.md", project), component_map=markdown_style),
        rx.image(
            src="../images/mcp_weather_tool/answer.png",
            alt="Claude's Answer",
            style={"width": "80%", "display": "block", "margin": "auto"}
        ),
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