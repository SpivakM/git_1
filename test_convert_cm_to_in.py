import library


def test_convert_cm_to_in_for_0():
    result = library.convert_cm_to_in(0)
    assert result == 0


def test_convert_cm_to_in_for_positive_int():
    result = library.convert_cm_to_in(13)
    assert result == 5.1181


def test_convert_cm_to_in_for_negative_int():
    result = library.convert_cm_to_in(-13)
    assert result == -5.1181


def test_convert_cm_to_in_for_positive_float():
    result = library.convert_cm_to_in(0.03)
    assert result == 0.01181


def test_convert_cm_to_in_for_negative_float():
    result = library.convert_cm_to_in(-0.03)
    assert result == -0.01181
