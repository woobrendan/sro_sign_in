# take  in array of entries, and sort by event in dict
from hmac import new
from format_entry_list.events import events_dict
from format_entry_list.convertEntry import convertEntry, convertSeries, convertClassif
import json
import copy


def sortByEvent(all_entries):
    entry_event_dict = copy.deepcopy(events_dict)

    for entry in all_entries:
        event_name = entry['eventLabel']

        # convert entry into object entry list objs

        new_entry = convertEntry(entry)

        new_entry['Car Series'] = convertSeries(new_entry['Car Series'])
        new_entry["Championship / Class"] = convertClassif(
            new_entry.get("Championship / Class"))
        print('new----', json.dumps(new_entry, indent=4))

        entry_event_dict[event_name].append(entry)

    print(json.dumps(entry_event_dict, indent=4))

    return entry_event_dict
