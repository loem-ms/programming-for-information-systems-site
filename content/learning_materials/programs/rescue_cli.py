"""Week 5: parse a planning command; actual reservations are a later lesson."""
import argparse
import sys

from pickup_app import planned_portions


def main(argv=None):
    parser = argparse.ArgumentParser(description="Calculate declared planned portions.")
    parser.add_argument("--portions-per-container", type=int, default=3)
    parser.add_argument("--containers", type=int, default=4)
    args = parser.parse_args(argv)
    if args.portions_per_container <= 0 or args.containers <= 0:
        print("portions per container and containers must be positive", file=sys.stderr)
        return 2
    print(f"Planned portions: {planned_portions(args.portions_per_container, args.containers)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
