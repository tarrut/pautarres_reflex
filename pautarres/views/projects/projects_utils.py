import reflex as rx
from pathlib import Path
import pandas as pd


def load_markdown_file(filename, project):
    filepath = Path.cwd() / "pautarres/views/projects" / project / "markdown" / filename
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def load_csv_file(filename, project):
    filepath = Path.cwd() / "pautarres/views/projects" / project / "tables" / filename
    return pd.read_csv(filepath)


markdown_style = {
    "h1": lambda text: rx.heading(
        text,
        border_bottom="2px solid black",
        margin_top="2rem",
        padding_bottom="0.5rem",
        margin_bottom="2rem",
    ),
    "h2": lambda text: rx.heading(
        text,
        border_bottom="1px solid black",
        margin_top="2rem",
        padding_bottom="0.5rem"
    ),
    "h3": lambda text: rx.heading(
        text,
        margin_top="2rem",
        size="5"
    ),
}