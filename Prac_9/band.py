class Band:
    """Represents a musical band with members and methods for managing them."""
    def __init__(self, name=""):
        """Initialize the Band with a name and an empty list of members."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string that describes the Band, including its name and members."""
        return f"{self.name} ({self.members})"

    def __repr__(self):
        """Return a string that shows the internal state of the Band."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band's member list."""
        self.members.append(musician)

    def play(self):
        """Simulate the band playing a performance."""
        if not self.members:
            return f"{self.name} has no members!"
        performance = f"{self.name} is playing:"
        for musician in self.members:
            performance += f" {musician.play()}"
        return performance
