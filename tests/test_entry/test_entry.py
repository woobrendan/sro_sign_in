from utility.convertEntry import convertEntry
from tests.test_entry.api_mock import gt4_entry, gt4_expected


def test_convert_entry():
    api_received = gt4_entry
    expected = gt4_expected
    converted = convertEntry(api_received)

    assert set(converted.keys()) == set(expected.keys())
    assert set(converted.values()) == set(expected.values())
