from standard_calc import bound_to_180, is_angle_between

""" Tests for bound_to_180() """


def test_bound_basic1():

    assert bound_to_180(0) == 0
    assert bound_to_180(191.6) == -168.4
    assert bound_to_180(180) == -180
    assert bound_to_180(-181) == 179
    assert bound_to_180(-540) == -180


def test_between_basic1():

    assert is_angle_between(0, 1, 2)
    assert not is_angle_between(0, 180, 359)
    assert not is_angle_between(0, 190, 270) 
    assert is_angle_between(181.46, 180.9, 179.3)
    assert is_angle_between(-170, 179, 170)
    assert is_angle_between(-170, 180, 170)
