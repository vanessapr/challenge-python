def flatten(list_of_lists: list):
    if type(list_of_lists) is not list:
        raise TypeError('Input is not valid. It should be a list.')

    flat = []
    for item in list_of_lists:
        if type(item) is list:
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat
