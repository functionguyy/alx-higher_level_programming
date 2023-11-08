"""Module defines function class_to_json."""


def class_to_json(obj):
    """returns the dictionary description for JSON serialization of an
    object.

    args:
        obj: instance of a Class
    returns:
        dictionary object
    """
    # check that object passed has __dict__ attribute
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    else:
        return {}
