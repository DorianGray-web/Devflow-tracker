"""Main CLI entry point for engram."""

import argparse
import sys

from .commands.init import init_command


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="engram",
        description="Engram - Engineering Memory Platform"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init command
    init_parser = subparsers.add_parser(
        "init", help="Initialize a .engram/ workspace in the current Git repository"
    )
    init_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without writing any files"
    )
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Allow initialization even if not in a Git repository (use with caution)"
    )

    args = parser.parse_args(argv)

    if args.command == "init":
        return init_command(dry_run=args.dry_run, force=args.force)

    return 1


if __name__ == "__main__":
    sys.exit(main())
