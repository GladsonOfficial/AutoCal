import math


def radius_to_circumference(radius: float) -> float:
    """Calculates circumference using radius.

    Args:
        radius (float): radius

    Returns:
        float: circumference
    """
    return 2 * math.pi * radius

def diameter_to_circumference(diameter: float) -> float:
    """Calculates circumference using diameter

    Args:
        diameter (float): diameter

    Returns:
        float: circumference
    """
    return 2 * math.pi * diameter / 2