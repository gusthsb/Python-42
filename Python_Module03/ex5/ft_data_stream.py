#!/usr/bin/env python3

import typing
import random


def get_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move",
               "climb", "swim", "use", "release"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        idx = random.randint(0, len(event_list) - 1)
        yield event_list.pop(idx)


def show_event() -> None:
    print("=== Game Data Stream Processor ===")
    init_event = get_event()
    for i in range(1000):
        event = next(init_event)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    event_list = list()
    for _ in range(10):
        event_list.append(next(init_event))
    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    show_event()
