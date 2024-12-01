from typing import List


def _get_location_ids(data: str) -> (List[int], List[int]):
    location_ids = data.split()
    list_one = []
    list_two = []
    for index, location_id in enumerate(location_ids):
        location_id = int(location_id)
        if index % 2 == 0:
            list_one.append(location_id)
            continue
        list_two.append(location_id)
    return list_one, list_two


def _get_total_distance_between_lists(location_ids_one: List[int], location_ids_two: List[int]) -> int:
    location_ids_one = sorted(location_ids_one)
    location_ids_two = sorted(location_ids_two)

    result = 0
    for id_one, id_two in zip(location_ids_one, location_ids_two):
        if id_one == id_two:
            continue
        if id_one > id_two:
            result += (id_one - id_two)
            continue
        result += (id_two - id_one)

    return result


def _get_similarities_between_lists(location_ids_one: List[int], location_ids_two: List[int]) -> int:
    list_two_totals: dict[int: int] = {}
    for location_id in location_ids_two:
        if list_two_totals.get(location_id):
            list_two_totals[location_id] += 1
            continue
        list_two_totals[location_id] = 1

    results = 0
    for location_id in location_ids_one:
        total = list_two_totals.get(location_id, 0)
        results += (location_id * total)

    return results


def get_results(data: str, part: int) -> int:
    list_one, list_two = _get_location_ids(data)
    if part == 1:
        return _get_total_distance_between_lists(list_one, list_two)

    return _get_similarities_between_lists(list_one, list_two)
