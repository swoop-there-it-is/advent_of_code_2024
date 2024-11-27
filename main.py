import os

from nicegui import ui
from day_one import file
from utils import aoc_utils

style_sheet = """
            <style>
                body {
                    background-color: #0e0f23; /* Light blue background */
                }
            </style>
            """


def get_results(arg):
    user_data = int(arg.value)
    results = file.func(user_data)
    ui.notify(results)


tabs: dict[int, ui.tab] = {}

with ui.tabs().classes("w-full") as tab:
    for i in range(25):
        day_of_christmas = i + 1
        tabs[day_of_christmas] = ui.tab(f"Day {day_of_christmas}").style("color:white;")

december_first = tabs[1]
with ui.tab_panels(tab, value=december_first).classes("w-full"):
    for i in range(25):
        tab = tabs[i + 1]
        with ui.tab_panel(tab).style("background-color:#0e0f23;"):
            data = ui.input(f"data for day {i + 1}").style("color:white;")
            ui.button(
                "get results",
                on_click=lambda d=data: get_results(
                    d
                ),  # Use default argument to capture `data`
            ).style('color: #0e0f23;')
            christmas_tree_image_path = aoc_utils.get_christmas_tree_image_path()
            ui.image(christmas_tree_image_path).style("width: 600px; height: 600px;")

ui.add_head_html(style_sheet)

ui.run()

if __name__ == "__main__":
    pass
