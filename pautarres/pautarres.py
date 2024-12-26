import reflex as rx
from .list_of_projects import projects

from .views.project_page import project_page
from .views.main_page import index

app = rx.App()
app.add_page(index, route="/", title="Pau Tarrés")

for i, project in enumerate(projects):
    app.add_page(project_page(f"project{i+1}.md"), route=f"/project{i+1}", title=project["title"])
app.add_page(project_page("project1.md"), route="/project1", title="Project 1")