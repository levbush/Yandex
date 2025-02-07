def from_string_to_list(string, container):
    for el in string.split():
        container.append(int(el))
