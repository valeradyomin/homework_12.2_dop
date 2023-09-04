def app_list(collection: list, item=None):
    if item:
        new_collection = collection
        new_collection.append(item)
        return new_collection
    else:
        return collection
