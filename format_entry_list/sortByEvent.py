# take  in array of entries, and sort by event in dict
from format_entry_list.events import events_dict
import json
import copy


def sortByEvent(all_entries):
    entry_event_dict = copy.deepcopy(events_dict)

    for entry in all_entries:
        event_name = entry['eventLabel']

        entry_event_dict[event_name].append(entry)

    print(json.dumps(entry_event_dict, indent=4))

    return entry_event_dict
