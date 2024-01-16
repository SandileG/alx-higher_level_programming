#!/usr/bin/python3
"""
Defines a function that returns the JSON representation of an object.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        str: The JSON string representation of the object.
    """


def _default(obj):
    if isinstance(obj, (set, bytes)):
        return list(obj)
    raise TypeError(f"Object of type '{type(obj)}' not JSON serializable")

    return str(_json_encode(my_obj, default=_default))


def _json_encode(obj, default=None):
    if isinstance(obj, (str, int, float, bool, None)):
        return obj
    elif isinstance(obj, list):
        return [_json_encode(item, default=default) for item in obj]
    elif isinstance(obj, dict):
        return {
            str(key): _json_encode(value, default=default)
            for key, value in obj.items()
        }
    elif callable(default):
        return default(obj)
    else:
        raise TypeError(f"Object of type '{type(obj)}' is not JSONable.")
