from utility.convertEntry import convertEntry
from tests.test_entry.api_mock import gt4_api, gt4_expected, gt3_api, gt3_expected


# Test GT4
def test_convert_entry():
    api_received = gt4_api
    expected = gt4_expected
    converted = convertEntry(api_received)

    assert set(converted.keys()) == set(expected.keys())
    assert set(converted.values()) == set(expected.values())


# Test GTWC
def test_convert_entry():
    api_received = gt3_api
    expected = gt3_expected
    converted = convertEntry(api_received)

    assert expected == converted, "Expected convert Entry function to take in GTWC api entry and convert it into easy to read dict"
