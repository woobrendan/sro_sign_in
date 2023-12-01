from lib2to3.pytree import convert
from utility.convertEntry import convertEntry
from .api_mock import gt4_entry, gt4_expected


def test_convert_entry():
    api_received = gt4_entry
    expected = gt4_expected

    assert convertEntry(api_received) == expected
