#!/usr/bin/env python3

def ft_count_harvest_iterative() -> None:
    days_to_harvest = input("Days until harvest: ")
    for day in range(1, int(days_to_harvest) + 1):
        print(f"Day {day}")
    print("Harvest time!")
