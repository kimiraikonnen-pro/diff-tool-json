import json

def load_json(filepath):
    with open(filepath, "r") as f:
        return json.load(f)


def diff_dicts(old, new, path=""):
    changes = []

    for key in old:
        current_path = f"{path}.{key}" if path else key

        if key not in new:
            changes.append(f"removed: '{current_path}' (was {old[key]})")
        elif isinstance(old[key], dict) and isinstance(new[key], dict):
            changes.extend(diff_dicts(old[key], new[key], current_path))
        elif isinstance(old[key], list) and isinstance(new[key], list):
            changes.extend(diff_lists(old[key], new[key], current_path))
        elif old[key] != new[key]:
            changes.append(f"changed: '{current_path}' from {old[key]} to {new[key]}")

    for key in new:
        if key not in old:
            current_path = f"{path}.{key}" if path else key
            changes.append(f"added: '{current_path}' = {new[key]}")

    return changes


def diff_lists(old_list, new_list, path=""):
    changes = []

    removed_items = [item for item in old_list if item not in new_list]
    added_items = [item for item in new_list if item not in old_list]

    for item in removed_items:
        changes.append(f"removed from '{path}': {item}")

    for item in added_items:
        changes.append(f"added to '{path}': {item}")

    return changes


