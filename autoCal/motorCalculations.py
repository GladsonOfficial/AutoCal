import autoCal.speedCalculations as sc


def motor_rpm_to_kmph(motor_rpm: float, tyre_size: float, drivetrain_ratio: float) -> float:
    """Calculates the speed of a motor in km/h from motor rpm and drivetrain ratio.

    Args:
        motor_rpm (float): motor RPM
        tyre_size (float): size of tyre in meters
        drivetrain_ratio (float): gear ratio

    Returns:
        float: return speed in km/h
    """
    wheel_rpm = motor_rpm / drivetrain_ratio
    return sc.wheel_rpm_to_kmph(wheel_rpm, tyre_size)

def motor_rpm_to_mph(motor_rpm: float, tyre_size: float, drivetrain_ratio: float) -> float:
    """Calculates the speed of a motor in mph from motor rpm and drivetrain ratio.

    Args:
        motor_rpm (float): motor RPM
        tyre_size (float): size of tyre in meters
        drivetrain_ratio (float): gear ratio

    Returns:
        float: returns speed in mph
    """
    wheel_rpm = motor_rpm / drivetrain_ratio
    return sc.wheel_rpm_to_mph(wheel_rpm, tyre_size)

def kmph_to_motor_rpm(kmph: float, tyre_size: float, drivetrain_ratio: float) -> float:
    """Calculates the motor rpm from speed in km/h.

    Args:
        motor_rpm (float): motor RPM
        tyre_size (float): size of tyre in meters
        drivetrain_ratio (float): gear ratio

    Returns:
        float: returns speed in RPM
    """
    wheel_rpm = sc.kmph_to_wheel_rpm(kmph, tyre_size)
    return wheel_rpm * drivetrain_ratio

def mph_to_motor_rpm(mph: float, tyre_size: float, drivetrain_ratio: float) -> float:
    """Calculates the motor RPM from speed in mph.

    Args:
        motor_rpm (float): motor RPM
        tyre_size (float): size of tyre in meters
        drivetrain_ratio (float): gear ratio

    Returns:
        float: returns speed in RPM
    """
    wheel_rpm = sc.mph_to_wheel_rpm(mph, tyre_size)
    return wheel_rpm * drivetrain_ratio

def wheel_rpm_to_motor_rpm(wheel_rpm: float, drivetrain_ratio: float) -> float:
    """Calculates the motor RPM from wheel RPM;

    Args:
        wheel_rpm (float): RPM of wheel
        drivetrain_ratio (float): gear ratio

    Returns:
        float: returns RPM of motor
    """
    return wheel_rpm * drivetrain_ratio

def motor_rpm_to_wheel_rpm(motor_rpm: float, drivetrain_ratio: float) -> float:
    """Calculates the wheel RPM from motor rpm.

    Args:
        motor_rpm (float): motor RPM
        drivetrain_ratio (float): gear ratio

    Returns:
        float: returns RPM of wheel
    """
    return motor_rpm / drivetrain_ratio

def motor_rpm_to_one_motor_rotation_time(motor_rpm: float) -> float:
    """Calculates the time required for motor to complete one rotation.

    Args:
        motor_rpm (float): RPM of motor

    Returns:
        float: returns time in seconds
    """
    return 60 / motor_rpm

def wheel_rpm_to_one_motor_rotation_time(wheel_rpm: float, drivetrain_ratio: float) -> float:
    """Calculates the time required for motor to complete one rotation.

    Args:
        wheel_rpm (float): RPM of wheel

    Returns:
        float: returns time in seconds
    """
    motor_rpm = wheel_rpm_to_motor_rpm(wheel_rpm, drivetrain_ratio)
    return 60 / motor_rpm


def get_hall_events_per_motor_rotation(pole_pairs: int) -> float:
    """Calculates the number of hall events in one rotation of motor.

    Args:
        pole_pairs (int): number of pole pairs

    Returns:
        float: number of hall events
    """
    return pole_pairs * 6

def get_hall_events_per_wheel_rotation(pole_pairs: int, drivetrain_ratio: float) -> float:
    """Calculates the number of hall events in one rotation of wheel.

    Args:
        pole_pairs (int): number of pole pairs
        drivetrain_ratio (float): drivetrain ratio

    Returns:
        float: number of hall events
    """
    return get_hall_events_per_motor_rotation(pole_pairs) * drivetrain_ratio

def get_hall_event_interval(motor_rpm: float, pole_pairs: int) -> float:
    """Calculates the time interval between two hall events.

    Args:
        motor_rpm (float): RPM of motor
        pole_pairs (int): number of pole pairs

    Returns:
        float: returns time interval in seconds
    """
    T = motor_rpm_to_one_motor_rotation_time(motor_rpm)
    hall_event_count = get_hall_events_per_motor_rotation(pole_pairs)
    return T / hall_event_count

def get_hall_events_per_second(motor_rpm: float, pole_pairs: int) -> float:
    """calculates the number of hall events per second

    Args:
        motor_rpm (float): RPM of motor
        pole_pairs (int): number of pole pairs

    Returns:
        float: returns number of hall events
    """
    rps = motor_rpm / 60
    hall_event_count = get_hall_events_per_motor_rotation(pole_pairs)
    return hall_event_count * rps

def get_hall_events_per_minute(motor_rpm: float, pole_pairs: float) -> float:
    """Calculates the number of hall events per minute

    Args:
        motor_rpm (float): RPM of motor
        pole_pairs (float): number of pole pairs

    Returns:
        float: returns the number of hall events
    """
    hall_event_count = get_hall_events_per_motor_rotation(pole_pairs)
    return hall_event_count * motor_rpm


