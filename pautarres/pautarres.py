import reflex as rx
from .list_of_projects import projects

from .views.projects.project_pages import project_page
from .views.main_page import index

from .views.projects.airline_optimization.airline_optimization import airline_optimization
from .views.projects.john_draim_constellation.john_draim_constellation import john_draim_constellation
from .views.projects.personal_website.personal_website import personal_website
from .views.projects.nonlagrangian_finite_elements.nonlagrangian_finite_elements import nonlagrangian_finite_elements

app = rx.App()
app.add_page(index, route="./", title="Pau Tarrés")

app.add_page(project_page(airline_optimization()), route="./airline_optimization", title="Airline Optimization")
app.add_page(project_page(john_draim_constellation()), route="./john_draim_constellation", title="John Draim's Constellation")
app.add_page(project_page(personal_website()), route="./personal_website", title="Personal Website")
app.add_page(project_page(nonlagrangian_finite_elements()), route="./nonlagrangian_finite_element", title="Non-Lagrangian Finite Elements")