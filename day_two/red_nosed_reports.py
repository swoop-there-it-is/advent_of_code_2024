from typing import List


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
    if len(report) == 0:
        return False

    failures = 0
    issues: List[int] = [0]

    increasing = bool(report[0] < report[1])
    for i in range(len(report)):
        if i == 0:
            continue
        data_one = report[i-1]
        data_two = report[i]
        difference = 0
        if data_one > data_two:
            if increasing:
                failures += 1
                issues.append(i-1)
                issues.append(i)
                continue
            difference = data_one - data_two
        elif data_one < data_two:
            if not increasing:
                failures += 1
                issues.append(i-1)
                issues.append(i)
                continue
            difference = data_two - data_one
        if difference > 3 or difference <= 0:
            failures += 1
            issues.append(i-1)
            issues.append(i)
            continue

    if failures == 0:
        return True

    if part == 1:
        return False

    if rerun:
        # if this is a rerun just return False
        # Still an issue even after removing the problem
        return False

    # try seeing if removing the issue fixes the problem
    for index in issues:
        new_report = report.copy()
        del new_report[index]
        if is_report_safe(new_report, part, rerun=True):
            return True

    return False


def get_results(data: str, part: int):
    reports = get_red_nosed_reactor_reports(data)
    results = get_num_safe_reports(reports, part)
    return results
