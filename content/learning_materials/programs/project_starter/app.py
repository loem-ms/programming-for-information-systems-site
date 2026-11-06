"""Optional entry point; does not change availability or record deliveries."""
import argparse
import sys
from policy import pickup_label


def main(argv=None):
    parser = argparse.ArgumentParser(description="Inspect a pickup coordination label.")
    parser.add_argument("total_portions", type=int)
    parser.add_argument("--reviewed", action="store_true")
    args = parser.parse_args(argv)
    try:
        label = pickup_label(args.total_portions, args.reviewed)
    except (ValueError, NotImplementedError) as error:
        print(str(error), file=sys.stderr)
        return 2
    print(label)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
