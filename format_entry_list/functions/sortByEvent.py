# take  in array of entries, and sort by event in dict
from format_entry_list.events import events_dict
from format_entry_list.convertEntry import convertEntry
import copy


def sortByEvent(all_entries):
    entry_event_dict = copy.deepcopy(events_dict)

    for entry in all_entries:
        event_name = entry['eventLabel']

        # convert entry into object entry list objs

        new_entry = convertEntry(entry)

        entry_event_dict[event_name].append(new_entry)

    return entry_event_dict