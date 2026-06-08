#!/usr/bin/env python3

def helper_count_harvest(day, total_days) -> None:
    if day == total_days + 1:
        print("Harvest time!")
        return
    print(f"Day {day}")
    day += 1
    helper_count_harvest(day, total_days)


def ft_count_harvest_recursive() -> None:
    days_to_harvest = input("Days until harvest: ")
    total_days = int(days_to_harvest)
    day = 1
    helper_count_harvest(day, total_days)
