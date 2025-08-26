def bound_to_180(angle):
    """Normalize angle into range [-180, 180)."""
    
    # find equivalent positive angle
    # To get [0,360] angle , we define args = k*360 + target
    # target = angle mod 360
    # to change boundary to [-180, 180), we can use the formula
    # target belongs [0,360)
    # if target > 180 return -1 * (180 - target%180)
    # else return target
    target = angle % 360
    return -1 * (360 - target) if target >= 180 else target


def is_angle_between(first_angle, middle_angle, second_angle):
    """Check if middle_angle is between first_angle and second_angle."""

    # find acceptable interval
    first_angle = bound_to_180(first_angle)
    second_angle = bound_to_180(second_angle)
    middle_angle = bound_to_180(middle_angle)
    
    # update sequence
    first_angle, second_angle = min(first_angle, second_angle), max(first_angle, second_angle)
    
    # check between interval in normal situation
    # *when angle overlap, also consider equal case
    between = first_angle <= middle_angle <= second_angle
    
    # note 180 when 180 degrees (half circle is include since the definition did not specifically mention)
    return not between if (second_angle - first_angle) >= 180 else between

