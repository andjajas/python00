#!/usr/bin/env python3

def ft_harvest_total() -> None:
    day1_harvest = input("Day 1 harvest: ")
    day2_harvest = input("Day 2 harvest: ")
    day3_harvest = input("Day 3 harvest: ")
    total_harvest = int(day1_harvest) + int(day2_harvest) + int(day3_harvest)
    print(f"Total harvest: {total_harvest}")
