def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """
    #find equivalent positive angle
    # To get [0,360] angle , we define args = k*360 + target
    # target = angle mod 360
    # to change boundary to [-180, 180), we can use the formula
    # target belongs [0,360)
    # if target > 180 return -1 * (180 - target%180)
    # else return target
    target = angle % 360
    return -1 * (360 - target) if target >= 180 else target

def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """
    #find acceptable interval
    first_angle = bound_to_180(first_angle)
    second_angle = bound_to_180(second_angle)
    middle_angle = bound_to_180(middle_angle)
    #update sequence
    first_angle, second_angle = min(first_angle, second_angle), max(first_angle, second_angle)
    #check between interval in normal situation
    #*when angle overlap, also consider equal case
    between = first_angle <= middle_angle <= second_angle
    #note 180 when 180 degrees (half circle is include since the definition did not specifically mention)
    return not between if (second_angle - first_angle) >= 180 else between

