import logging
import os
from typing import Callable

from nicegui import ui
from nicegui.elements.input import Input

from day_one import historian_hysteria
from day_two import red_nosed_reports

DayOfDecember = int

functions: dict[DayOfDecember: Callable] = {
    1: historian_hysteria.get_results,
    2: red_nosed_reports.get_results
}

puzzles: dict[DayOfDecember: str] = {
    1: historian_hysteria.PUZZLE,
    2: red_nosed_reports.PUZZLE,
}


def get_christmas_tree_image_path() -> str:
    christmas_tree_path = os.path.join(os.getcwd(), "images\\aocLogo.jpeg")
    return christmas_tree_path


def get_results(day_of_december: int, user_input: Input, part: int):
    try:
        user_input = user_input.value
        func = functions.get(day_of_december)
        if func is None:
            ui.notify("No results")
            return
        results = func(user_input, part)
        ui.notify(results)
    except Exception as e:
        logging.warning(f"Failed to get results for day {day_of_december}", exc_info=True)
        ui.notify("Issue occurred when getting results. Check logs.")


def get_puzzle(day_of_december: int):
    try:
        puzzle = puzzles.get(day_of_december, "No puzzle released yet")
        return puzzle
    except Exception as e:
        logging.warning(f"Failed to get puzzle for day {day_of_december}", exc_info=True)
        ui.notify("Issue occurred when getting puzzle. Check logs.")
