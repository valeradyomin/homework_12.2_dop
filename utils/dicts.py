def get_val(collection: dict, key, default='git'):
    if key:
        return collection[key]
    else:
        return default