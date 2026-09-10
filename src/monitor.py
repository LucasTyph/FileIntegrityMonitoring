def compare(baseline_data: dict[str, str], new_data: dict[str, str]) -> dict[str, list]:
    modified = []
    deleted = []
    created = []

    for entry in baseline_data:
        if entry in new_data:
            if new_data[entry] != baseline_data[entry]:
                modified.append(entry)
        else:
            deleted.append(entry)

    for entry in new_data:
        if entry not in baseline_data:
            created.append(entry)

    return {
        "modified" : modified,
        "deleted" : deleted,
        "created" : created,
    }