class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None) -> None:
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name) -> None:
        self.passengers.append(name)

    def drop(self, name) -> None:
        self.passengers.remove(name)
