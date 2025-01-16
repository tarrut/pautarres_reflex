import reflex as rx

from ..projects_utils import markdown_style, load_markdown_file, load_csv_file

project = "airline_optimization"

def airline_optimization():
    return rx.box(
        rx.markdown(load_markdown_file("script1.md", project), component_map=markdown_style),
        rx.data_table(
            data=load_csv_file("schedule.csv", project),
            pagination=True,
        ),
        rx.markdown(load_markdown_file("script2.md", project), component_map=markdown_style),
        rx.data_table(
            data=load_csv_file("flight_info.csv", project),
            pagination=True,
        ),
        rx.markdown(load_markdown_file("script3.md", project), component_map=markdown_style),
        rx.data_table(
            data=load_csv_file("fleet_dist.csv", project),
            pagination=True,
        ),
        rx.markdown(load_markdown_file("script4.md", project), component_map=markdown_style),
        rx.data_table(
            data=load_csv_file("aircrafts_combinations.csv", project),
            pagination=False,
        ),
        rx.markdown(load_markdown_file("script5.md", project), component_map=markdown_style),
        rx.data_table(
            data=load_csv_file("routings_fleet1.csv", project),
            pagination=False,
        ),
        rx.markdown("On the other hand, the routings selected for the A321 are:", component_map=markdown_style),
        rx.data_table(
            data=load_csv_file("routings_fleet2.csv", project),
            pagination=False,
        ),
        rx.markdown(load_markdown_file("script6.md", project), component_map=markdown_style),
        rx.data_table(
            data=load_csv_file("stranded_original.csv", project),
            pagination=False,
        ),
        rx.markdown("Modified schedule:", component_map=markdown_style),
        rx.data_table(
            data=load_csv_file("stranded_modified.csv", project),
            pagination=False,
        ),
        rx.markdown(load_markdown_file("script7.md", project), component_map=markdown_style),
        rx.data_table(
            data=load_csv_file("routings_modified_fleet1.csv", project),
            pagination=False,
        ),
        rx.markdown("This table shows the maintenance opportunities during the three-day routings:", component_map=markdown_style),
        rx.data_table(
            data=load_csv_file("maintenance_fleet2.csv", project),
            pagination=False,
        ),
        rx.markdown("The solution for A321 is:", component_map=markdown_style),
        rx.data_table(
            data=load_csv_file("routings_modified_fleet2.csv", project),
            pagination=False,
        ),
        rx.markdown("And, this fleet has 18 maintenance opportunities:", component_map=markdown_style),
        rx.data_table(
            data=load_csv_file("maintenance_fleet1.csv", project),
            pagination=False,
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