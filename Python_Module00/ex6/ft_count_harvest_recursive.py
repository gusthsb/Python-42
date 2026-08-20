def ft_count_harvest_recursive() -> None:
    harvest_days: int = int(input("Days until harvest: "))

    def ft_helper(current_day: int, final_day: int) -> None:
        if current_day > final_day:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        ft_helper(current_day + 1, final_day)

    ft_helper(1, harvest_days)
