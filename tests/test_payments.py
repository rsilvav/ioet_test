from payhours.calculate_payments import get_name_intervals, string_to_hour, get_day_payment


def test_name_intervals():
    assert get_name_intervals("TEST=MO00:00-24:00") == ("TEST", ["MO00:00-24:00"])
    assert get_name_intervals("TEST1=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00") == ("TEST1", ["MO10:00-12:00", "TU10:00-12:00", "TH01:00-03:00"])


def test_string_to_hour():
    assert string_to_hour("00:00") == 0
    assert string_to_hour("23:59") == 24
    assert string_to_hour("24:00") == 24


def test_day_payment():
    assert get_day_payment("MO00:00-01:00") == 25
    assert get_day_payment("MO00:00-24:00") == 480
    assert get_day_payment("MO00:00-00:00") == 0
    assert get_day_payment("MO00:00-23:59") == 480
    assert get_day_payment("SA00:00-23:59") == 600
