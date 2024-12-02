from typing import List

PUZZLE = "https://adventofcode.com/2024/day/2"


def get_red_nosed_reactor_reports(data: str) -> List[List[int]]:
    reports = data.split("\n")
    sep_reports = [[int(data) for data in report.split()] for report in reports]
    return sep_reports


def get_num_safe_reports(reports: List[List[int]], part: int) -> int:
    num_safe_reports: int = 0
    for report in reports:
        if not is_report_safe(report, part):
            continue
        num_safe_reports += 1
    return num_safe_reports


def is_report_safe(report: List[int], part: int, rerun: bool = False) -> bool:
    if not report or len(report) < 2:
        return False

    max_differences = 3
    failures = 0
    issues = {0}

    increasing = report[0] < report[1]

    for i in range(1, len(report)):
        prev, curr = report[i - 1], report[i]
        difference = abs(curr - prev)

        if (
            (increasing and curr < prev)
            or (not increasing and curr > prev)
            or not (0 < difference <= max_differences)
        ):
            failures += 1
            issues.update({i - 1, i})

    if failures == 0:
        return True

    if part == 1 or rerun:
        return False

    # Try removing each problematic index and rerun
    for index in sorted(issues):
        new_report = report[:index] + report[index + 1:]
        if is_report_safe(new_report, part, rerun=True):
            return True

    return False


def get_results(data: str, part: int):
    reports = get_red_nosed_reactor_reports(data)
    results = get_num_safe_reports(reports, part)
    return results
