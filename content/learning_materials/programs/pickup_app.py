"""Week 4: reusable arithmetic and an explicit program entry point."""


def planned_portions(portions_per_container, containers):
    """Multiply nonnegative integers (the caller must honor this precondition).

    A planning calculation may be zero. It does not approve food, reserve an
    offer, or establish that anything was collected or delivered.
    """
    return portions_per_container * containers


def main():
    planned = planned_portions(3, 4)
    print("Bread boxes: 4 containers")
    print(f"Planned portions: {planned}")


if __name__ == "__main__":
    main()
