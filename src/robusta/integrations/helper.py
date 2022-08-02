def exact_match(expected, field_value) -> bool:
    return True if expected is None else expected == field_value


def prefix_match(prefix: str, field_value: str) -> bool:
    if not prefix:
        return True

    return False if field_value is None else field_value.startswith(prefix)
