import random, typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release", "use"]
    event = ["", ""]

    while True:
        event[0] = random.choice(names)
        event[1] = random.choice(actions)
        yield (event[0], event[1])


def consume_event(events: list) -> typing.Generator[list, None, None]:
    while len(events) > 0:
        idx = random.randint(0, len(events) - 1)
        print("Got event from list:", events[idx])
        events = events[:idx] + events[idx+1:]

        yield events


if __name__ == "__main__":
    values = gen_event()
    event = ()

    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        event = next(values)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    print()
    lst_events = [next(gen_event()) for _ in range(10)]
    print("Built list of 10 events:",lst_events)
    consume = consume_event(lst_events)
    for i in range(10):
        lst_events = next(consume)
        print("Remains in list:", lst_events)
    print()    