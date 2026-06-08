#!/usr/bin/env python3

def ft_water_reminder() -> None:
    days_since_watering = input("Days since last watering: ")
    if int(days_since_watering) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
