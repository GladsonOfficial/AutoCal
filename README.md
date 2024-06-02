# AutoCal
**__Work in progress. Currently under testing.__**

This Python library provides a comprehensive toolbox of mathematical formulas commonly encountered in the automotive industry, with a particular focus on electric vehicles (EVs) and Brushless DC (BLDC) motors. The library offers a valuable resource for engineers and researchers working on EV components, motor control systems, and related applications.

Developed by [Gladson Thomas](https://www.linkedin.com/in/gladson-thomas/) and [Sumati Ladane](https://www.linkedin.com/in/sumati-ladane-802b511a2/).


This repository provides a collection of mathematical formulas commonly used in the automotive industry, with a particular focus on Brushless DC (BLDC) motors.

## Installation
Binary installers are available at Python [Python Package Index (PyPi)](https://pypi.org/project/autoCal/).
```
pip install autoCal
```
The source code is hosted on github at https://github.com/GladsonOfficial/AutoCal

## Usage
The formulas are categorized into 2 parts. Speed calculations and motor calculations.

**Speed Calculation**: This contains the formulas related to general speed conversions.

List of functions:
```python
wheel_rpm_to_kmph(wheel_rpm: float, tyre_size: float) -> float:
wheel_rpm_to_mph(wheel_rpm: float, tyre_size: float) -> float:
kmph_to_wheel_rpm(kmph: float, tyre_size: float) -> float:
mph_to_wheel_rpm(mph: float, tyre_size: float) -> float:
wheel_rpm_to_time_required_for_one_wheel_rotation(rpm: float) -> float:
kmph_to_time_required_for_one_wheel_rotation(kmph: float, tyre_size: float) -> float:
mph_to_time_required_for_one_wheel_rotation(mph: float, tyre_size: float) -> float:
```

**Motor Calculations**: This contains the formulas related to BLDC motors.
List of functions:
```python
motor_rpm_to_kmph(motor_rpm: float, tyre_size: float, drivetrain_ratio: float) -> float:
motor_rpm_to_mph(motor_rpm: float, tyre_size: float, drivetrain_ratio: float) -> float:
kmph_to_motor_rpm(kmph: float, tyre_size: float, drivetrain_ratio: float) -> float:
mph_to_motor_rpm(mph: float, tyre_size: float, drivetrain_ratio: float) -> float:
wheel_rpm_to_motor_rpm(wheel_rpm: float, drivetrain_ratio: float) -> float:
motor_rpm_to_wheel_rpm(motor_rpm: float, drivetrain_ratio: float) -> float:
motor_rpm_to_one_motor_rotation_time(motor_rpm: float) -> float:
wheel_rpm_to_one_motor_rotation_time(wheel_rpm: float, drivetrain_ratio: float) -> float:
get_hall_events_per_motor_rotation(pole_pairs: int) -> float:
get_hall_events_per_wheel_rotation(pole_pairs: int, drivetrain_ratio: float) -> float:
get_hall_event_interval(motor_rpm: float, pole_pairs: int) -> float:
get_hall_events_per_second(motor_rpm: float, pole_pairs: int) -> float:
get_hall_events_per_minute(motor_rpm: float, pole_pairs: float) -> float:
```

## Examples
Finding time required for wheel to complete one full rotation using km/h
```python
from autoCal import speedCalculations as sc
print(sc.kmph_to_time_required_for_one_wheel_rotation(25, uc.inch_to_m(26)))
```