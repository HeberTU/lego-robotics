"""Script to check battery related info."""
from pybricks.hubs import InventorHub


def main():
    """Start main function."""
    hub = InventorHub()
    print(f"Current: {hub.battery.current()}")
