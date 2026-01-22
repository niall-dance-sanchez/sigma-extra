"""Practice tech assessment"""


def count_items(instructions: str) -> int:
    """Counts the number of items stored by the robot after a set of instructions."""

    count = 0
    for char in instructions:
        if char == "^":
            count += 1
            if count > 5:
                raise ValueError("Can't carry more than 5 objects!")
        elif char == "v" and count != 0:
            count -= 1

    return count


def heaviest_load(instructions: str) -> int:
    """Returns the heaviest load carried during a set of instructions"""

    count = 0
    loads = []
    for char in instructions:
        if char == "^":
            count += 1
            if count > 5:
                return 0
        elif char == "v" and count != 0:
            count -= 1
        loads.append(count)

    return max(loads)


def instruction_set_heaviest_load(instruction_set: list[str]) -> int:
    """Returns the index of the heaviest load of an instruction"""

    loads = []
    for instruction in instruction_set:
        loads.append(heaviest_load(instruction))

    return loads.index(max(loads))


if __name__ == "__main__":
    pass
