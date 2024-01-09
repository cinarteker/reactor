import os
import sys

__all__ = []


def main():
    """Set up the project's configuration and run a Django command."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reactor.settings")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Development")

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
