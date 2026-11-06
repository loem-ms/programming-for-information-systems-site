"""Week 6: a planning object, not approval or automatic database persistence.

Public attributes remain mutable. Constructor checks validate creation only.
"""


class OfferLine:
    """One batch planning line with nonnegative integer planning counts."""

    def __init__(self, batch_id, portions_per_container, containers):
        if not isinstance(batch_id, str) or not batch_id.strip():
            raise ValueError("batch_id must be a nonblank string")
        if type(portions_per_container) is not int or portions_per_container < 0:
            raise ValueError("portions_per_container must be a nonnegative integer")
        if type(containers) is not int or containers < 0:
            raise ValueError("containers must be a nonnegative integer")
        self.batch_id = batch_id
        self.portions_per_container = portions_per_container
        self.containers = containers

    def total_portions(self):
        return self.portions_per_container * self.containers


def main():
    line = OfferLine("DEMO-B1", 3, 4)
    print(line.batch_id, line.containers, line.total_portions())


if __name__ == "__main__":
    main()
