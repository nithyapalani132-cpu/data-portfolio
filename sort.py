def sort_dict(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

data = {"a": 5, "b": 2, "c": 8}
print(sort_dict(data))