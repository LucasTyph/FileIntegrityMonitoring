def compare(baseline_data: dict[str, str], new_data: dict[str, str]) -> dict[str, str]:
    result = {}
    for entry in baseline_data:
        if entry in new_data:
            if new_data[entry] != baseline_data[entry]:
                result[entry] = "[MODIFIED] - " + entry
        else:
            result[entry] = "[DELETED] - " + entry

    for entry in new_data:
        if entry not in baseline_data:
            result[entry] = "[CREATED] - " + entry
    return result