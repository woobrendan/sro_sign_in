# Take in sort array of classes to sort by desired class
def sortEntriesByClass(entry_arr, sort_arr):
    entries = {}

    for entry in entry_arr:
        classif = entry['class']
        exists = entries.get(classif)

        if exists:
            entries[classif].append(entry)
        else:
            entries[classif] = [entry]

    ordered = []
    for car_class in sort_arr:
        entry_arr = entries.get(car_class)
        if entry_arr:
            ordered += entry_arr

    return ordered
