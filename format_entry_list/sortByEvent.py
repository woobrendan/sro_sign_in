# take  in array of entries, and sort by event in dict
from format_entry_list import events


def sortByEvent(all_entries):
    event_dict = {}

    for event in events:
        event_dict[event] = []
