from nicegui import ui
from utils import aoc_utils

style_sheet = """
            <style>
                body {
                    background-color: #0e0f23; /* Light blue background */
                }
            </style>
            """


tabs: dict[int, ui.tab] = {}

with ui.tabs().classes("w-full") as tab:
    for i in range(25):
        day_of_christmas = i + 1
        tabs[day_of_christmas] = ui.tab(f"Day {day_of_christmas}").style("color:white;")

december_first = tabs[1]
with ui.tab_panels(tab, value=december_first).classes("w-full"):
    for i in range(25):
        day_of_december = i + 1
        tab = tabs[day_of_december]
        with ui.tab_panel(tab).style("background-color:#0e0f23;"):
            puzzle: str = aoc_utils.get_puzzle(day_of_december)
            message = (
                f"Here's the link to the advent of code puzzle: \n\n {puzzle} \n\n"
                "To get the answer, paste your puzzle input in the text area to the left."
            )

            ui.label("Puzzle Input:").style("color:white;")
            with ui.row():
                data = ui.textarea(
                    value="12 15 12 12\n"
                          "23 4 4 5 6\n"
                          "12 41 41 4 5 7\n"
                          "12 7 89 24\n"
                          "12 15 12 12\n"
                          "23 4 4 5 6\n"
                          "12 41 41 4 5 7\n"
                          "12 7 89 24"
                ).props('input-style="color: green"')
                ui.chat_message(
                    message, name="Robot", avatar="https://robohash.org/ui", stamp="Now"
                )

            with ui.row():
                ui.button(
                    "part one results",
                    on_click=lambda d=day_of_december, u=data: aoc_utils.get_results(
                        d, u, 1
                    ),  # Use default argument to capture `data`
                ).style("color: #0e0f23;")
                ui.button(
                    "part two results",
                    on_click=lambda d=day_of_december, u=data: aoc_utils.get_results(
                        d, u, 2
                    ),  # Use default argument to capture `data`
                ).style("color: #0e0f23;")

                for _ in range(15):
                    ui.space()

                christmas_tree_image_path = aoc_utils.get_christmas_tree_image_path()
                ui.image(christmas_tree_image_path).style(
                    "width: 600px; height: 600px;"
                )


ui.add_head_html(style_sheet)

ui.run()

if __name__ == "__main__":
    pass
