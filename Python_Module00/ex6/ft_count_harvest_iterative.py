def ft_count_harvest_iterative() -> None:
    start_day: int = int(input("Days until harvest: "))
    for i in range(1, start_day + 1):
        print(f"Day {i}")
    print("Harvest time!")
