from pybricks.hubs import InventorHub

def main():

    hub = InventorHub()
    print(f"Current: {hub.battery.current()}")