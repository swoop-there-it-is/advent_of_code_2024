from nicegui import ui
from day_one import file


def get_results():
    user_data = int(data.value)
    results = file.func(user_data)
    ui.notify(results)


tabs: dict[int: ui.tab] = {}

with ui.tabs().classes('w-full') as tab:
    for i in range(25):
        day_of_christmas = i+1
        tabs[day_of_christmas] = ui.tab(f'Day {i+1}')

december_first = tabs[1]
with ui.tab_panels(tab, value=december_first).classes('w-full'):

    for i in range(25):
        tab = tabs[i+1]
        with ui.tab_panel(tab):
            data = ui.input('data')
            ui.button("get results", on_click=get_results)


ui.run()

if __name__ == "__main__":
    pass
