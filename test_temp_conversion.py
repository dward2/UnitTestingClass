def test_convert_c_to_f():
    from temp_conversion import convert_c_to_f

    answer = convert_c_to_f(20)

    assert answer == 68.0


def test_fever_detection():
    from temp_conversion import fever_detection

    temperatures = [98.0, 99.0, 100.0, 101.0]
    max_temp, has_fever = fever_detection(temperatures)

    assert max_temp == 101.0
    assert has_fever is False


def test_fever_detection2():
    from temp_conversion import fever_detection

    temperatures = [98.0, 99.0, 100.0, 100.0]
    max_temp, has_fever = fever_detection(temperatures)

    assert max_temp == 100.0
    assert has_fever is False
